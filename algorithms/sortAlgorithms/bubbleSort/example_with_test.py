def bubble_sort(lst):
    last_index = len(lst) - 1
    for i in range(last_index, 0, -1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


def test_buble_sort():
    lst1 = [1, 5, 3, 8, 2]
    result = bubble_sort(lst1)
    print('True' if result == [1, 2, 3, 5, 8] else 'False')

    lst2 = [0, -5, -3, 1, -2]
    result = bubble_sort(lst2)
    print('True' if result == [-5, -3, -2, 0, 1] else 'False')

    lst3 = [-1, -5, -3, -8, -2]
    result = bubble_sort(lst3)
    print('True' if result == [-8, -5, -3, -2, -1] else 'False')


test_buble_sort()
