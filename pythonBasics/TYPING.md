# Аннотации типов

Аннотации типов — это мощный инструмент для улучшения качества кода и облегчения совместной работы над проектами Python. Они помогают уточнить намерения разработчика и делают код более доступным для понимания и поддержки.



**Основные аспекты аннотации типов в Python:**

- **Базовая аннотация**: Для переменных и аргументов функций аннотации добавляются после двоеточия (`:`), а для возвращаемых значений функций — после стрелки (`->`).

```python
def add_numbers(x: int, y: int) -> int:
    return x + y
```

- **Типы контейнеров**: Для указания типов внутри контейнеров, таких как списки, словари и кортежи, используются специальные классы из модуля `typing`.

```python
from typing import List, Dict, Tuple

def process_items(items: List[int]) -> Dict[str, int]:
    # ...

coordinates: Tuple[int, int, int] = (10, 20, 30)
```

- **Optional и Union**: `Optional` указывает, что переменная может быть определённого типа или `None`. `Union` позволяет указать, что переменная может быть одним из нескольких типов.

```python
from typing import Optional, Union

def get_user(id: int) -> Optional[User]:
    # ...

def process(value: Union[int, str]):
    # ...
```

- **TypeVar и Generics**: `TypeVar` используется для создания обобщённых типов, которые могут быть заменены любым типом, а `Generics` позволяют определять классы и функции с параметрами типа.

```python
from typing import TypeVar, Generic, List

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self.items: List[T] = []

    def push(self, item: T):
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()
```

- **ClassVar**: `ClassVar` используется для определения переменных, которые предназначены для использования на уровне класса, а не экземпляра. Это означает, что переменная с `ClassVar` не будет разделяться между экземплярами класса, а будет иметь одно и то же значение для всего класса.

```python
from typing import ClassVar

class MyClass:
    # Это переменная класса, не изменяется между экземплярами
    class_variable: ClassVar[int] = 10
```

- **Использование в dataclasses**: В `dataclasses`, `ClassVar` исключает переменные из методов, таких как `__init__` и `__eq__`, которые автоматически генерируются, таким образом, `ClassVar` помогает определить, какие атрибуты должны быть атрибутами класса.

```python
from dataclasses import dataclass
from typing import ClassVar

@dataclass
class DataClassExample:
    class_variable: ClassVar[int] = 99
    instance_variable: int
```

В этом примере `class_variable` будет одинаковым для всех экземпляров `DataClassExample`, в то время как `instance_variable` может быть уникальным для каждого экземпляра.

__!__ `ClassVar` не используется с `TypeVar` и `Generics`, так как они относятся к параметризации типов для экземпляров.

- **InitVar**: `InitVar` — это специальный тип из модуля `dataclasses`, который используется для атрибутов, которые не являются частью данных объекта и нужны только во время инициализации. Это может быть полезно, когда вам нужно передать дополнительные параметры в метод `__post_init__` для дальнейшей обработки или настройки экземпляра класса.

**Как использовать `InitVar`?**
Вы объявляете `InitVar` внутри класса `dataclass`, и он не будет включен в автоматически сгенерированные методы, такие как `__init__`, `__repr__`, `__eq__` и другие.

**Пример использования `InitVar`:**

```python
from dataclasses import dataclass, field, InitVar

@dataclass
class DataClassWithInitVar:
    # Это переменная экземпляра
    instance_variable: int
    # Это InitVar, не будет включен в автоматически сгенерированные методы
    initialization_only: InitVar[int]

    def __post_init__(self, initialization_only):
        # Этот метод вызывается после __init__
        # Здесь можно использовать значение initialization_only
        print(f"Initialization only variable: {initialization_only}")

# Создание экземпляра класса с InitVar
my_instance = DataClassWithInitVar(10, 20)
```

В этом примере `initialization_only` является `InitVar` и используется только во время инициализации объекта `DataClassWithInitVar`. После инициализации, `initialization_only` не сохраняется как часть данных объекта.

__!__ `InitVar` не используется с `TypeVar` и `Generics`, так как его цель — передача параметров в `__post_init__`, а не параметризация типов экземпляров. `InitVar` не применяется к контейнерным типам, __он используется только в контексте инициализации.__

- **Type Hints в Python 3.8+**: Начиная с Python 3.8, можно использовать более простой синтаксис для аннотаций типов с использованием нового синтаксиса `:=`, известного как "walrus operator".

```python
total: int
if (total := sum([1, 2, 3])) > 5:
    print(f"Total is {total}")
```

- **Строгая проверка типов**: Строгая проверка типов не выполняется интерпретатором Python во время выполнения. Однако вы можете использовать инструменты, такие как `mypy`, для статической проверки типов в вашем коде.

Аннотации типов предназначены прежде всего для сторонних программ
проверки типов, например Mypy (https://mypy.readthedocs.io/en/stable/) или интегрированной среды разработки PyCharm (https://www.jetbrains.com/pycharm/) со встроенной проверкой типов. Это инструменты статического анализа: они проверяют «покоящийся» исходный код, а не код в процессе выполнения.