class ShippingCostCalculator:
    def calculate(self, shipping_type, weight):
        if shipping_type == "ground":
            return weight * 1.5
        elif shipping_type == "air":
            return weight * 3.0
        elif shipping_type == "sea":
            return weight * 0.5
        else:
            raise ValueError("Неизвестный тип доставки")