from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

class TournamentSerializer(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., description="The ID of the tournament.")
    name: str = Field(description="The name of the tournament.")
    has_rounds: Optional[bool] = Field(description="Does the tournament have rounds?")
    start_date: Optional[int] = Field(description="The timestamp of start date of the tournament.")
