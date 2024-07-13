from pydantic import BaseModel, Field


class XPTORequest(BaseModel):
    location: str = Field(min_length=1, max_length=249)

    class Config:
        frozen = False
        json_schema_extra = {
            "example": {
                "location": "location-XPTO",
            }
        }
