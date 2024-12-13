


class Figure:

    def __init__(self, wight, height, length):
        self._wight = wight
        self._height = height
        self.__length = length

    @property
    def wight(self):
        return self._wight

    @wight.setter
    def wight(self, value):
        self._wight = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        return self.__length

    def area(self):
        return self.wight * self.height
    
    def volume(self):
        return self.area() * self.length




d = Figure(2, 3, 10)
d.length = 20
print(d.area())
print(d.volume())


