

class CustomList(list):
    def __init__(self, iterable=None):
        super().__init__(iterable)
        self._list = list(iterable) if iterable else []

    def append(self, item: any):
        """Добавить элемент в конец списка."""
        self._list.append(item)

    def remove(self, item):
        """Удалить первое вхождение элемента из списка."""
        self._list.remove(item)

    def pop(self, index=-1):
        """Удалить элемент по индексу и вернуть его."""
        return self._list.pop(index)

    def insert(self, index, item):
        """Вставить элемент на указанную позицию."""
        self._list.insert(index, item)

    def clear(self):
        """Очистить список."""
        self._list.clear()

    def __getitem__(self, index):
        """Получить элемент по индексу."""
        return self._list[index]

    def __setitem__(self, index, value):
        """Установить значение элемента по индексу."""
        self._list[index] = value

    def __delitem__(self, index):
        """Удалить элемент по индексу."""
        del self._list[index]

    def __len__(self):
        """Получить длину списка."""
        return len(self._list)

    def __iter__(self):
        """Итерирование по элементам списка."""
        return iter(self._list)

    def __contains__(self, item):
        """Проверить, содержится ли элемент в списке."""
        return item in self._list

    def __repr__(self):
        """Строковое представление объекта."""
        return f"CustomList({self._list})"

    def __add__(self, other):
        """Сложение с другим списком."""
        if isinstance(other, CustomList):
            other = other._list
        return CustomList(self._list + other)

    def __iadd__(self, other):
        """In-place сложение с другим списком."""
        if isinstance(other, CustomList):
            other = other._list
        self._list += other
        return self

    def __eq__(self, other):
        """Сравнение двух списков."""
        if isinstance(other, CustomList):
            other = other._list
        return self._list == other
