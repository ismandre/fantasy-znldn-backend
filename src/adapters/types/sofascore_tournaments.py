from typing import TypedDict


class UniqueTournament(TypedDict):
    id: int
    name: str
    hasRounds: bool
    startDateTimestamp: int


class TournamentSeasonResponse(TypedDict):
    id: int
    name: str
    year: str


class UniqueTournamentResponse(TypedDict):
    uniqueTournament: UniqueTournament


class UniqueTournamentSeasonsResponse(TypedDict):
    seasons: list[TournamentSeasonResponse]


class TournamentRoundResponse(TypedDict):
    round: int


class UniqueTournamentSeasonRoundsResponse(TypedDict):
    currentRound: TournamentRoundResponse
    rounds: list[TournamentRoundResponse]


class RoundEventTeam(TypedDict):
    id: int
    name: str


class RoundEventScore(TypedDict):
    current: int
    display: int
    period1: int
    period2: int
    normaltime: int


class RoundEventStatus(TypedDict):
    code: int
    description: str
    type: str


class RoundEventInfo(TypedDict):
    round: int


class RoundEventTournament(TypedDict):
    id: int
    name: str


class RoundEventSeason(TypedDict):
    id: int
    name: str
    year: str


class RoundEvent(TypedDict):
    tournament: RoundEventTournament
    season: RoundEventSeason
    homeTeam: RoundEventTeam
    awayTeam: RoundEventTeam
    homeScore: RoundEventScore
    awayScore: RoundEventScore
    startTimestamp: int
    status: RoundEventStatus
    roundInfo: RoundEventInfo


class UniqueTournamentSeasonEventsRoundResponse(TypedDict):
    events: list[RoundEvent]
