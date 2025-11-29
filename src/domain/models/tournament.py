from dataclasses import dataclass


@dataclass
class Tournament:
    id: int
    name: str
    has_rounds: bool
    start_date: int

@dataclass
class TournamentSeason:
    id: int
    name: str
    year: str