import unittest

from .bubble_sort import bubble_sort


class TestBubble(unittest.TestCase):
    """Проверяем правильность выполнение сортировки пузырьком."""

    def test_althorims(self):
        lst1 = [1, 5, 3, 8, 2]
        test_data = bubble_sort(lst1)
        self.assertEqual(test_data, [1, 2, 3, 5, 8])
