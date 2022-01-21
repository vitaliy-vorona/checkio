test_list = ["tsar", "rat", "tar", "star", "tars", "cheese"]


def group_anagrams(test_list):
    test_list = sorted(["".join(sorted(list(x))) for x in test_list])
    anagrams = []
    index_shift = 0
    len_test_list = len(test_list)
    while index_shift < len_test_list:
        anagram_count = test_list.count(test_list[0])
        anagrams.append([test_list[0]] * anagram_count)
        index_shift += anagram_count
        test_list = test_list[anagram_count:]
    return anagrams


def group_anagrams_(test_list):
    print(test_list)
    dic_test = {x: 1 for x in test_list}
    print(dic_test)
    # anagram = [dic_test[x] for v in test_list for x in test_list if ''.join(sorted(v)) == ''.join(sorted(x))]
    anagram = {
        x
        for v in test_list
        for x in test_list
        if "".join(sorted(v)) == "".join(sorted(x))
    }
    print(anagram)
    return anagram


print(group_anagrams_(test_list))
