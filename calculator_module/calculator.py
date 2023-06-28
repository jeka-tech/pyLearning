import time


def subtraction (first, second):
    const = -1
    temp_var = 0

    if second > 0:
        for i in range(second):
            temp_var = temp_var + const
        second = temp_var
    else:
        second = abs(second)
    return first + second

def multiplication (first, second):
    result = 0
    if first == 0 or second == 0:
        return 0
    if second > 0:
        for i in range(second):
            result = result + first
    elif second < 0:
        for i in range(abs(second)):
            result = subtraction(result, first)
    return result


def division (a, b):
    if b == 0:
        return "Division by zero"
    elif a == 0:
        return 0

    if multiplication(a,b) > 0:
        result = ""
    else:
        result = "-"

    a = abs(a)
    b = abs(b)

    whole = 0

    while (a-b) >= 0:
        whole += 1
        a = a - b
    if a == 0:
        return whole

    result = result + str(whole) + '.'

    for i in range(16):
        fractional = 0
        a = a*10
        while (a - b) >= 0:
            fractional += 1
            a = a - b
        result = result + str(fractional)
        if a == 0:
            return float(result)
    return float(result)



if __name__ == "__main__":
    start = time.time()
    print(division(207686780, 5))
    print(time.time() - start)
    assert (division(200, 5) == 40)
    assert (division(201, 5) == 40.2)
    assert (division(2, 4) == 0.5)
    assert (division(5, 5) == 1)
    assert (division(125, 5) == 25)
    assert (division(0, 5) == 0)
    assert (division(3, 7) == round(3/7, 16))
    assert (division(12343, 7443) == round(12343 / 7443, 16))
    assert (division(-6, 12) == -0.5)
    assert (division(-6, -12) == 0.5)
    assert (division(6, -12) == -0.5)
    assert (division(0, 0) == "Division by zero")
    assert (division(3, 0) == "Division by zero")



