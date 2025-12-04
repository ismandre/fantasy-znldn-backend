from domain.models.club import ClubDetails
from domain.ports.club_repository import ClubRepository


class ClubService:
    def __init__(self, club_repository: ClubRepository):
        self.club_repository = club_repository

    async def get_all_clubs(self) -> list[ClubDetails]:
        return await self.club_repository.get_all()
