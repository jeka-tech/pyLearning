
squares = (e ** 2 for e in range(0, 11, 2))

def squares_2():
    print("Generator working")
    for e in range(0, 11, 2):
        yield e ** 2
    return 100

gen = squares_2()
gen_2 = squares_2()
print(gen)
print(gen_2)


for i in gen:
    print(i)

print('='*20)

for i in gen_2:
    print(i)