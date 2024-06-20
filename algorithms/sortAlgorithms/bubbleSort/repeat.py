from typing import List

test_list = [6, 4, 3, 1]

def bubble_sort(list_num: List[int]) -> List[int]:
    for i in range(len(list_num) - 1, 0, -1):
        for j in range(i):
            if list_num[j] > list_num[j+1]:
                list_num[j], list_num[j+1] = list_num[j+1], list_num[j]
    return list_num


print(bubble_sort([6, 4, 3, 1]))