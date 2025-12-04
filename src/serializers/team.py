from pydantic import BaseModel, ConfigDict, Field


class TeamSerializer(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str = Field(description="The name of the club.", examples=["FC Test Club"])
