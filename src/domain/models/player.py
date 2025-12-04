from dataclasses import dataclass
from enum import StrEnum


class PlayerPosition(StrEnum):
    GOALKEEPER = "G"
    DEFENDER = "D"
    MIDFIELDER = "M"
    FORWARD = "F"


@dataclass
class Player:
    id: int
    position: PlayerPosition
    name: str
