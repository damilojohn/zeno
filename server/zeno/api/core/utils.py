from datetime import datetime
import uuid


def current_time() -> datetime:
    return datetime.now(datetime.UTC)


def generate_uuid() -> uuid.UUID:
    return uuid.uuid4()
