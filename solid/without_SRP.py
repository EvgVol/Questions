class UserManager:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def add_user(self, username, password):
        # Логика валидации пользователя
        if len(username) < 5:
            raise ValueError("Имя пользователя должно содержать более 5 символов")
        
        # Логика хеширования пароля
        hashed_password = self.hash_password(password)
        
        # Логика добавления пользователя в базу данных
        self.db_connection.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, hashed_password)
        )

    def hash_password(self, password):
        return hash(password)
