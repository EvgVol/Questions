# Задача
# Напиши функцию, которая определит наибольшее из трех целых чисел


def max_of_three(a, b, c):
    ...


# ----------------------------------------------------------------------------
# def max(a, b, c):
#     lst = [a, b, c]
#     lst.sort(reverse=True)
#     return lst[0]
# ----------------------------------------------------------------------------

# Задача
# Напиши функцию, которая выводит числа из списка lst,
# находящиеся в диапазоне [start, end] с фильтром (по дефолту - без фильтра).
# Если передан фильтр filter_fn, выводит только те числа, которые проходят через него.

def foo(lst, start, end, filter_fn=None):
    ...


# ----------------------------------------------------------------------------
# def foo(lst, start, end, filter_fn=None, sort_fn=False):
    # result = [x for x in lst if start <= x <= end]

    # if filter_fn:
    #     result = [x for x in result if filter_fn(x)]
    # if result_sorted:
    #     result.sort()
    # return result

    # result = [x for x in lst if start <= x <= end and (filter_fn(x) if filter_fn else True)]
    # return sorted(result) if sort_fn else result



# assert foo([1.1, 2.5, 3.7, 4.0, 5.9], 2.0, 4.5) == [2.5, 3.7, 4.0]
# assert foo([1, 9, 6, 4, 5, 8], 1, 7, lambda x: x % 2 == 0 and x > 3, sort_fn=True) == [4, 6]
# assert foo([1, 2, 3, 4, 5], 5, 2) == []
# assert foo([10, 20, 30, 40, 50], 15, 35) == [20, 30]
# assert foo([-5, -2, 0, 3, 7], -3, 3, sort_fn=True) == [-2, 0, 3]
# assert foo([], 1, 10) == []
# assert foo([1, 2, 3, 4, 5], -10, 10, lambda x: x > 3)
# assert foo([1, 2, 3, 4, 5], 10, 20) == []
# assert foo([1, 2, 3, 4, 5], 2, 4, lambda x: x % 2 == 0) == [2, 4]
# assert foo([1, 2, 3, 4, 5], 1, 6, lambda x: x % 2 != 0) == [1, 3, 5]
# assert foo([10, 20, 3, 16, 8], 10, 20, lambda x: x > 15, sort_fn=True) == [16, 20]
# ----------------------------------------------------------------------------

