import builtins
print(dir(builtins))

open = 'global'
# max = 10
def outer():
    open = 'encoled'

    def inner():
        open = 'local'
        print(open)
        print(max([1,2,3]))

    inner()

if __name__ == '__main__':
    outer()