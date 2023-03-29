
# list-comprehensions -> listcomps
# generator-expressions -> genexp
# Синтаксис одинаковый, но в genexp используются круглые скобки
# Отличие big_numbers = [e for e in range(100000)]

text = 'First second : third 12345'
elements = text.split()
Elements = [e.capitalize() for e in elements if "th" in e]
ints = [-3, 6, 0, -2, 7, 9]
positive = [e for e in ints if e > 0]

if __name__ == '__main__':
    big_numbers = [e for e in range(10_000_000)]
    print(big_numbers.__len__())
