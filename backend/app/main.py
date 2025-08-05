from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator
from fastapi import Depends, FastAPI
import uvicorn
from sqlmodel import text
from core.database import engine, get_session, AsyncSession


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None, Any]:
    yield
    await engine.dispose()


app = FastAPI(lifespan=lifespan)


# return information about mysql db
@app.get("/")
async def read_root(session: AsyncSession = Depends(get_session)):
    db_info = await session.exec(statement=text("SELECT DATABASE()"))
    db_metadata = await session.exec(statement=text("SELECT VERSION()"))

    return {
        "database": db_info.scalar(),
        "version": db_metadata.scalar(),
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
