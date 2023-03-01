# global и nonlocal нужны только для изменения значений (т.е. для чтения они не нужны)
# global может создать переменную, nonlocal не может
# nonlocal ищет только во внешних скоупах, но не в глобальных
# try not to use global and non-local

counter = 100

def increment():
    counter = 0

    def inner1():
        def inner():
            nonlocal counter
            counter = 1
            print(counter)

        inner()
    inner1()

if __name__ == '__main__':
    increment()