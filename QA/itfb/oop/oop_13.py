class User:

    def __init__(self, name) -> None:
        self.name = name
        self.__password = None

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = hash(value)



if __name__ == "__main__":
    john = User(name="John")
    john.password = "abs"
    print(john.name)
    print(john.password)