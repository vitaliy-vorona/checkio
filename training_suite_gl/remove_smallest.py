from random import choice

tests = [
    ([1, 2, 3, 4, 5], [2, 3, 4, 5]),
    ([5, 4, 1, 3], [5, 4, 3]),
    ([1, 2, 1], [2, 1]),
]


def remove_smallest_classic(list_):
    min_ = list_[0]
    index_min_ = 0
    list_ = list_.copy()
    for i, v in enumerate(list_):
        if v < min_:
            min_ = v
            index_min_ = i
    list_.remove(list_[index_min_])
    return list_


def remove_smallest(list_):
    list_ = list_.copy()
    list_.remove(min(list_))
    return list_


for test in tests:
    result = remove_smallest(test[0])
    print(result)
    assert result == test[1], "Wrong :("
    assert result is not test[0], "You can't change original list"


def func(a, b, c=2):
    return a + b + c


print(func(20, b=13, c=10))
