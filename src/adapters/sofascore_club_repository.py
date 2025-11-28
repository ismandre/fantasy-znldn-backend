from domain.models.club import ClubDetails
from domain.ports.club_repository import ClubRepository
from domain.ports.http_client import HttpClient


class SofascoreClubRepository(ClubRepository):

    def __init__(self, http_client: HttpClient):
        self.http_client = http_client

    async def get_all(self) -> list[ClubDetails]:
        response = await self.http_client.get("https://api.sofascore.com/api/v1/event/14526955/lineups")
        from pprint import pprint
        pprint(response)
        return []