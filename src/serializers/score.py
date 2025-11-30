from pydantic import BaseModel, ConfigDict, Field


class ScoreSerializer(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    current: int = Field(..., description="The current score.")
    display: int = Field(..., description="The score to display.")
    period1: int = Field(..., description="The score for the first period.")
    period2: int = Field(..., description="The score for the second period.")
    normaltime: int = Field(..., description="The score for the normal time.")