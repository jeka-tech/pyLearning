def calc (a):
    return a + 3

# list-comprehensions -> listcomps
# generator-expressions -> genexp
# Синтаксис одинаковый, но в genexp используются круглые скобки
# Отличие big_numbers = [e for e in range(100000)]

numbers = [12, 0, -5, 7, 9, 12, -5]

positive = [e for e in range(100) ]


if __name__ == '__main__':
    sp = [3, 7, -8, 17]
    sp_new = (e for e in sp if e > 0)
    print(sp_new)

    # print(type(positive))
    # print(positive[0])
    # print(positive[1])