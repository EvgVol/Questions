def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        merge_sort(left)
        merge_sort(right)

        a = 0
        b = 0
        c = 0

        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                lst[c] = left[a]
                a = a + 1
            else:
                lst[c] = right[b]
                b = b + 1
            c = c + 1

        while a < len(left):
            lst[c] = left[a]
            a = a + 1
            c = c + 1

        while b < len(right):
            lst[c] = right[b]
            b = b + 1
            c = c + 1
    return lst


def test_merge_sort():
    
    assert merge_sort([]) == []
    assert merge_sort([5]) == [5]
    assert merge_sort([8, 3]) == [3, 8]
    assert merge_sort([5, 1, 9, 3, 7]) == [1, 3, 5, 7, 9]
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert merge_sort([5, 2, 5, 1, 5, 2]) == [1, 2, 2, 5, 5, 5]
    assert merge_sort([-10, 0, 3, -8, 15, 1]) == [-10, -8, 0, 1, 3, 15]

test_merge_sort()
