# 12 Декараторов которые улучшают код

## @logger

Если вы только знакомитесь с декораторами, можете считать их функциями, которые принимают другие функции в качестве входных данных и расширяют их функциональность без изменения основного назначения.

Начнем с простого декоратора, который расширяет функцию, регистрируя время начала и окончания ее выполнения.

Результат работы декорируемой функции будет выглядеть следующим образом:

```bash
some_function(args)

# ----- some_function: начало -----
# some_function выполняется
# ----- some_function: окончание -----
```

Чтобы написать этот декоратор, нужно сначала подобрать ему подходящее имя. Назовем его `logger`.

__logger__  —  это функция, которая принимает другую функцию в качестве входной и возвращает ее в качестве выходной. Выходная функция обычно является расширенной версией входной. В нашем случае нужно, чтобы выходная функция окружала вызов входной функции утверждениями start и end.

Поскольку нам неизвестно, какие аргументы использует входная функция, можем передать их из функции-обертки с помощью выражений *args и **kwargs. Эти выражения позволяют передавать произвольное количество позиционных и ключевых аргументов.

Вот простая реализация декоратора logger:

```python
def logger(function):
    def wrapper(*args, **kwargs):
        print(f"----- {function.__name__}: start -----")
        output = function(*args, **kwargs)
        print(f"----- {function.__name__}: end -----")
        return output
    return wrapper
```

Теперь можно применить `logger` к `some_function` или любой другой функции.

```python
decorated_function = logger(some_function)
```

Python предоставляет более “питонический” синтаксис для этого: он предлагает перед определением функции указывать символ @, после которого идет имя декоратора:

```python
@logger
def some_function(text):
    print(text)

some_function("first test")
# ----- some_function: начало -----
# первый тест
# ----- some_function: окончание -----

some_function("second test")
# ----- some_function: начало -----
# второй тест
# ----- some_function: окончание -----
```

## @wraps

Этот декоратор обновляет функцию-обертку, чтобы она выглядела как оригинальная функция и наследовала ее имя и свойства.

Для понимания того, что делает и зачем используется @wraps, возьмем предыдущий декоратор и применим его к простой функции, которая складывает два числа.

Этот декоратор еще не использует @wraps.

```python
def logger(function):
    def wrapper(*args, **kwargs):
        """wrapper documentation"""
        print(f"----- {function.__name__}: start -----")
        output = function(*args, **kwargs)
        print(f"----- {function.__name__}: end -----")
        return output
    return wrapper

@logger
def add_two_numbers(a, b):
    """this function adds two numbers"""
    return a + b
```

Если мы проверим имя и документацию декорированной функции add_two_numbers, вызвав атрибуты __name__ и __doc__, получим странные (и все же ожидаемые) результаты:

```python
add_two_numbers.__name__
'wrapper'

add_two_numbers.__doc__
'wrapper documentation'
```

Мы получаем имя обертки и документацию.


Это нежелательный результат. Нам необходимо сохранить имя исходной функции и документацию. Вот тут-то и пригодится `@wraps`.

__Нужно лишь декорировать функцию-обертку.__

```python
from functools import wraps

def logger(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        """wrapper documentation"""
        print(f"----- {function.__name__}: start -----")
        output = function(*args, **kwargs)
        print(f"----- {function.__name__}: end -----")
        return output
    return wrapper

@logger
def add_two_numbers(a, b):
    """this function adds two numbers"""
    return a + b
```

Перепроверив имя и документацию, увидим метаданные исходной функции:

```python
add_two_numbers.__name__
# 'add_two_numbers'

add_two_numbers.__doc__
# 'this function adds two numbers'
```

## @lru_cache

Это встроенный декоратор, который можно импортировать из `functools`.

Он кэширует возвращаемые значения функции, используя при заполнении кэша алгоритм `LRU`  —  алгоритм замещения наименее часто используемых значений.

Обычно я применяю этот декоратор для длительно выполняющихся задач, которые не меняют результат при одинаковых входных данных, например для запроса к базе данных, запроса статической удаленной веб-страницы и выполнения сложной обработки.

В следующем примере `@lru_cache` используется для декорирования функции, которая имитирует некую обработку. Эта функция применяется на одном и том же входе несколько раз подряд.

```python
import random
import time
from functools import lru_cache

@lru_cache(maxsize=None)
def heavy_processing(n):
    sleep_time = n + random.random()
    time.sleep(sleep_time)

# первый раз
%%time
heavy_processing(0)
# Процессорное время: user 363 µs, sys: 727 µs, всего: 1.09 мс
# Время по часам: 694 мс

# второй раз
%%time
heavy_processing(0)
# Процессорное время: user 4 µs, sys: 0 ns, всего: 4 µs
# Время по часам: 8.11 µs

# третий раз 
%%time
heavy_processing(0)
# Процессорное время: user 5 µs, sys: 1 µs, всего: 6 µs
# Время по часам: 7.15 µs
```

Чтобы реализовать декоратор кэша самостоятельно с нуля, выполните следующее:

Добавьте пустой словарь в качестве атрибута к функции-обертке для хранения значений, ранее вычисленных входной функцией.
При вызове входной функции сначала проверьте, присутствуют ли ее аргументы в кэше. Если да  —  результат возвращается. В противном случае вычислите его и поместите в кэш.

```python
from functools import wraps

def cache(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key in wrapper.cache:
            output = wrapper.cache[cache_key]
        else:
            output = function(*args)
            wrapper.cache[cache_key] = output
        return output
    wrapper.cache = dict()
    return wrapper

@cache
def heavy_processing(n):
    sleep_time = n + random.random()
    time.sleep(sleep_time)

%%time
heavy_processing(1)
# Процессорное время: user 446 µs, sys: 864 µs, всего: 1.31 ms
# Время по часам: 1.06 с

%%time
heavy_processing(1)
# Процессорное время: user 11 µs, sys: 0 ns, всего: 11 µs
# Время по часам: 13.1 µs
```

## 4. @repeat

Этот декоратор заставляет функцию вызываться несколько раз подряд. Он может быть полезен для отладки, стресс-тестов и автоповтора нескольких задач.

В отличие от предыдущих декораторов этот предполагает входной параметр.

```python
def repeat(number_of_times):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(number_of_times):
                func(*args, **kwargs)
        return wrapper
    return decorate
```

В следующем примере определяется декоратор @repeat, который принимает в качестве аргумента количество вызовов. Затем декоратор определяет функцию wrapper, которая оборачивает декорируемую функцию. Функция wrapper вызывает декорируемую функцию столько раз, сколько указано в аргументе.

```python
@repeat(5)
def dummy():
    print("hello")

dummy()
# hello
# hello
# hello
# hello
# hello

```
## 5. @timeit 
Этот декоратор измеряет время выполнения функции и выводит результат, что необходимо для отладки и мониторинга.

В следующем фрагменте декоратор @timeit измеряет время выполнения функции process_data, выводя истекший временной период в секундах.

```python
import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'{func.__name__} took {end - start:.6f} seconds to complete')
        return result
    return wrapper

@timeit
def process_data():
    time.sleep(1)

process_data()
# функция process_data заняла 1,000012 с
```

## 6. @retry

Этот декоратор заставляет функцию, которая сталкивается с исключением, совершить несколько повторных попыток.

Он принимает три аргумента:

- количество повторных попыток;
- исключение, которое нужно поймать и повторно выполнить;
- время сна (sleep time) между повторными попытками.

Это работает следующим образом.

Функция-обертка запускает цикл for с количеством итераций num_retries.

На каждой итерации она вызывает входную функцию в блоке try/except. При успешном вызове она прерывает цикл и возвращает результат. В противном случае она ожидает в течение sleep_time секунд и переходит к следующей итерации.
Если после завершения цикла for вызов функции не удается, функция-обертка инициирует исключение.

```python
import random
import time
from functools import wraps

def retry(num_retries, exception_to_check, sleep_time=0):
    """
    Decorator that retries the execution of a function if it raises a specific exception.
    """
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, num_retries+1):
                try:
                    return func(*args, **kwargs)
                except exception_to_check as e:
                    print(f"{func.__name__} raised {e.__class__.__name__}. Retrying...")
                    if i < num_retries:
                        time.sleep(sleep_time)
            # Инициирование исключения, если функция оказалсь неуспешной после указанного количества повторных попыток
            raise e
        return wrapper
    return decorate

@retry(num_retries=3, exception_to_check=ValueError, sleep_time=1)
def random_value():
    value = random.randint(1, 5)
    if value == 3:
        raise ValueError("Value cannot be 3")
    return value

random_value()
# random_value вызвало ValueError. Повторная попытка...
# 1

random_value()
# 5
```

## 7. @countcall

Декоратор @countcall подсчитывает, сколько раз была вызвана функция.

Это число хранится в атрибуте обертки count.

```python
from functools import wraps

def countcall(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        result = func(*args, **kwargs)
        print(f'{func.__name__} has been called {wrapper.count} times')
        return result
    wrapper.count = 0
    return wrapper

@countcall
def process_data():
    pass

process_data()
process_data has been called 1 times
process_data()
process_data has been called 2 times
process_data()
process_data has been called 3 times
```

## 8. @rate_limited 
Это декоратор, который ограничивает частоту вызова функции. Если функция вызывается слишком часто, он заставляет ее заснуть на некоторое время.

```python
import time
from functools import wraps

def rate_limited(max_per_second):
    min_interval = 1.0 / float(max_per_second)
    def decorate(func):
        last_time_called = [0.0]
        @wraps(func)
        def rate_limited_function(*args, **kargs):
            elapsed = time.perf_counter() - last_time_called[0]
            left_to_wait = min_interval - elapsed
            if left_to_wait > 0:
                time.sleep(left_to_wait)
            ret = func(*args, **kargs)
            last_time_called[0] = time.perf_counter()
            return ret
        return rate_limited_function
    return decorate
    
```
Декоратор работает, измеряя время, прошедшее с момента последнего вызова функции, и при необходимости заставляет ее ожидать соответствующее количество времени, чтобы не превысить лимит частоты. Время ожидания рассчитывается как min_interval - elapsed, где:

* min_interval  —  минимальный интервал времени (в секундах) между двумя вызовами функции;
* elapsed  —  время, прошедшее с момента последнего вызова.
Если прошедшее время меньше минимального интервала, функция ожидает в течение left_to_wait секунд перед повторным выполнением.

Таким образом, эта функция связана с небольшими временными издержками между вызовами, но гарантирует, что лимит частоты не будет превышен.

Есть также сторонний пакет, реализующий ограничение частоты API. Он называется ratelimit.

```bash
pip install ratelimit
```

Чтобы использовать этот пакет, надо просто декорировать любую функцию, которая делает вызов API:

```python
from ratelimit import limits

import requests

FIFTEEN_MINUTES = 900

@limits(calls=15, period=FIFTEEN_MINUTES)
def call_api(url):
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception('API response: {}'.format(response.status_code))
    return response
Если декорированная функция вызывается большее количество раз, чем разрешено, то инициируется исключение ratelimit.RateLimitException.

Для обработки этого исключения можно использовать декоратор @sleep_and_retry в сочетании с декоратором @ratelimit.

@sleep_and_retry
@limits(calls=15, period=FIFTEEN_MINUTES)
def call_api(url):
    response = requests.get(url)

if response.status_code != 200:
        raise Exception('API response: {}'.format(response.status_code))
    return response

```
Это заставит функцию спать оставшееся время перед повторным выполнением.

## 9. @dataclass

Декоратор @dataclass в Python используется для декорирования классов.

Он автоматически генерирует специальные методы, такие как __init__, __repr__, __eq__, __lt__ и __str__ для классов, которые в основном хранят данные. Это позволяет сократить объем кода и сделать классы более читаемыми и удобными для сопровождения.

Он также предоставляет готовые методы для элегантного представления объектов, преобразования их в формат JSON, обеспечения их неизменяемости и т. д.

Декоратор `@dataclass` был представлен в Python 3.7 и доступен в стандартной библиотеке.

```python
from dataclasses import dataclass, 

@dataclass
class Person:
    first_name: str
    last_name: str
    age: int
    job: str

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.age == other.age
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Person):
            return self.age < other.age
        return NotImplemented

john = Person(first_name="John", 
              last_name="Doe", 
              age=30, 
              job="doctor",)

anne = Person(first_name="Anne", 
              last_name="Smith", 
              age=40, 
              job="software engineer",)

print(john == anne)
# False

print(anne > john)
# True

asdict(anne)
#{'first_name': 'Anne',
# 'last_name': 'Smith',
# 'age': 40,
# 'job': 'software engineer'}
```

## 10. @register 
Когда Python-скрипт случайно завершается, а вы не успели выполнить какие-то задачи по сохранению работы, очистке или выводу сообщения, декоратор @register будет весьма полезен.

```python
from atexit import register

@register
def terminate():
    perform_some_cleanup()
    print("Goodbye!")

while True:
    print("Hello")
```
При запуске этого скрипта и нажатии CTRL+C,


Происходит вывод функции terminate.

## 11. @property

Этот декоратор используется для определения свойств класса, которые по сути являются методами getter, setter и deleter для атрибута экземпляра класса.

Используя декоратор `@property`, можно определить метод как свойство класса и получить к нему доступ, как к атрибуту класса, без явного вызова метода.

Это полезно, если нужно добавить некоторые ограничения и логику проверки в отношении получения и установки значения.

В следующем примере определяется метод setter для свойства rating, чтобы наложить ограничение на вводимое значение (от 0 до 5).

```python
class Movie:
    def __init__(self, r):
        self._rating = r

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, r):
        if 0 <= r <= 5:
            self._rating = r
        else:
            raise ValueError("The movie rating must be between 0 and 5!")

batman = Movie(2.5)
batman.rating
# 2.5
batman.rating = 4
batman.rating
# 4
batman.rating = 10

# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# Ввод In [16], в <cell line: 1>()
# ----> 1 batman.rating = 10
# Ввод In [11], в Movie.rating(self, r)
#      12     self._rating = r
#      13 else:
# ---> 14     raise ValueError("Оценка фильма должна быть от 0 до 5!")
#
# ValueError: Оценка фильма должна быть от 0 до 5!!
```

## 12. @singledispatch
Этот декоратор позволяет функции иметь различные реализации для разных типов аргументов.

```python
from functools import singledispatch

@singledispatch
def fun(arg):
    print("Called with a single argument")
@fun.register(int)
def _(arg):
    print("Called with an integer")
@fun.register(list)
def _(arg):
    print("Called with a list")
fun(1)  # Выводит "Called with an integer"
fun([1, 2, 3])  # Выводит "Called with a list"
```

## Заключение

__Декораторы__  —  полезные абстракции для расширения кода дополнительными функциями, такими как кэширование, автоповтор, ограничение частоты, регистрация и превращение классов в суперконтейнеры данных.

Но на этом тема декораторов не исчерпывается. Вы можете реализовать собственные декораторы для решения специфических проблем.
