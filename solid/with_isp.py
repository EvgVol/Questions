class LoginPage:
    def login(self, username, password):
        """Ввод имени пользователя и пароля на странице логина."""
        ...

class DashboardPage:
    def navigate_to_dashboard(self):
        """Навигация на дашборд."""
        ...

    def open_settings(self):
        """Открытие страницы настроек на дашборде."""
        ...

    def logout(self):
        """Выход из приложения."""
        ...