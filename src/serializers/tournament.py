from pydantic import BaseModel, ConfigDict, Field

class TournamentSerializer(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., description="The ID of the tournament.")
    name: str = Field(description="The name of the tournament.")
    has_rounds: bool = Field(description="Does the tournament have rounds?")
    start_date: int = Field(description="The timestamp of start date of the tournament.")
