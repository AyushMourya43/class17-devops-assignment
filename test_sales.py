from sales import calculate_revenue


def test_revenue_positive():
    assert calculate_revenue(100, 5) == 500


def test_revenue_zero():
    assert calculate_revenue(100, 0) == 100
