
class Personal:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


def get_personal() -> dict:
    return {
        "name": "John",
        "age": 42
    }


def main():
    pers_1 = get_personal()
    print(pers_1)
    print(pers_1["name"])
    pers_2 = get_personal()
    pers_2["name"] = "Sam"
    pers_2["email"] = "email@example.com"
    print(pers_2)
    print(pers_2["email"])
    # print(pers_2["email"])


if __name__ == "__main__":
    main()
