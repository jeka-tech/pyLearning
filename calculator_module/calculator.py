def subtraction (first, second):
    if second > 0:
        const = -1
        temp_var = 0
        for i in range(second):
            temp_var = temp_var + const
        second = temp_var
    else:
        second = abs(second)
    return first + second

def multiplication (first, second):
    result = 0
    for i in range(second):
        result = result + first
    return result


# def division (a: int, b: int):
#     if b == 0:
#         return "Division by zero"
#     elif a == 0:
#         return 0
#     whole = 0
#     while (a-b) >= 0:
#         whole += 1
#         a = a - b
#     if a == 0:
#         return whole
#     else:
#         fractional = 0
#         a = a*10
#         while (a - b) >= 0:
#             fractional += 1
#             a = a - b
#         if a == 0:
#             return whole + fractional/10
#         print(whole + fractional/10)
#
# if __name__ == "__main__":
#     assert (division(200, 5) == 40)
#     assert (division(201, 5) == 40.2)
#     assert (division(2, 4) == 0.5)
#     assert (division(5, 5) == 1)
#     assert (division(125, 5) == 25)
#     assert (division(0, 5) == 0)
#     assert (division(3, 7) == round(3/7, 16))
#     assert (division(12343, 7443) == round(12343 / 7443, 16))
#     assert (division(-6, 12) == -0.5)
#     assert (division(-6, -12) == 0.5)
#     assert (division(6, -12) == -0.5)
#     assert (division(0, 0) == "Division by zero")
#     assert (division(3, 0) == "Division by zero")
#     print(division(2, 4))
#
