import uuid

from pydantic import BaseModel


class GeoRunOut(BaseModel):
    id: uuid.UUID
    run_name: str | None = None
    prompt: str
    access_method: str
    run_mode: str
    consumer_surface: str | None = None
    viewport_type: str | None = None

    model_config = {"from_attributes": True}
