from pydantic import BaseModel, ConfigDict


class TournamentRoundSerializer(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    round: int


class TournamentRoundsSerializer(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    current_round: TournamentRoundSerializer
    rounds: list[TournamentRoundSerializer]