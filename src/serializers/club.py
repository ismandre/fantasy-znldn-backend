from pydantic import BaseModel, ConfigDict, Field

class ClubSerializer(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    name: str = Field(description="The name of the club.", example="FC Test Club")