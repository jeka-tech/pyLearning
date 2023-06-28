class NewException(Exception):
    pass

def divide(a,b):
    if a == 6 and b == 3:
        raise NewException('Коммент')
    return a/b

if __name__ == '__main__':

    print(divide(6, 3))
