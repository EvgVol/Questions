def interpolation_search(lst, x):
    (left, right, found) = (0, len(lst) - 1, False)

    while lst[left] != lst[right] and lst[left] <= x <= lst[right]:
        mid = left + (x - lst[left]) * (right - left) // (lst[right] - lst[left])
        if lst[mid] == x:
            found = True
            return found
        if lst[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return found
