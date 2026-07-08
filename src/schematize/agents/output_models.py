from pydantic import BaseModel, Field

from schematize.schema.model import SchemaFields


class SchemaGenerationOutput(BaseModel):
    model_config = {"populate_by_name": True}

    justification: list[str] = Field(default_factory=list, description="Explanations for design choices")
    error: str | None = Field(default=None, description="Error message if generation failed")
    is_generated: bool = Field(description="True if schema was successfully generated")
    schema_: SchemaFields | None = Field(default=None, alias="schema", description="The generated extraction schema")


class SchemaRefinementOutput(BaseModel):
    model_config = {"populate_by_name": True}

    justification: list[str] = Field(default_factory=list, description="Explanations for each change made")
    error: str | None = Field(default=None, description="Error message if refinement failed")
    is_refined: bool = Field(description="True if schema was modified")
    schema_: SchemaFields | None = Field(default=None, alias="schema", description="The refined extraction schema")


class SchemaAssessmentOutput(BaseModel):
    overall_score: float = Field(description="Overall quality score")
    criteria_scores: str = Field(description="JSON object with criterion names as keys and scores (1-5) as integer values")
    strengths: list[str] = Field(description="List of schema strengths")
    weaknesses: list[str] = Field(description="List of schema weaknesses")
    improvement_suggestions: list[str] = Field(description="Specific improvement recommendations")
    is_high_quality: bool = Field(description="True if schema meets quality threshold")
    needs_refinement: bool = Field(description="True if schema needs refinement")
    assessment_summary: str = Field(description="Brief summary of the assessment")


class DataAssessmentMergerOutput(BaseModel):
    summary: str = Field(description="Brief summary with specific field mentions")
    main_issues: list[str] = Field(description="Specific problems with field names")
    strengths: list[str] = Field(description="Schema strengths with examples")
    needs_refinement: bool = Field(description="Whether refinement is needed")
    confidence: str = Field(description="Confidence level: high, medium, or low")
    priority_areas: list[str] = Field(description="Specific fields needing attention")


class ChatOutput(BaseModel):
    model_config = {"populate_by_name": True}

    justification: list[str] | None = Field(default=None, description="Explanations for changes")
    is_refined: bool = Field(description="True if schema was modified")
    schema_: SchemaFields | None = Field(default=None, alias="schema", description="The refined extraction schema")
    end_conversation: bool = Field(description="True to terminate the chat loop")
