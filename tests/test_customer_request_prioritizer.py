from customer_request_prioritizer import (classify_request, count_open_requests, filter_urgent_requests,)


REQUESTS = [
{"customer": "A", "status": "open", "priority": "high"},
{"customer": "B", "status": "closed", "priority": "low"},
{"customer": "C", "status": "open", "priority": "high"},
{"customer": "D", "status": "open", "priority": "medium"},
]


def test_count_open_requests():
    assert count_open_requests(REQUESTS) == 3


def test_filter_urgent_requests():
    result = filter_urgent_requests(REQUESTS)
    assert len(result) == 2


def test_classify_request():
    assert classify_request("high") == "urgent"
    assert classify_request("low") == "normal"
