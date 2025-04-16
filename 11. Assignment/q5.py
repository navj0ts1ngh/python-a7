def calculate_interest(principal: float, roi: float, time: float) -> float:
    return (principal * roi * time) / 100


print(calculate_interest(10000, 7, 1))
