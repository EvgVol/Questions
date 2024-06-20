from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Personal:
    age: int
    weight: int


def main():
    p1 = Point(3, 5)
    p2 = Point(x=4, y=4)
    print(p1)
    print(p2)
    person = Personal(age=3, weight=5)
    print(person)
    print("p1 == person", p1 == person)
    person2 = Personal(age=3, weight=5)
    person2.age = 42
    person2.weight = 55
    print(person)
    print(person2)

    # person.email = "email@example.com"
    # print(person.email)


if __name__ == "__main__":
    main()
