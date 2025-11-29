from typing import TypedDict


class UniqueTournament(TypedDict):
    id: int
    name: str
    hasRounds: bool
    startDateTimestamp: int


class UniqueTournamentResponse(TypedDict):
    uniqueTournament: UniqueTournament
