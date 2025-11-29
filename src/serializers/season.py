from pydantic import BaseModel, ConfigDict, Field


class SeasonSerializer(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., description="The ID of the season.")
    name: str = Field(description="The name of the season.")
    year: str = Field(description="The year of the season.")
