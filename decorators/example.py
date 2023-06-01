def typed(var_type):
    def decor(x):
        def wrapper(*args):
            for arg in args:
                if not isinstance(arg, var_type):
                    raise ValueError(f"Неверный тип. Должен быть {var_type}")
            x(*args)

        return wrapper
    return decor




@typed(int)
def summ (a,b):
    print(a+b)
@typed(str)
def conc (a,b):
    print(a+b)

if __name__ == '__main__':
    summ("1", "3")
