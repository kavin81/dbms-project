from apscheduler.schedulers.asyncio import AsyncIOScheduler
from scheduler.tasks import run_cleanup

scheduler = AsyncIOScheduler()


def start_scheduler():
    scheduler.add_job(
        run_cleanup,
        trigger="interval",
        minutes=30,
        id="cleanup_blacklisted_tokens",
        replace_existing=True,
    )
    scheduler.start()

