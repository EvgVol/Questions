def shell_sort(lst):
    distanse = len(lst) // 2
    while distanse > 0:
        for i in range(distanse, len(lst)):
            temp = lst[i]
            j = i
            while j >= distanse and lst[j - distanse] > temp:
                lst[j] = lst[j - distanse]
                j = j - distanse
            lst[j] = temp
        distanse = distanse // 2
    return lst
