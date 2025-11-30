from dataclasses import dataclass



@dataclass
class Score:
    current: int
    display: int
    period1: int
    period2: int
    normaltime: int