# Функция - полноправный объект или объект первого класса
# Присваиваем ее как объект, без скобок
# Внутренняя функция берет переменные из внешней
# имя = декоратор(имя)


def external(a):
    def inner(b):
        print(a+b)

    inner(3)
def example(func):
    print(f'{func.__name__}')

def decor(func):
    def wrap(first, second):
        print(f'{func.__name__} started')
        func(first, second)
        print(f'{func.__name__} finished')

    return wrap

@ decor
def summ(a, b):
    print('In progress..')
    print(a+b)

def decor_int(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError('Неверный тип')
        return func(*args)

    return wrapper

def decor_str(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, str):
                raise ValueError('Неверный тип')
        return func(*args)

    return wrapper

def typed(var_type):
    def real_decor(function):
        def wrapper(*args):
            for arg in args:
                if not isinstance(arg, var_type):
                    raise ValueError('Неверный тип')
            return function(*args)

        return wrapper
    return real_decor

@typed(int)
def calc(a,b,c):
    print(a+b+c)
@typed(str)
def convert(a,b):
    print(a+b)

if __name__ == '__main__':
    calc(1,2,3)
    convert('asd', 'fgh')