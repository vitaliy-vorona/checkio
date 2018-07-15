data = "   123 sd 34 as324 12 sdf34 asd231asd"


def parse_digits(data):
    _list = []
    _tmp = ''
    for i, v in enumerate(data):
        if v.isdigit():
            _tmp += v
            print(v)
        if not v.isdigit() and len(_tmp) > 0 or (i == len(data)-1) and (len(_tmp) > 0):
            _list.append(int(_tmp))
            _tmp = ''
    return _list



print(parse_digits('1sdafadf 2d fad34e 9234'))
print(parse_digits('A1 02BBB12sdfsdf Fg123 12 0001 45'))
print(parse_digits(data))
