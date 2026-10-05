class SearchCriteria:
    """Model representing search parameters."""

    def __init__(self, keyword="", status="All", priority="All", scope=None):
        self.keyword = keyword.strip().lower()
        self.status = status
        self.priority = priority
        self.scope = scope