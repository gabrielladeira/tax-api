from datetime import datetime, timezone


class DateTimes:
    @classmethod
    def now(cls) -> datetime:
        return datetime.now(timezone.utc)
