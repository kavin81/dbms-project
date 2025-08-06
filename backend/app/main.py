# types
from typing import AsyncGenerator
from contextlib import asynccontextmanager

# web API imports
import uvicorn
from fastapi import FastAPI

# application logic
from core.database import dispose
from scheduler import start_scheduler, run_cleanup
from api import router


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator:
    # on_startup
    await run_cleanup()
    start_scheduler()
    yield
    # on_shutdown
    await dispose()


app = FastAPI(lifespan=lifespan)
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
