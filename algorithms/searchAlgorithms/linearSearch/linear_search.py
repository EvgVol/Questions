def linear_search(lst, item):
    index = 0
    found = False
    while index < len(lst) and found is False:
        if lst[index] == item:
            found = True
        else:
            index = index + 1
    return found
