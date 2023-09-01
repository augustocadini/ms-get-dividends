from dataclasses import dataclass, field


def is_iso_date_format(value):
    try:
        datetime.fromisoformat(value)
        return True
    except ValueError:
        return False


@dataclass
class DividendsGetRequest:
    ticker: str
    startDate: str = field(metadata={'validate': is_iso_date_format})
    endDate: str = field(metadata={'validate': is_iso_date_format})
