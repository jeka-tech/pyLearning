# *args - собирает все позиционные аргументы
# **kwargs - собирает все keyworg аргументы в словарь

a, *b, c = 'abcd'

def example(d, e, f):
    print(d)
    print(e)
    print(f)

def my_print(*args, **kwargs):
    print(f'Got keyword arguments {kwargs}')
    for arg in args:
        print(str(arg), **kwargs)

if __name__ == '__main__':
    # print(f'{a=}')
    # print(f'{b=}')
    # print(f'{c=}')
    # example(1, 3, f=5)
    my_print(1,2,3,4, sep=':', end='_')