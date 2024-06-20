from collections import namedtuple


Point = namedtuple(typename="Point", field_names=['x', 'y'])


def get_point():
    return Point(42, 52)


def main():
    point1 = get_point()
    point2 = get_point()

    print(point1)
    print(point2)

    print(point1 == point2)

    print("point1.x =", point1.x)
    print("point1.y =", point1.y)


if __name__ == "__main__":
    main()
