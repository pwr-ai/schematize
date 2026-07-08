from importlib.metadata import version

import schematize


def test_version():
    assert schematize.__version__ == version("schematize")


def test_public_exports():
    assert hasattr(schematize, "SchemaGenerator")
    assert hasattr(schematize, "SchemaEvaluator")
    assert hasattr(schematize, "DocumentRetriever")
    assert hasattr(schematize, "SchemaFields")
    assert hasattr(schematize, "FieldDef")
    assert hasattr(schematize, "NamedFieldDef")
    assert hasattr(schematize, "FieldType")
    assert hasattr(schematize, "DynamicModelFactory")
    assert hasattr(schematize, "load_prompts")
    assert hasattr(schematize, "agent_state_to_json")


def test_schema_model():
    from schematize.schema.model import DynamicModelFactory, NamedFieldDef, SchemaFields

    spec = SchemaFields(
        fields=[
            NamedFieldDef(name="age", type_="integer", description="Age in years"),
            NamedFieldDef(name="name", type_="string", description="Full name"),
        ]
    )
    factory = DynamicModelFactory()
    Model = factory(spec)
    instance = Model(age=30, name="Alice")
    assert instance.age == 30
    assert instance.name == "Alice"


def test_schema_model_enum():
    from schematize.schema.model import DynamicModelFactory, NamedFieldDef, SchemaFields

    spec = SchemaFields(
        fields=[
            NamedFieldDef(
                name="role",
                type_="enum",
                enum_name="RoleEnum",
                enum_values=["admin", "user"],
                description="User role",
            )
        ]
    )
    factory = DynamicModelFactory()
    Model = factory(spec)
    instance = Model(role="admin")
    assert instance.role.value == "admin"


def test_document_retriever_protocol():
    from schematize.retrieval.base import DocumentRetriever

    class MyRetriever:
        async def __call__(self, query: str, max_docs: int = 100) -> list:
            return []

    assert isinstance(MyRetriever(), DocumentRetriever)


def test_huggingface_import_guard():
    import importlib
    import importlib.util
    import sys

    hf_modules = [k for k in sys.modules if k.startswith(("datasets", "sentence_transformers", "faiss"))]
    for mod in hf_modules:
        del sys.modules[mod]

    if importlib.util.find_spec("datasets") is None or importlib.util.find_spec("faiss") is None:
        import pytest

        with pytest.raises(ImportError, match="schematize\\[huggingface\\]"):
            import schematize.retrieval.huggingface  # noqa: F401

            importlib.reload(schematize.retrieval.huggingface)


def test_weaviate_import_guard():
    import importlib
    import sys

    weaviate_modules = [k for k in sys.modules if "weaviate" in k]
    for mod in weaviate_modules:
        del sys.modules[mod]

    import importlib.util

    if importlib.util.find_spec("weaviate") is None:
        import pytest

        with pytest.raises(ImportError, match="schematize\\[weaviate\\]"):
            import schematize.retrieval.weaviate  # noqa: F401
            importlib.reload(schematize.retrieval.weaviate)


def test_load_prompts_bad_language():
    import pytest

    with pytest.raises(AssertionError):
        schematize.load_prompts("de", "tax")


def test_load_prompts_bad_system_type():
    import pytest

    with pytest.raises(AssertionError):
        schematize.load_prompts("en", "medical")


def test_load_prompts_en_tax():
    prompts = schematize.load_prompts("en", "tax")
    assert "problem_definer_helper_prompt" in prompts
    assert "schema_generator_prompt" in prompts


def test_load_prompts_pl_law():
    prompts = schematize.load_prompts("pl", "law")
    assert "problem_definer_helper_prompt" in prompts
