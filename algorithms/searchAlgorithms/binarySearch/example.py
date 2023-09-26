def binary_search(lst, item):
    left = 0
    right = len(lst) - 1
    flag = False

    while left <= right and not flag:
        mid = (right + left) // 2
        if lst[mid] == item:
            flag = True
        elif lst[mid] < item:
            left = mid + 1
        else:
            right = mid - 1
    return flag


def test_binary_search():
    assert binary_search([1, 2, 6, 9, 15, 22, 26, 38, 45], 6) == True
    assert binary_search([1, 2, 6, 9, 15, 22, 26, 38, 45], 0) == False
    assert binary_search([0, 0, 1, 9, 15, 22, 26, 38, 45], 0) == True
    assert binary_search([-5, -2, 0, 9, 15, 22, 26, 38, 45], -2) == True


test_binary_search()