from pydantic import BaseModel, ConfigDict

from serializers.round import TournamentRoundSerializer
from serializers.score import ScoreSerializer
from serializers.season import SeasonSerializer
from serializers.team import TeamSerializer
from serializers.tournament import TournamentSerializer


class EventStatusSerializer(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    description: str
    type: str


class TournamentRoundEventSerializer(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    tournament: TournamentSerializer
    season: SeasonSerializer
    home_team: TeamSerializer
    away_team: TeamSerializer
    home_score: ScoreSerializer
    away_score: ScoreSerializer
    start_timestamp: int
    status: EventStatusSerializer
    round_info: TournamentRoundSerializer
