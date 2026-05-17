import uuid

from pydantic import BaseModel


class LLMPlatformOut(BaseModel):
    id: uuid.UUID
    name: str
    company: str
    ecosystem: str
    country: str
    default_access_method: str
    supports_api: bool
    supports_openai_compatible: bool
    supports_search: bool
    supports_citation: bool
    supports_browser_access: bool
    status: str

    model_config = {"from_attributes": True}
