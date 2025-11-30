from dataclasses import dataclass
from typing import Optional


@dataclass
class Tournament:
    id: int
    name: str
    has_rounds: Optional[bool] = None
    start_date: Optional[int] = None

@dataclass
class TournamentSeason:
    id: int
    name: str
    year: str