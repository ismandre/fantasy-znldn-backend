from dataclasses import dataclass
from enum import StrEnum

from domain.models.player import Player
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


@dataclass
class IncidentType(StrEnum):
    PERIOD = "period"
    SUBSTITUTION = "substitution"
    GOAL = "goal"
    CARD = "card"


@dataclass
class EventIncident:
    id: int
    time: int
    incident_type: IncidentType


@dataclass
class PeriodType(StrEnum):
    HALF_TIME = "HT"
    FULL_TIME = "FT"


@dataclass
class PeriodEventIncident(EventIncident):
    text: PeriodType
    home_score: int
    away_score: int


@dataclass
class SubstitutionEventIncident(EventIncident):
    player_in: Player
    player_out: Player


@dataclass
class GoalEventIncident(EventIncident):
    home_score: int
    away_score: int
    player: Player


@dataclass
class CardType(StrEnum):
    YELLOW = "yellow"
    YELLOW_RED = "yellowRed"
    RED = "red"


@dataclass
class CardEventIncident(EventIncident):
    player: Player
    card: CardType
