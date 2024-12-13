def test_calculate_ground_shipping():
    calculator = ShippingCostCalculator()
    assert calculator.calculate("ground", 10) == 15.0

def test_calculate_air_shipping():
    calculator = ShippingCostCalculator()
    assert calculator.calculate("air", 10) == 30.0

def test_calculate_sea_shipping():
    calculator = ShippingCostCalculator()
    assert calculator.calculate("sea", 10) == 5.0