data = "   123 sd 34 as324 12 sdf34 asd231asd"


# That's how I would do it
def parse_digits_(data):
    _list = []
    _tmp = ""
    for i in data:
        if i.isdigit():
            _tmp += i
        elif (
            not i.isdigit()
            and len(_tmp) > 0
            or (i == len(data) - 1)
            and (len(_tmp) > 0)
        ):
            _list.append(int(_tmp))
            _tmp = ""
    return _list


# That's how I should do it
def parse_digits(data):
    import itertools

    return [
        int("".join(group))
        for is_chunk, group in itertools.groupby(data, key=lambda x: x.isdigit())
        if is_chunk
    ]


print(parse_digits("1sdafadf 2d fad34e 9234"))
print(parse_digits("A1 02BBB12sdfsdf Fg123 12 0001 45"))
print(parse_digits(data))
