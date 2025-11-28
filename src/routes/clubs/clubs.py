from typing import Annotated

from fastapi import APIRouter, Depends

from services.clubs import ClubService
from services.deps import get_club_service

from serializers.club import ClubSerializer

router = APIRouter(prefix="/clubs", tags=["clubs"])


@router.get("/")
async def clubs(
        service: Annotated[ClubService, Depends(get_club_service)]
) -> list[ClubSerializer]:
    clubs = await service.get_all_clubs()
    return [ClubSerializer.model_validate(club) for club in clubs]