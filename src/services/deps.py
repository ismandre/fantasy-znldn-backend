from typing import Annotated

from fastapi import Depends

from adapters.sofascore_client import SofascoreClient
from adapters.sofascore_club_repository import SofascoreClubRepository
from domain.ports.club_repository import ClubRepository
from domain.ports.http_client import HttpClient
from services.clubs import ClubService


def get_http_client() -> HttpClient:
    return SofascoreClient()

def get_club_repository(
        http_client: Annotated[HttpClient, Depends(get_http_client)]
) -> ClubRepository:
    return SofascoreClubRepository(http_client)



def get_club_service(
        club_repo: Annotated[ClubRepository, Depends(get_club_repository)]
) -> ClubService:
    return ClubService(club_repo)