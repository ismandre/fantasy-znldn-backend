from fastapi import APIRouter

from routes.clubs.clubs import router as clubs_router
from routes.dummy.dummy import router as dummy_router
from routes.tournament.tournament import router as tournament_router

router = APIRouter()


router.include_router(clubs_router)
router.include_router(dummy_router)
router.include_router(tournament_router)

__all__ = ["router"]