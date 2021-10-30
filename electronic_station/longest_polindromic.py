def longest_palindromic(text):
    last_index = len(text)
    reduced = 0
    first_index = 0

    while True:
        sub_string = text[first_index:last_index]
        if sub_string == sub_string[::-1]:
            print(sub_string)
            return sub_string

        if last_index == len(text):
            reduced += 1
            last_index = len(text) - (reduced + 1)
            first_index = 0
            continue

        first_index += 1
        last_index += 1


if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
