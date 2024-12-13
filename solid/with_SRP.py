class UserValidator:
    def validate(self, username):
        if len(username) < 5:
            raise ValueError("Имя пользователя должно содержать более 5 символов")

class PasswordHasher:
    def hash_password(self, password):
        return hash(password)

class UserRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def add_user(self, username, hashed_password):
        self.db_connection.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, hashed_password)
        )

class UserManager:
    def __init__(self, validator, hasher, repository):
        self.validator = validator
        self.hasher = hasher
        self.repository = repository

    def add_user(self, username, password):
        self.validator.validate(username)
        hashed_password = self.hasher.hash_password(password)
        self.repository.add_user(username, hashed_password)
        
