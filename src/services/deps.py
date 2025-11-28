from typing import Annotated

from fastapi import Depends

from adapters.sofascore_club_repository import SofascoreClubRepository
from domain.ports.club_repository import ClubRepository
from services.clubs import ClubService

def get_club_repository() -> ClubRepository:
    return SofascoreClubRepository()



def get_club_service(
        club_repo: Annotated[ClubRepository, Depends(get_club_repository)]
) -> ClubService:
    return ClubService(club_repo)