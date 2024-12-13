def test_user_validation():
    """Проверка валидации для короткого имени пользователя."""
    validator = UserValidator()
    with pytest.raises(ValueError):
        validator.validate("john")


def test_password_hashing():
    """Проверка хеширования пароля."""
    hasher = PasswordHasher()
    hashed_password = hasher.hash_password("password123")
    assert hashed_password == hasher.hash_password("password123")


def test_user_repository():
    """Проверка добавления нового пользователя в базу данных."""
    db_connection = Database()
    repository = UserRepository(db_connection)
    repository.add_user("john_doe", "hashed_password")
    assert db_connection.query("SELECT * FROM users WHERE username = 'john_doe'") is not None

