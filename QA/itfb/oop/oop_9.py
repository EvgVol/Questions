def div_safe(a, b):
    try:
        result = a / b
    except TypeError:
        print("No string!")
    except ZeroDivisionError:
        print("No zero!")
    except ArithmeticError:
        print("Arithmetic Error!")
    else:
        print("return result")
        return result
    finally:
        print("done div", [a, b])


if __name__ == "__main__":
    print(div_safe(10, 4))
    print(div_safe(10, "4"))
    print(div_safe(10, 0))
