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
    name: str = Field(..., description="Name of the field")


class SchemaFields(BaseModel):
    fields: list[NamedFieldDef]


class DynamicModelFactory:
    def __call__(self, spec: SchemaFields) -> type[BaseModel]:
        return create_model(
            "SchemaModel",
            **{field.name: field.to_field() for field in spec.fields},
        )
