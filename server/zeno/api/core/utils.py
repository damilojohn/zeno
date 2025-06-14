from datetime import datetime, timezone
import uuid
import structlog

LOG = structlog.stdlib.get_logger()


def current_time() -> datetime:
    return datetime.now(timezone.utc)


def generate_uuid() -> uuid.UUID:
    return uuid.uuid4()
