import os
import random


def validate_pwd(pwd):
    x = [
        x for x in list(pwd) if str(x).isdigit() or str(x).isupper() or str(x).islower()
    ]
    return len(x) == len(pwd) and 3 < len(x) < 20


def fib():
    a = 1
    b = 1

    for i in range(10):
        yield b
        # a, b = b, a + b
        a = b
        b = a + b


counter = 0
for i in fib():
    print(i)
    counter += 1
    if counter == 10:
        break

res = [ord(x) for x in "test"]
x = list(map((lambda x: x ** 2), filter((lambda x: x % 2 == 0), range(10))))
print(x)

l_ = [1, 2, 3, 4, 5]
ll_ = l_[:-1:]

print(os.getcwd())
