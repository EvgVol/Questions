def insertion_sort(lst):
    for i in range(1, len(lst)):
        j = i-1
        element_index = lst[i]
        while (lst[j] > element_index) and j >= 0:
            lst[j+1] = lst[j]
            j = j - 1
        lst[j+1] = element_index
    return lst


def test_insertion_sort():
    lst1 = [0, 1, 2, 4, 3]
    result = insertion_sort(lst1)
    print('True' if result == [0, 1, 2, 3, 4] else 'False')

    lst2 = [0, -5, -3, 1, -2]
    result = insertion_sort(lst2)
    print('True' if result == [-5, -3, -2, 0, 1] else 'False')

    lst3 = [-1, -5, -3, -8, -2]
    result = insertion_sort(lst3)
    print('True' if result == [-8, -5, -3, -2, -1] else 'False')


test_insertion_sort()
