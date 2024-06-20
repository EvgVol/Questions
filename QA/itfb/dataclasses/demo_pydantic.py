from typing_extensions import Annotated

from datetime import datetime
from pydantic import BaseModel, Field, StringConstraints



class Point(BaseModel):
    x: int
    y: int


class Person(BaseModel):
    age: int
    name: str
    email: str | None = None

    class Config:
        extra = "allow"


class Food(BaseModel):
    name: Annotated[str, StringConstraints(min_length=3, max_length=1000)]
    price: Annotated[int, Field(ge=0, le=1000)]
    created_at: datetime

    class Config:
        validate_assignment = True


def main():
    # p1 = Point(x=1, y=2)
    # p2 = Point(x=3, y=4)
    # print(p1)
    # print(p2)
    # print([p1, p2])
    person = Person(name="John", age=48, a="123")
    person.email = "john@example.com"
    print(person)
    food_1 = Food(name="Milk", price=50, created_at="2020-01-01T00:12:12")
    food_2 = Food(name="Milk", price=23, created_at=1577823132.0)
    print(food_1.created_at.timestamp())
    # print(food_2.created_at)
    food_1.name = "M"
    print(food_1)
    


if __name__ == "__main__":
    main()
