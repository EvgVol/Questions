def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]

        less = [i for i in lst[1:] if i <= pivot]
        greater = [i for i in lst[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([20, 21, 22, 23, -24, 28, 35]))