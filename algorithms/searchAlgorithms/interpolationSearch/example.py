def interpolation_search(lst: list, item: int):
    left = 0
    right = len(lst) - 1
    flag = False

    while left != right and  lst[left] <= item <= lst[right]:
        mid = left + (item - lst[left]) * (right - left) // (lst[right] - lst[left])
        if lst[mid] == item:
            flag = True
            return flag
        elif lst[mid] < item:
            left = mid + 1
        else:
            right = mid - 1
    return flag


def test_interpolation_search():
    assert interpolation_search([0, 5, 36, 58, 78, 96], 4) == False
    assert interpolation_search([0, 5, 36, 58, 78, 96], 0) == True


test_interpolation_search()