# Основы Python

Python – по сути своей словари, обернутые тоннами синтаксического сахара.
– `Лало Мартинс`, один из первых цифровых номадов и питонистов


## **Class**

Класс в Python — это шаблон для создания объектов. Объекты класса содержат данные и функции, которые работают с этими данными.

**Пример**:
```python
class Автомобиль:
    def __init__(self, марка, модель):
        self.марка = марка
        self.модель = модель

    def отобразить_информацию(self):
        print(f"Марка автомобиля: {self.марка}, Модель: {self.модель}")
```


## **Классметод (Class Method)**:
Метод класса привязан к самому классу, а не к экземпляру класса. Он может изменять состояние класса, которое будет применяться ко всем экземплярам класса. Они определяются внутри класса и требуют декоратора `@classmethod`. Первым аргументом классметода всегда является ссылка на сам класс, обычно обозначаемая как `cls`.

Классметоды могут быть использованы для следующих целей:
- Создание экземпляров класса с использованием различных параметров, отличных от тех, что предусмотрены в конструкторе `__init__`.
- Определение функций, которые логически связаны с классом, но не требуют создания экземпляра класса для выполнения.

**Пример классметода**:
```python
class Автомобиль:
    количество_автомобилей = 0

    def __init__(self, марка, модель):
        self.марка = марка
        self.модель = модель
        Автомобиль.количество_автомобилей += 1

    @classmethod
    def общее_количество_автомобилей(cls):
        return cls.количество_автомобилей
```

В этом примере `общее_количество_автомобилей` является классметодом, который возвращает значение статической переменной `количество_автомобилей`, принадлежащей классу `Автомобиль`. Этот метод может быть вызван напрямую через класс, без необходимости создания экземпляра:

```python
print(Автомобиль.общее_количество_автомобилей())  # Выведет количество созданных автомобилей
```

Классметоды часто используются для реализации фабричных методов, которые создают объекты на основе различных параметров:

```python
class Автомобиль:
    def __init__(self, марка, модель):
        self.марка = марка
        self.модель = модель

    @classmethod
    def от_вин(cls, вин):
        марка = получить_марку_из_вин(вин)  # Предположим, что эта функция определена где-то еще
        модель = получить_модель_из_вин(вин)  # И эта функция тоже
        return cls(марка, модель)
```

Здесь `от_вин` — это классметод, который позволяет создать экземпляр `Автомобиль`, используя VIN-код для определения марки и модели автомобиля.

## **Статикметод (Static Method)**:

Статические методы в Python — это методы, которые можно вызывать без создания экземпляра класса. Они не имеют доступа к экземпляру (`self`) или классу (`cls`), с которыми они связаны. Статические методы определяются внутри класса и используют декоратор `@staticmethod`.

Статические методы полезны, когда вам нужно выполнить какое-то действие, которое связано с классом, но не требует доступа к его экземплярам или самому классу. Они часто используются для группировки утилитных функций в классе.

**Пример статического метода**:
```python
class Автомобиль:
    @staticmethod
    def проверить_валидность_вин(вин):
        return len(вин) == 17 и вин.isdigit()

# Вызов статического метода
print(Автомобиль.проверить_валидность_вин('12345678901234567'))  # Выведет True или False
```

В этом примере `проверить_валидность_вин` является статическим методом, который проверяет, соответствует ли VIN-код определенным критериям (в данном случае длине и состоит ли он только из цифр).

Статические методы могут быть вызваны напрямую через класс, как показано в примере выше, и они не требуют создания экземпляра класса для их использования. Это делает их похожими на обычные функции, но с тем отличием, что они логически связаны с классом, в котором они определены.

## **Проперти (Property)**:
Свойство в Python позволяет использовать методы класса как атрибуты, обеспечивая при этом дополнительную логику, такую как проверка валидности данных.

**Пример**:
```python
class Автомобиль:
    def __init__(self, марка):
        self._марка = марка

    @property
    def марка(self):
        return self._марка

    @марка.setter
    def марка(self, значение):
        if значение != "":
            self._марка = значение
        else:
            raise ValueError("Марка не может быть пустой")
```

Декоратор `@property` в Python используется для создания свойств в классе. Свойства позволяют классам иметь атрибуты, доступ к которым контролируется методами класса, что делает их похожими на геттеры и сеттеры в других языках программирования.

С помощью `@property` можно определить метод, который будет доступен как атрибут только для чтения. Если вы хотите разрешить изменение значения свойства, вы можете определить сеттер с тем же именем, используя декоратор `@<property_name>.setter`.

**Пример использования `@property`**:
```python
class Автомобиль:
    def __init__(self, марка, модель):
        self._марка = марка
        self._модель = модель

    @property
    def марка(self):
        return self._марка

    @марка.setter
    def марка(self, значение):
        self._марка = значение

    @property
    def модель(self):
        return self._модель

# Создание объекта и использование свойств
авто = Автомобиль('Toyota', 'Corolla')
print(авто.марка)  # Выведет 'Toyota'
авто.марка = 'Honda'  # Изменит марку автомобиля на 'Honda'
print(авто.марка)  # Выведет 'Honda'
```

В этом примере `марка` и `модель` являются свойствами класса `Автомобиль`. Метод `марка` определен как свойство с помощью декоратора `@property`, что позволяет получать значение марки автомобиля. С помощью `@марка.setter` определен сеттер, который позволяет изменять марку автомобиля.

Свойства полезны для инкапсуляции данных, предоставления удобного интерфейса для доступа к атрибутам класса и добавления дополнительной логики при получении или установке значения атрибута.

В контексте автоматизации тестирования веб-приложений, `@property` часто используется в паттерне Page Factory для создания свойств, которые представляют элементы на веб-страницах. 

__Page Factory__ — это способ оптимизации процесса автоматизации, который позволяет легко и удобно находить элементы на странице и работать с ними.

Использование `@property` в Page Factory обеспечивает лучшую читаемость кода и позволяет инкапсулировать логику поиска элементов, делая тесты более устойчивыми к изменениям в структуре веб-страницы.

**Пример использования `@property` в Page Factory**:
```python
from selenium.webdriver.support.page_object import PageObject
from selenium.webdriver.common.by import By

class LoginPage(PageObject):
    _username_locator = (By.ID, 'username')
    _password_locator = (By.ID, 'password')
    _login_button_locator = (By.ID, 'loginButton')

    @property
    def username_field(self):
        return self.find_element(*self._username_locator)

    @property
    def password_field(self):
        return self.find_element(*self._password_locator)

    @property
    def login_button(self):
        return self.find_element(*self._login_button_locator)

    def login(self, username, password):
        self.username_field.send_keys(username)
        self.password_field.send_keys(password)
        self.login_button.click()
```

В этом примере `LoginPage` представляет страницу входа в систему. С помощью `@property` создаются свойства `username_field`, `password_field` и `login_button`, которые возвращают элементы веб-страницы. Эти свойства затем используются в методе `login`, который выполняет действия входа в систему.


##  **Дандерные методы (Dunder Methods)**:

Дандерные методы (или магические методы) в Python — это специальные методы, имена которых начинаются и заканчиваются двойным подчеркиванием, например `__init__` или `__str__`. Они предоставляют способ реализации поведения объектов, которое не может быть представлено обычными методами. Вот некоторые из наиболее часто используемых дандерных методов:

- `__init__(self, ...)`: Используется для инициализации нового объекта с начальным состоянием.
- `__del__(self)`: Вызывается при удалении объекта с целью выполнения очистки.
- `__repr__(self)`: Предоставляет официальное строковое представление объекта, которое можно использовать для воссоздания этого объекта.
- `__str__(self)`: Предоставляет более читаемое строковое представление объекта, предназначенное для конечного пользователя.
- `__call__(self, ...)`: Позволяет объекту быть вызванным как функция.
- `__getattr__(self, name)`: Вызывается, когда атрибут не найден в обычных местах.
- `__setattr__(self, name, value)`: Назначает значение атрибуту.
- `__delattr__(self, name)`: Удаляет атрибут.
- `__getitem__(self, key)`: Позволяет объекту использовать синтаксис индексации.
- `__setitem__(self, key, value)`: Назначает значение по индексу или ключу.
- `__delitem__(self, key)`: Удаляет элемент по индексу или ключу.
- `__iter__(self)`: Возвращает итератор для объекта.
- `__next__(self)`: Возвращает следующий элемент в итерации.
- `__contains__(self, item)`: Проверяет наличие элемента в объекте.
- `__eq__(self, other)`: Определяет поведение оператора равенства `==`.
- `__ne__(self, other)`: Определяет поведение оператора неравенства `!=`.
- `__lt__(self, other)`: Определяет поведение оператора `<`.
- `__le__(self, other)`: Определяет поведение оператора `<=`.
- `__gt__(self, other)`: Определяет поведение оператора `>`.
- `__ge__(self, other)`: Определяет поведение оператора `>=`.

Дандерные методы позволяют использовать встроенные функции Python и операторы с пользовательскими объектами, обеспечивая интуитивно понятный и единообразный интерфейс. Например, реализация `__str__` позволяет использовать функцию `print()` для вывода информации об объекте, а `__getitem__` и `__setitem__` позволяют объекту вести себя как коллекция, доступ к элементам которой осуществляется с помощью синтаксиса квадратных скобок.


## Именованные кортежи в Python

### namedtuple

`namedtuple` в Python — это функция из модуля `collections`, которая предоставляет возможность создавать кортежи с именованными полями. Это обеспечивает читаемость обычных кортежей, но с добавлением возможности доступа к значениям по имени, а не только по индексу.

**Основные особенности `namedtuple`:**
- **Именованные поля**: Каждый элемент `namedtuple` может быть доступен через уникальное имя.
- **Неизменяемость**: Как и обычные кортежи, `namedtuple` неизменяем после создания.
- **Эффективность по памяти**: `namedtuple` эффективнее обычных классов, так как не хранят словарь `__dict__`, который обычно используется для хранения атрибутов экземпляра.

**Создание `namedtuple`:**
Чтобы создать `namedtuple`, нужно указать имя нового типа и строку с именами полей, разделенными пробелами или запятыми.

```python
from collections import namedtuple

# Создаем тип 'Person' с полями 'name' и 'age'
Person = namedtuple('Person', 'name age')
```

**Использование `namedtuple`:**
Созданный тип можно использовать для создания объектов, которые будут вести себя как кортежи, но с доступом к данным по имени.

```python
# Создаем объект 'Person'
p = Person(name="Иван", age=30)

# Доступ к данным
print(p.name)  # Выведет: Иван
print(p.age)   # Выведет: 30
```

**Методы `namedtuple`:**
`namedtuple` предоставляет несколько полезных методов, таких как `_make()`, `_asdict()`, `_replace()`, и `_fields`.

- `_make(iterable)`: Создает новый экземпляр `namedtuple` из последовательности или итерируемого объекта.
- `_asdict()`: Преобразует `namedtuple` в `OrderedDict`.
- `_replace(**kwargs)`: Возвращает новый экземпляр `namedtuple`, заменяя указанные поля.
- `_fields`: Возвращает кортеж с именами полей.

**Пример использования методов:**

```python
# Создаем объект 'Person'
p = Person(name="Иван", age=30)

# Преобразуем в словарь
print(p._asdict())  # Выведет: {'name': 'Иван', 'age': 30}

# Замена значения поля
p_new = p._replace(name="Алексей")
print(p_new.name)  # Выведет: Алексей
print(p_new._fields) # Выведет: ('name', 'age')
print(p_new._asdict()) # Выведет: {'name': 'Алексей', 'age': 30}

```

**Преимущества и ограничения:**
`namedtuple` идеально подходит для быстрого создания неизменяемых объектов, когда вам нужна структура данных с именованными полями для улучшения читаемости кода. Однако, если вам нужны изменяемые объекты или более сложная логика, лучше использовать обычные классы.

`namedtuple` может быть особенно полезен в тестировании для структурирования тестовых данных. Вот несколько примеров, где `namedtuple` может использоваться в реальных тестовых сценариях:

1. **Хранение данных для тестовых случаев**:
   Вместо использования словарей или обычных классов, `namedtuple` может использоваться для создания читаемых и неизменяемых контейнеров для хранения тестовых данных.

```python
from collections import namedtuple

# Определение namedtuple для тестовых данных
TestData = namedtuple('TestData', 'username password expected_result')

# Создание тестовых данных
test_data_1 = TestData(username="user1", password="pass1", expected_result=True)
test_data_2 = TestData(username="user2", password="pass2", expected_result=False)

# Использование в тесте
def test_login(test_data):
    # Здесь будет логика теста, использующая test_data
    pass

test_login(test_data_1)
test_login(test_data_2)
```

2. **Параметризация тестов**:
   `namedtuple` удобно использовать с параметризацией в тестовых фреймворках, таких как pytest, для передачи наборов данных в тестовую функцию.

```python
import pytest
from collections import namedtuple

# Определение namedtuple для параметров теста
TestParams = namedtuple('TestParams', 'input expected')

# Тестовые параметры
params = [
    TestParams(input=10, expected=100),
    TestParams(input=20, expected=400),
]

# Параметризованный тест
@pytest.mark.parametrize("test_params", params)
def test_square(test_params):
    assert test_params.input ** 2 == test_params.expected
```

3. **Моделирование ответов API**:
   При тестировании API можно использовать `namedtuple` для моделирования ожидаемых ответов, что упрощает проверку корректности полученных данных.

```python
from collections import namedtuple

# Определение namedtuple для ответа API
ApiResponse = namedtuple('ApiResponse', 'status_code data')

# Моделирование ожидаемого ответа
expected_response = ApiResponse(status_code=200, data={"key": "value"})

# Функция для тестирования API
def test_api():
    # Здесь будет логика теста, сравнивающая реальный и ожидаемый ответы
    pass
```

### typing.NamedTuple

`typing.NamedTuple` — это улучшенная версия `namedtuple` из модуля `collections`, которая добавляет поддержку аннотаций типов из модуля `typing`. Это позволяет использовать `NamedTuple` для создания классов, которые работают как кортежи, но с дополнительной возможностью аннотирования типов их полей для лучшей интеграции с системой типизации Python.

**Основные особенности `typing.NamedTuple`:**
- **Аннотации типов**: Каждое поле может иметь аннотацию типа, что улучшает совместимость с инструментами статического анализа кода.
- **Поддержка методов**: В отличие от `namedtuple`, `typing.NamedTuple` позволяет определять методы внутри класса.
- **Неизменяемость**: Экземпляры `NamedTuple` также являются неизменяемыми, как и `namedtuple`.

**Создание `typing.NamedTuple`:**
Для создания `NamedTuple` используется синтаксис класса, где поля определяются как переменные с аннотациями типов.

```python
from typing import NamedTuple

class Person(NamedTuple):
    name: str
    age: int
```

**Использование `typing.NamedTuple`:**
Экземпляры `NamedTuple` создаются и используются так же, как и обычные кортежи, но с дополнительными преимуществами типизации.

```python
# Создаем объект 'Person'
p = Person(name="Иван", age=30)

# Доступ к данным
print(p.name)  # Выведет: Иван
print(p.age)   # Выведет: 30
```

**Методы `typing.NamedTuple`:**
`NamedTuple` наследует все методы `namedtuple`, такие как `_make()`, `_asdict()`, `_replace()`, и `_fields`, и позволяет добавлять собственные методы.

**Пример добавления метода:**

```python
from typing import NamedTuple

class Person(NamedTuple):
    name: str
    age: int

    def greet(self):
        return f"Привет, меня зовут {self.name}!"

# Создаем объект 'Person'
p = Person(name="Иван", age=30)

# Вызываем метод
print(p.greet())  # Выведет: Привет, меня зовут Иван!
```

**Преимущества и ограничения:**
`typing.NamedTuple` предоставляет все преимущества `namedtuple`, но с добавленной строгостью и ясностью типизации. Это делает его идеальным выбором для ситуаций, когда необходима четкая типизация и возможность определения методов. Однако, как и `namedtuple`, `NamedTuple` не подходит для создания изменяемых объектов.

Вот несколько примеров использования `typing.NamedTuple` в различных сценариях тестирования:

1. **Тестирование API**:
   Создание моделей ответов API с аннотациями типов для проверки соответствия ответов спецификациям.

```python
from typing import NamedTuple, List, Dict

class ApiResponse(NamedTuple):
    status_code: int
    data: List[Dict[str, str]]
    message: str

# Предположим, что это ожидаемый ответ от списка пользователей
expected_response = ApiResponse(
    status_code=200,
    data=[{"name": "Иван", "age": "30"}, {"name": "Мария", "age": "25"}],
    message="Пользователи успешно получены"
)

# Функция для тестирования API
def test_user_list_api():
    # Здесь будет логика отправки запроса и проверки ответа
    pass
```

2. **Параметризация тестов**:
   Использование `typing.NamedTuple` для параметризации тестов в Pytest, обеспечивая четкую типизацию входных и ожидаемых значений.

```python
import pytest
from typing import NamedTuple

class TestParams(NamedTuple):
    input: int
    expected: int

# Параметры для теста функции, вычисляющей квадрат числа
params = [
    TestParams(input=2, expected=4),
    TestParams(input=3, expected=9),
]

@pytest.mark.parametrize("test_params", params)
def test_square(test_params):
    assert test_params.input ** 2 == test_params.expected
```

3. **Тестирование пользовательского интерфейса**:
   Определение моделей данных для форм, которые могут быть использованы для автоматизации тестирования пользовательского интерфейса.

```python
from typing import NamedTuple

class RegistrationForm(NamedTuple):
    username: str
    email: str
    password: str
    confirm_password: str

# Тестовые данные для формы регистрации
registration_data = RegistrationForm(
    username="testuser",
    email="test@example.com",
    password="securePass123",
    confirm_password="securePass123"
)

# Функция для тестирования формы регистрации
def test_registration_form():
    # Здесь будет логика заполнения формы и проверки результатов
    pass
```

### dataclass

`dataclass` в Python — это декоратор и библиотека, которая автоматически добавляет специальные методы, такие как `__init__()`, `__repr__()`, и `__eq__()`, в классы, упрощая процесс создания классов, предназначенных для хранения данных.

**Основные особенности `dataclass`:**
- **Автоматическая генерация методов**: Python автоматически создает методы `__init__()`, `__repr__()`, и `__eq__()`, что уменьшает количество шаблонного кода.
- **Поддержка аннотаций типов**: Подобно `typing.NamedTuple`, `dataclass` поддерживает аннотации типов для полей.
- **Изменяемость**: В отличие от `NamedTuple`, экземпляры `dataclass` могут быть изменяемыми, если только вы явно не укажете `frozen=True`.

**Создание `dataclass`:**
Чтобы создать `dataclass`, вы используете декоратор `@dataclass` над классом и определяете поля с аннотациями типов.

```python
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0
```

**Использование `dataclass`:**
Создание и использование экземпляров `dataclass` происходит так же, как и с обычными классами.

```python
# Создаем объект 'Product'
product = Product(name="Чай", price=150.0)

# Доступ к данным
print(product.name)  # Выведет: Чай
print(product.price)  # Выведет: 150.0
```

**Методы `dataclass`:**
Помимо автоматической генерации методов `__init__()`, `__repr__()` и `__eq__()`, `dataclass` позволяет добавлять дополнительные методы и использовать различные параметры для настройки поведения класса.


- `__post_init__(self)`: Этот специальный метод вызывается сразу после `__init__()`. Он полезен для инициализации полей, которые зависят от других полей.

```python
from dataclasses import dataclass, field

@dataclass
class Point:
    x: int
    y: int
    z: int = field(init=False)

    def __post_init__(self):
        self.z = self.x + self.y
```

- `field()`: Функция `field()` используется для настройки атрибутов полей в `dataclass`. Например, можно задать значение по умолчанию или указать, что поле не должно учитываться при сравнении объектов.

```python
from dataclasses import dataclass, field

@dataclass
class Product:
    name: str
    price: float
    quantity: int = field(default=0, compare=False)
```

Функция `field` используется для тонкой настройки атрибутов данных в классах данных. Она предоставляет несколько именованных аргументов для управления поведением атрибутов:

- **default**: Устанавливает значение по умолчанию для поля.
- **default_factory**: Принимает вызываемый объект, который возвращает начальное значение поля.
- **init**: Если `True`, поле будет включено в сгенерированный метод `__init__`.
- **repr**: Если `True`, поле будет включено в сгенерированный метод `__repr__`.
- **compare**: Если `True`, поле будет участвовать в сравнениях.
- **hash**: Может быть `None`, `True` или `False`. Указывает, должно ли поле участвовать в вычислении хеша.
- **metadata**: Принимает словарь с метаданными пользователя. Эти данные не используются напрямую `dataclasses`, но доступны для использования.

Вот пример класса данных с использованием `field`:

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class InventoryItem:
    """Класс для отслеживания инвентаря в магазине."""
    name: str
    unit_price: float
    quantity_on_hand: int = 0
    tags: List[str] = field(default_factory=list, repr=False)

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand

# Пример использования
item = InventoryItem(name="Кресло", unit_price=299.99)
print(item)
```

В этом примере `tags` имеет `default_factory`, который указывает на пустой список, если другое значение не предоставлено, и `repr=False`, что означает, что `tags` не будет включен в строковое представление объекта.


- `asdict()`: Этот метод позволяет преобразовать объект `dataclass` в словарь, что может быть полезно для сериализации или работы с данными в формате, ожидаемом другими частями программы.

```python
from dataclasses import dataclass, asdict

@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0

product = Product('Чай', 150.0, 4)
product_dict = asdict(product)
```

- `astuple()`: Аналогично `asdict()`, `astuple()` преобразует объект `dataclass` в кортеж.

```python
from dataclasses import dataclass, astuple

@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0

product = Product('Чай', 150.0, 4)
product_tuple = astuple(product)
```

- `replace()`: Этот метод создает новый объект `dataclass`, заменяя указанные поля переданными значениями.

```python
from dataclasses import dataclass, replace

@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0

product = Product('Чай', 150.0, 4)
new_product = replace(product, name='Кофе')
```

**Параметры декоратора `@dataclass`:**
- `init`: Если `True`, создается метод `__init__()`.
- `repr`: Если `True`, создается метод `__repr__()`.
- `eq`: Если `True`, создается метод `__eq__()`.
- `order`: Если `True`, добавляются методы для сравнения объектов (`__lt__`, `__le__`, `__gt__`, `__ge__`).
- `unsafe_hash`: Если `True`, создается метод `__hash__()`.
- `frozen`: Если `True`, объект становится неизменяемым.


**Пример добавления метода:**

```python
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0

    def total_cost(self) -> float:
        return self.price * self.quantity

# Создаем объект 'Product'
product = Product(name="Чай", price=150.0, quantity=4)

# Вызываем метод
print(product.total_cost())  # Выведет: 600.0
```

**Преимущества и ограничения:**
`dataclass` упрощает создание классов для хранения данных и обеспечивает большую гибкость по сравнению с `NamedTuple`, особенно когда требуется изменяемость объектов. Однако, если вам нужны неизменяемые объекты с поддержкой кортежей, `NamedTuple` может быть более подходящим выбором.

 Вот несколько примеров, как `dataclass` может быть использован в автоматизированном тестировании:

**1. Определение тестовых данных:**
Вы можете использовать `dataclass` для определения тестовых данных, что упрощает их создание и управление.

```python
from dataclasses import dataclass

@dataclass
class TestUser:
    username: str
    password: str
    email: str

# Создание тестового пользователя
test_user = TestUser(username="testuser", password="securepass", email="test@example.com")
```

**2. Параметризация тестов:**
С `dataclass` вы можете легко параметризовать тесты, передавая различные наборы данных в тестовые функции.

```python
import pytest
from dataclasses import dataclass

@dataclass
class LoginData:
    username: str
    password: str
    expected_result: bool

# Тестовые данные
login_test_data = [
    LoginData(username="user1", password="pass1", expected_result=True),
    LoginData(username="user2", password="wrongpass", expected_result=False),
]

@pytest.mark.parametrize("data", login_test_data)
def test_login(data):
    assert login(data.username, data.password) == data.expected_result
```

**3. Использование в фикстурах:**
Фикстуры в pytest могут использовать `dataclass` для создания сложных тестовых объектов, которые затем могут быть использованы в нескольких тестах.

```python
import pytest
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    in_stock: bool

@pytest.fixture
def product_fixture():
    return Product(name="Test Product", price=9.99, in_stock=True)

def test_product_in_stock(product_fixture):
    assert product_fixture.in_stock is True
```

**4. Сравнение ожидаемых и фактических результатов:**
`Dataclass` упрощает сравнение сложных структур данных, что полезно при проверке ожидаемых результатов теста.

```python
from dataclasses import dataclass

@dataclass
class ApiResponse:
    status_code: int
    body: dict

def test_api_response():
    expected_response = ApiResponse(status_code=200, body={"key": "value"})
    actual_response = call_api()  # Функция, которая вызывает API и возвращает ApiResponse
    assert expected_response == actual_response
```