from energy_bill_calculation import (average_monthly_consumption, calculate_energy_cost, classify_consumption, detect_high_usage_months,estimate_annual_cost,)


MONTHLY_CONSUMPTIONS = [300, 300, 300, 300]


def test_calculate_energy_cost():
assert calculate_energy_cost(100, 0.30) == 30.0

def test_estimate_annual_cost():
assert estimate_annual_cost([100, 200, 300], 0.25) == 150.0

def test_detect_high_usage_months():
result = detect_high_usage_months(MONTHLY_CONSUMPTIONS, 300)
assert result == [310, 400, 360]

def test_average_monthly_consumption():
result = average_monthly_consumption(MONTHLY_CONSUMPTIONS)
assert result == 300

def test_classify_consumption():
assert classify_consumption(400, 300) == "too high"
assert classify_consumption(200, 300) == "normal"
