import uvicorn
from fastapi import FastAPI

from config import Settings, get_settings
from routes import router

settings: Settings = get_settings()



def create_app(
) -> FastAPI:
    app = FastAPI(title="Basket Service")
    app.include_router(router)
    return app

app: FastAPI = create_app()



def main() -> None:

    uvicorn.run(
        "main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.API_RELOAD,
        proxy_headers=settings.API_PROXY_HEADERS
    )


if __name__ == "__main__":
    main()