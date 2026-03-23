"""Simple tools to sort and summarize customer requests."""


def count_open_requests(requests):
    """Return the number of open requests."""
    return sum(1 for request in requests if request["status"] == "open")


def filter_urgent_requests(requests):
    """Return all requests with high priority."""
    return [request for request in requests if request["priority"] == "high"]


def classify_request(priority):
    """Classify a request as urgent or normal."""
    if priority == "high":
        return "urgent"
    else:
        return "normal"
