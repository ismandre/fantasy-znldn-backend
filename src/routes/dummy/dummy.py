from fastapi import APIRouter

router = APIRouter(prefix="/dummy", tags=["dummy"])

@router.get("/")
async def dummy():
    return {"message": "Hello World"}