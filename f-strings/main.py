text = "hello world"

print(f"{text:^15}")

number = 1234567890
print(f"{number:,}")

number = 123
print(f"{number:08}")



from string import Template
x, y = "Hello", "World"
print(f"{x} {y}")  # 39.6 nsec per loop - Быстро!
print(x + " " + y)  # 43.5 nsec per loop
print(" ".join((x, y)))  # 58.1 nsec per loop
print("%s %s" % (x, y))  # 103 nsec per loop
print("{} {}".format(x, y))  # 141 nsec per loop
print(Template("$x $y").substitute(x=x, y=y))  # 1.24 usec per loop - Медленно!

width = 8
precision = 4
value = 42.12345
print(f"output: {value:{width}.{precision}}")

x = 10
y = 25
print(f"x = {x}, y = {y}")
print(f"{x = }, {y = }")  # (3.8+)

print(f"{x = :.3f}")


