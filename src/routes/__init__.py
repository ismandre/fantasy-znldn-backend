from fastapi import APIRouter

from routes.dummy.dummy import router as dummy_router

router = APIRouter()


router.include_router(dummy_router)

__all__ = ["router"]