

class Date:
    def __init__(self, year: int, month: int, day: int) -> None:
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_date_string(cls, date_string: str):
        year, month, day = map(int, date_string.split("-"))
        return cls(year=year, month=month, day=day)

    @staticmethod
    def is_date_string(data_string: str):
        return data_string.count("-") == 2

    def __str__(self) -> str:
        return (f"{self.__class__.__name__}: "
                f"year = {self.year}, month = {self.month}, day = {self.day}")


if __name__ == "__main__":
    dt = Date(2000, 1, 1)
    print(dt)
    dt_2 = Date.from_date_string("2001-2-2")
    print(dt_2)
    print(Date.is_date_string("abs"))
    print(Date.is_date_string("2000-1-1"))