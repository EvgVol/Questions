# Pydantic


Pydantic — это библиотека для валидации данных и управления настройками с использованием аннотаций типов Python. Она позволяет определять структуры данных, которые автоматически проверяются на соответствие типам при создании экземпляров. Это особенно полезно для работы с JSON, конфигурационными файлами и веб-запросами.

Вот основные возможности Pydantic:
- **Валидация**: Автоматическая проверка входных данных на соответствие предопределенным типам.
- **Преобразование типов**: Автоматическое преобразование входных данных в нужные типы.
- **Экспорт данных**: Преобразование моделей в словари, JSON и другие форматы.
- **Документация**: Генерация схемы модели, которая может быть использована для документации API.

### Определения модели и валидации данных

```python
from pydantic import BaseModel, ValidationError

# Определение модели
class User(BaseModel):
    id: int
    name: str
    age: int
    signup_ts: Optional[datetime] = None

# Создание экземпляра модели с валидацией
try:
    user = User(
        id=123,
        name='John Doe',
        age='23',  # Pydantic автоматически преобразует строку в число
        signup_ts='2021-01-01T12:34'
    )
    print(user)
except ValidationError as e:
    print(e.json())

```

В этом примере мы определяем класс `User` с использованием Pydantic. Каждое поле класса аннотировано типом данных, и Pydantic автоматически валидирует и преобразует данные при создании экземпляра `User`. Если данные не соответствуют ожидаемым типам, Pydantic вызовет исключение `ValidationError`.

---

### Валидация списка объектов и использование пользовательских валидаторов.

```python
from pydantic import BaseModel, ValidationError, validator
from typing import List, Optional
from datetime import datetime

# Определение модели пользователя
class User(BaseModel):
    id: int
    name: str
    age: Optional[int] = None
    signup_ts: Optional[datetime] = None

    # Пользовательский валидатор для поля 'age'
    @validator('age')
    def check_age(cls, value):
        if value is not None and value < 18:
            raise ValueError('Возраст должен быть не менее 18 лет')
        return value

# Определение модели для списка пользователей
class UserList(BaseModel):
    users: List[User]

# Валидация списка пользователей
try:
    users_data = [
        {'id': 1, 'name': 'Alice', 'age': 30},
        {'id': 2, 'name': 'Bob', 'age': 17},  # Этот пользователь вызовет ошибку валидации
        {'id': 3, 'name': 'Charlie', 'age': 25}
    ]
    users_list = UserList(users=users_data)
    print(users_list)
except ValidationError as e:
    print(e.json())

```

В этом примере мы определяем класс `User` с пользовательским валидатором для поля `age`, который проверяет, что возраст пользователя не меньше 18 лет. Затем мы создаем класс `UserList`, который представляет собой список пользователей. При попытке создать экземпляр `UserList` с данными, Pydantic валидирует каждый объект в списке. Если какие-либо данные не соответствуют ожиданиям, будет вызвано исключение `ValidationError`.

Это позволяет легко управлять сложными структурами данных и обеспечивает дополнительный уровень безопасности при работе с входными данными. Pydantic особенно полезен в веб-разработке и при создании API, где необходимо гарантировать, что входные данные соответствуют определенным требованиям.

### Использование моделей для вложенных структур данных

```python
from pydantic import BaseModel, ValidationError
from typing import List, Optional

# Определение модели адреса
class Address(BaseModel):
    street: str
    city: str
    country: str

# Определение модели пользователя с вложенной моделью адреса
class User(BaseModel):
    id: int
    name: str
    age: Optional[int] = None
    address: Address  # Вложенная модель

# Создание экземпляра модели с валидацией
try:
    user = User(
        id=123,
        name='John Doe',
        age=30,
        address={
            'street': '123 Main St',
            'city': 'Anytown',
            'country': 'Anycountry'
        }
    )
    print(user)
except ValidationError as e:
    print(e.json())
```

В этом примере `Address` является отдельной моделью, которая затем используется в качестве типа для поля `address` в модели `User`. Это позволяет Pydantic валидировать адрес как часть процесса создания пользователя. Если данные адреса не соответствуют ожидаемым типам, Pydantic вызовет исключение `ValidationError`.

Такой подход упрощает управление сложными JSON-структурами и обеспечивает строгую типизацию и валидацию на всех уровнях вложенности.