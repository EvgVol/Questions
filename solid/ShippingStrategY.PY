from abc import ABC, abstractmethod

class ShippingStrategy(ABC):
    @abstractmethod
    def calculate(self, weight):
        pass

class GroundShipping(ShippingStrategy):
    def calculate(self, weight):
        return weight * 1.5

class AirShipping(ShippingStrategy):
    def calculate(self, weight):
        return weight * 3.0

class SeaShipping(ShippingStrategy):
    def calculate(self, weight):
        return weight * 0.5

class ShippingCostCalculator:
    def __init__(self, strategy: ShippingStrategy):
        self.strategy = strategy

    def calculate(self, weight):
        return self.strategy.calculate(weight)


