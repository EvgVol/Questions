# print(Exception)
# print(type(Exception))
# print(Exception.mro())
# print(ValueError)
# print(ValueError.mro())
# print(ZeroDivisionError)
# print(ZeroDivisionError.mro())


class MyError(Exception):
    ...

# print(MyError)
# print(MyError.mro())


class DBException(Exception):
    ...


class NotFoundError(DBException):
    ...


class UserNotFound(NotFoundError):
    ...


class ArticleNotFound(NotFoundError):
    ...


if __name__ == "__main__":
    print(NotFoundError.mro())
    print(UserNotFound.mro())
    print(ArticleNotFound.mro())