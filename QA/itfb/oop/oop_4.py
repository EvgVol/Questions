class Shape:
    def get_area(self):
        print('no shape')


class Rectangle(Shape):

    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: a = {self.a}, b = {self.b}"

    def get_area(self):
        return self.a * self.b


class Square(Rectangle):
    def __init__(self, a) -> None:
        self.a = a

    @property
    def b(self):
        return self.a

    @b.setter
    def b(self, value):
        self.a = value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: a = {self.a}"

    def get_area(self):
        return self.a * self.a


if __name__ == "__main__":
    rect_1 = Rectangle(6, 4)
    rect_1.b = 7
    sq_1 = Square(6)
    sq_1.b = 7
    print(rect_1.get_area())
    print(sq_1.get_area())

# print(rect_1)
# print([rect_1])
# print(Rectangle.mro())
# print(rect_1.a)
# print(rect_1.b)

