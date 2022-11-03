from pydantic import BaseModel
from typing import Optional

class AttributeSchema(BaseModel):
    trait_type: str | None
    type_: str | None
    value: str

class CollectionSchema(BaseModel):
    name: str
    id_: str
    attributes: list[AttributeSchema]

class NFTSchema(BaseModel):
    format: str
    name: str
    description: str
    minting_tool: Optional[str]
    sensitive_content: bool
    series_number: int
    series_total: int
    attributes: list[AttributeSchema]
    collection: CollectionSchema
