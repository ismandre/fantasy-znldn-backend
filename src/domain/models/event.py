from dataclasses import dataclass

from domain.models.round import TournamentRound
from domain.models.score import Score
from domain.models.team import Team
from domain.models.tournament import Tournament, TournamentSeason


@dataclass
class EventStatus:
    description: str
    type: str

@dataclass
class Event:
    tournament: Tournament
    season: TournamentSeason
    home_team: Team
    away_team: Team
    home_score: Score
    away_score: Score
    start_timestamp: int
    status: EventStatus
    round_info: TournamentRound
