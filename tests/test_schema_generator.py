import pytest
from langgraph.graph import END

from schematize.schema.model import DynamicModelFactory, SchemaFields


def _assert_valid_schema(state: dict) -> None:
    schema = state["current_schema"]
    assert isinstance(schema, SchemaFields)
    assert schema.fields
    # The produced schema must be usable to build a Pydantic extraction model.
    DynamicModelFactory()(schema)


def test_full_pipeline_end_to_end(make_generator):
    generator = make_generator()
    state = generator.get_complete_results("Extract parties and amounts from contracts")

    _assert_valid_schema(state)
    assert state["end_conversation"] is True
    assert state["problem_definition"]
    assert state["query"]
    assert state["schema_history"]          # accumulated across generation + refinement
    assert state["token_usage"]             # usage recorded per node
    assert state["refinement_rounds"] >= 1
    assert state["data_refinement_rounds"] >= 1


def test_stream_graph_updates_returns_final_state(make_generator):
    generator = make_generator()
    state = generator.stream_graph_updates("Extract parties and amounts from contracts")

    _assert_valid_schema(state)
    assert state["end_conversation"] is True


@pytest.mark.parametrize(
    ("skip_problem_definition", "skip_refinement", "skip_data_grounded"),
    [
        (False, False, False),
        (True, False, False),
        (False, True, False),
        (False, False, True),
        (True, True, True),
    ],
)
def test_pipeline_with_skipped_stages(
    make_generator, skip_problem_definition, skip_refinement, skip_data_grounded
):
    generator = make_generator(
        skip_problem_definition=skip_problem_definition,
        skip_refinement=skip_refinement,
        skip_data_grounded=skip_data_grounded,
    )
    state = generator.get_complete_results("Extract parties and amounts from contracts")

    _assert_valid_schema(state)
    assert state["end_conversation"] is True


@pytest.mark.parametrize(
    ("rounds", "needs_refinement", "skip_data_grounded", "expected"),
    [
        (0, False, False, "llm_schema_refiner"),      # below min -> refine
        (0, False, True, "llm_schema_refiner"),
        (2, False, False, "llm_schema_data_assessment"),  # min reached, no refinement needed
        (2, False, True, "summarizer"),               # ...and data grounding skipped
        (2, True, False, "llm_schema_refiner"),       # still needs refinement, under max
        (3, True, False, "llm_schema_data_assessment"),   # max reached -> stop refining
    ],
)
def test_route_after_assessment(make_generator, rounds, needs_refinement, skip_data_grounded, expected):
    generator = make_generator(
        skip_data_grounded=skip_data_grounded,
        min_refinement_rounds=2,
        max_refinement_rounds=3,
    )
    state = {
        "assessment_result": {"needs_refinement": needs_refinement},
        "refinement_rounds": rounds,
    }
    assert generator.route_after_assessment(state) == expected


@pytest.mark.parametrize(
    ("rounds", "needs_refinement", "expected"),
    [
        (0, False, "llm_schema_data_refiner"),   # below min -> refine
        (2, False, "summarizer"),                # min reached, no refinement needed
        (2, True, "llm_schema_data_refiner"),    # still needs refinement, under max
        (3, True, "summarizer"),                 # max reached -> stop
    ],
)
def test_route_after_data_assessment_merger(make_generator, rounds, needs_refinement, expected):
    generator = make_generator(min_data_refinement_rounds=2, max_data_refinement_rounds=3)
    state = {
        "merged_data_assessment": {"needs_refinement": needs_refinement},
        "data_refinement_rounds": rounds,
    }
    assert generator.route_after_data_assessment_merger(state) == expected


@pytest.mark.parametrize(
    ("end_conversation", "expected"),
    [(True, END), (False, "human_message")],
)
def test_route_after_chat(make_generator, end_conversation, expected):
    generator = make_generator()
    assert generator.route_after_chat({"end_conversation": end_conversation}) == expected


def test_use_interrupt_not_implemented(fake_llm, fake_retriever, prompts):
    with pytest.raises(NotImplementedError):
        from schematize.agents.schema_generator import SchemaGenerator

        SchemaGenerator(fake_llm, fake_retriever, prompts, use_interrupt=True)
