from datetime import date, datetime

DATE_FORMAT = "%m/%d/%Y"

def parse_deadline(text):
    """Convert date text to date object. Handles varying zero padding."""
    if not text or not isinstance(text, str):
        return None
    text = text.strip()
    try:
        return datetime.strptime(text, DATE_FORMAT).date()
    except ValueError:
        parts = text.split("/")
        if len(parts) == 3:
            try:
                return date(int(parts[2]), int(parts[0]), int(parts[1]))
            except ValueError:
                return None
        return None