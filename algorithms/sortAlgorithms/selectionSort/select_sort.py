def select_sort(lst):
    for fill_slot in range(len(lst) - 1, 0, -1):
        max_index = 0
        for location in range(1, fill_slot + 1):
            if lst[location] > lst[max_index]:
                max_index = location
        lst[fill_slot], lst[max_index] = lst[max_index], lst[fill_slot]
    return lst
