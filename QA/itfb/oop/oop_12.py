class User:
    def __init__(self, name) -> None:
        self.name = name
        self._password = None


class UserTwo:
    def __init__(self, name) -> None:
        self.name = name
        self.__password = None


if __name__ == "__main__":
    john = User(name="John")
    print(john.name)
    print(john._password)
    john._password = "test"
    print(john._password)
    sam = UserTwo(name="Sam")
    print(sam.name)
    print(sam.__dict__)
    print(sam._UserTwo__password)
    sam._UserTwo__password = "abs"
    print(sam._UserTwo__password)
