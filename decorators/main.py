# Функция - полноправный объект или объект первого класса

# Внутренняя функция может захватывать переменные из внешней функции
def logger(func):
    def wrapper(*args):
        print("start")
        result = func(*args)
        print("stop")
        return result

    return wrapper

@ logger
def summ(a, b):
    return a + b





if __name__ == '__main__':
    print(summ(2,5))
