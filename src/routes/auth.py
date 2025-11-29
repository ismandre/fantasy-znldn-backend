from fastapi import APIRouter, status

router = APIRouter(prefix="/auth", tags=["auth"])



@router.get(
    path="/login",
    name="Login",
    response_model=None,
    status_code=status.HTTP_200_OK
)
async def login():
    return {"message": "Login"}