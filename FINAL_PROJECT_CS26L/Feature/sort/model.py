from datetime import datetime, date

DATE_FORMAT = "%m/%d/%Y"
PRIORITY_ORDER = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}

class SortRule:
    """Model defining rules and keys for task sorting."""

    @staticmethod
    def deadline_key(task):
        """Parses deadline string for chronological comparison."""
        raw_date = task.get("Deadline", "")
        if not raw_date or not isinstance(raw_date, str):
            return date.max

        raw_date = raw_date.strip()
        try:
            return datetime.strptime(raw_date, DATE_FORMAT).date()
        except ValueError:
            parts = raw_date.split("/")
            if len(parts) == 3:
                try:
                    return date(int(parts[2]), int(parts[0]), int(parts[1]))
                except ValueError:
                    return date.max
            return date.max

    @staticmethod
    def priority_key(task):
        """Maps priority strings to numeric values for ordering."""
        return PRIORITY_ORDER.get(task.get("Priority"), 99)