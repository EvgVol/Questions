def add_safe(a, b):
    try:
        return a + b
    except TypeError:
        print("Type Error")



print(add_safe(2, 5))
print(add_safe(2, "5"))
print("end")