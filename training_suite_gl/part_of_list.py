test_data = ["az", "toto", "picaro", "zone", "kiwi"]


def partlist(list_):
    index = 1
    ll = []
    tmp_ll = []
    while index < len(list_):
        tmp_ll.append(" ".join([x for x in list_[:index]]))
        tmp_ll.append(" ".join([x for x in list_[index:]]))
        ll.append(tuple(tmp_ll))
        tmp_ll = []
        index += 1
    return ll


print(partlist(test_data))
