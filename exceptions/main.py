class DenominatorEqualZeroError(Exception):
    '''Когда делитель равен нулю'''
    pass

class ArgumentNotIntegerError(Exception):
    '''Когда аргумент не целое число'''
    pass

def divide(a:int, b:int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ArgumentNotIntegerError("Not integer")
    if b == 0:
        raise DenominatorEqualZeroError("Divide by zero")
    return a // b

if __name__ == '__main__':
    try:
        result = divide(0, 0)
    except (ArgumentNotIntegerError, DenominatorEqualZeroError) as exe:
        print(exe)
    finally:
        print("Always")
