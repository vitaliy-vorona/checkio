# def filter_numbers(start_range, end_range):
#     l_ = list(filter(lambda x: x % 3 == 0, range(start_range, end_range)))
#     return l_
#
# print(filter_numbers(3000, 3010))
import functools

print(
    list(
        map(
            lambda x, y: str(x) + y,
            range(11)[::-1],
            ["a", "b", "c", "d", "e", "f", "g", "h", "i"],
        )
    )
)
print((9 * 1223))


def sum2(x, y, z):
    return x + y + z


import random as RND
from operator import mul

fnx = lambda: RND.randint(0, 10)
data = [(fnx(), fnx()) for c in range(2)]
target = (2, 4)

print(functools.reduce(lambda x, y: x * y, range(1, 6)))
print(functools.reduce(mul, range(1, 6)))
print(sum(i * i for i in range(1, 6)))


def pluser():
    val = 0
    while True:
        val = (yield val) + 1


p = pluser()
print(p.send())
