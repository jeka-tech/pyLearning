# Функция - полноправный объект
# Функция может захватывать переменные из внешней функции

def logger(func):
    def wrapper(*args):
        print(f'{func.__name__} started')
        result = func(*args)
        print(f'{func.__name__} finished')
        return result

    return wrapper
@logger
def summ(a, b):
    return a + b

if __name__ == '__main__':

    # print(logger(summ)(2, 3))

    # summ = logger(summ)

    # function = logger(summ)
    # print(function(2, 3))

    print(summ(2, 3))
