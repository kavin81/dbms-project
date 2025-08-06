from fastapi import APIRouter, Depends
from core.database import get_session, AsyncSession
from sqlmodel import text

# import api routers & `include_router` them here

router = APIRouter(
    prefix="/api/v1",
    tags=["api"],
)


# testing endpoint to check database connection and version
@router.get("/")
async def read_root(session: AsyncSession = Depends(get_session)):
    db_info = await session.exec(statement=text("SELECT DATABASE()"))  # pyright: ignore[reportArgumentType, reportCallIssue]
    db_metadata = await session.exec(statement=text("SELECT VERSION()"))  # pyright: ignore[reportArgumentType, reportCallIssue]

    return {
        "database": db_info.scalar(),
        "version": db_metadata.scalar(),
    }


__all__: list[str] = ["router"]
