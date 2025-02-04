from fastapi import FastAPI
from .api import router as api_router
from .log import start_bot

app = FastAPI()

app.include_router(api_router)

if __name__ == "__main__":
    start_bot()
