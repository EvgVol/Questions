def test_calculate_ground_shipping():
    """Проверка стоимости доставки наземным транспортом."""
    calculator = ShippingCostCalculator(GroundShipping())
    assert calculator.calculate(10) == 15.0


def test_calculate_air_shipping():
    """Проверка стоимости доставки воздушным транспортом."""
    calculator = ShippingCostCalculator(AirShipping())
    assert calculator.calculate(10) == 30.0


def test_calculate_sea_shipping():
    """Проверка стоимости доставки морем."""
    calculator = ShippingCostCalculator(SeaShipping())
    assert calculator.calculate(10) == 5.0
