from core.database import get_session
from core.auth import cleanup_blacklisted_tokens


async def run_cleanup():
    session_gen = get_session()
    session = await anext(session_gen)
    try:
        await cleanup_blacklisted_tokens(session)
    finally:
        await session_gen.aclose()

