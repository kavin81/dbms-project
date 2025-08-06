# types
from datetime import datetime, timezone
from core.database import AsyncSession

# database logic
from sqlmodel import select
from models import BlacklistToken


async def cleanup_blacklisted_tokens(db: AsyncSession) -> None:
    now = datetime.now(timezone.utc)
    stmt = select(BlacklistToken).where(BlacklistToken.expires_at < now)
    await db.delete(stmt)
    await db.commit()
