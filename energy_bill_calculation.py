"""Tool to calculate and analyze energy costs."""

def calculate_energy_cost(consumption_kwh, price_per_kwh):
"""Return total energy cost."""
if consumption_kwh < 0 or price_per_kwh < 0:
raise ValueError("Inputs must be non-negative")
return consumption_kwh * price_per_kwh


def estimate_annual_cost(monthly_consumptions, price_per_kwh):
"""Return annual energy cost based on monthly values."""
total = sum(monthly_consumptions)
return total * price_per_kwh


def detect_high_usage_months(monthly_consumptions, threshold_kwh):
"""Return values above a usage threshold."""
return [value for value in monthly_consumptions if value > threshold_kwh]


def average_monthly_consumption(monthly_consumptions):
"""Return average monthly consumption."""
return sum(monthly_consumptions) / len(monthly_consumptions)

def classify_consumption(consumption_kwh, threshold_kwh):
"""Classify consumption as too high or normal."""
if consumption_kwh > threshold_kwh:
return "too high"
else: return "normal"
