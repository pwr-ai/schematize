from enum import Enum, StrEnum
from typing import Any

from pydantic import BaseModel, Field, create_model
from pydantic.fields import FieldInfo


class FieldType(StrEnum):
    string = "string"
    integer = "integer"
    boolean = "boolean"
    float_ = "float"
    enum = "enum"


TYPE_MAP = {
    FieldType.string: str,
    FieldType.integer: int,
    FieldType.boolean: bool,
    FieldType.float_: float,
}


class FieldDef(BaseModel):
    """Definition of a single extraction field.

    Attributes:
        type_: Data type — one of `string`, `integer`, `boolean`, `float`, or `enum`.
        enum_name: Name for the dynamically created enum type (required when `type_` is `enum`).
        enum_values: Allowed values when `type_` is `enum`.
        description: Human-readable description of what this field captures.
    """

    type_: FieldType = Field(..., description="Data type of the field (string, integer, boolean, float, or enum)")
    enum_name: str | None = Field(default=None, description="Name of the enum type if type is enum")
    enum_values: list[str] = Field([], description="List of allowed values if type is enum")
    description: str = Field(..., description="Description of the field")

    def to_field(self) -> tuple[Any, FieldInfo]:
        if self.type_ == FieldType.enum:
            py_type = Enum(self.enum_name, {v: v for v in self.enum_values})  # type: ignore[misc]
        else:
            py_type = TYPE_MAP[self.type_]
        return (py_type, Field(default=..., description=self.description))


class NamedFieldDef(FieldDef):
    """A `FieldDef` with an attached field name, used in `SchemaFields`."""

    name: str = Field(..., description="Name of the field")


class SchemaFields(BaseModel):
    """Container for the full set of named fields in a generated schema."""

    fields: list[NamedFieldDef]


class DynamicModelFactory:
    """Creates a typed Pydantic `BaseModel` subclass from a `SchemaFields` spec at runtime.

    Example:
        ```python
        factory = DynamicModelFactory()
        model_cls = factory(spec)
        instance = model_cls(violation_type="privacy", severity=3)
        ```
    """

    def __call__(self, spec: SchemaFields) -> type[BaseModel]:
        return create_model(
            "SchemaModel",
            **{field.name: field.to_field() for field in spec.fields},
        )
