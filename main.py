import asyncio
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path
from app.api import router
from app.bot import start_bot

app = FastAPI()
app.include_router(router)

BASE_DIR = Path(__file__).resolve().parent


@app.on_event("startup")
async def on_startup():
    asyncio.create_task(start_bot())


@app.get("/")
async def read_root():
    return {"message": "Welcome to the API!"}


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    favicon_path = BASE_DIR / "favicon.ico"
    if not favicon_path.exists():
        return {"error": "favicon.ico не найден"}
    return FileResponse(favicon_path)
