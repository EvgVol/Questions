class Car:
    def __init__(self, doors, sound) -> None:
        self.doors = doors
        self.sound = sound

    def make_sound(self):
        print('Car with', self.doors, "doors does", self.sound)


class RaceCar(Car):
    ...


class Ship:
    def __init__(self, cabins, sound) -> None:
        self.cabins = cabins
        self.sound = sound

    def make_sound(self):
        print('Ship with', self.cabins, "cabins does", self.sound)

class Yach(Ship):
    ...


class Amphibian(Car, Ship):
    def __init__(self, doors, cabins, sound, color) -> None:
        Car.__init__(self, doors, sound)
        Ship.__init__(self, cabins, sound)
        self.color = color

    def make_sound(self):
        print('Amphibian with', self.doors,
              "doors and", self.cabins,
              "cabins and color", self.color,
              "make sound", self.sound)


if __name__ == "__main__":
    amp = Amphibian(doors=4, sound="beep", cabins=3, color="green")
    print(amp.doors)
    print(amp.sound)
    print(amp.cabins)
    print(amp.color)
    amp.make_sound()