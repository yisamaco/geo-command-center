import uuid

from pydantic import BaseModel


class KnowledgeEntityOut(BaseModel):
    id: uuid.UUID
    entity_type: str
    name: str
    slug: str
    short_definition: str | None = None
    language: str
    region: str
    status: str

    model_config = {"from_attributes": True}
