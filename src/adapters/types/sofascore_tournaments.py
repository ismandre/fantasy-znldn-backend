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
