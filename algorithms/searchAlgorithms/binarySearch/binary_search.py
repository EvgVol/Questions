def binary_search(lst, item):
    first = 0
    last = len(lst) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2
        if lst[mid] == item:
            found = True
        else:
            if item < lst[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found
