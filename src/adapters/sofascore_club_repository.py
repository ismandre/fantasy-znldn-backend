from domain.models.club import ClubDetails
from domain.ports.club_repository import ClubRepository


class SofascoreClubRepository(ClubRepository):
    async def get_all(self) -> list[ClubDetails]:
        return [ClubDetails(id="some_id", name="FC Test Club")]