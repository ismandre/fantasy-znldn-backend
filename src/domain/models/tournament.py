from dataclasses import dataclass


@dataclass
class Tournament:
    id: int
    name: str
    has_rounds: bool
    start_date: int