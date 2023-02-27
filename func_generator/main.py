
squares = (e ** 2 for e in range(0, 11, 2))

def squares_2():
    print("Generator working")
    for e in range(0, 11, 2):
        yield e ** 2
    return 100

def pause():
    print("Generator working")
    while True:
        print(a)
        yield a

a = 10
gen = pause()
print(next(gen))
a = 20
print(next(gen))

# for i in gen:
#     print(i)
#
# print('='*20)
#
# for i in gen_2:
#     print(i)