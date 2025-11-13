from celery import Celery
import os

# Redis connection URL
redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")

# Create Celery app
celery = Celery(
    "backend",
    broker=redis_url,
    backend=redis_url,
    include=["tasks"],  # 👈 ensures tasks.py is auto-imported
)

# Optional: Celery beat schedule (runs weekly)
celery.conf.beat_schedule = {
    "weekly-report": {
        "task": "tasks.send_weekly_report",
        "schedule": 604800.0,  # 7 days in seconds
        "args": (),
    },
}

# Timezone
celery.conf.timezone = "UTC"
celery.conf.enable_utc = True
