import string


def checkio(data):
    all_letters_dict = {}
    all_letters_keys = []

    for k in data:
        k = k.lower()
        # if k.isalpha():
        if k in all_letters_dict.keys():
                all_letters_dict[k] = all_letters_dict.get(k) + 1
        else:
                all_letters_dict[k] = 1

    temp_list = list(all_letters_dict.values())
    temp_list.sort()
    x = temp_list[len(temp_list)-1]

    for k, v in all_letters_dict.items():
        if v == x:
            all_letters_keys.append(k)
    all_letters_keys.sort()
    x = all_letters_keys[0]
    return x

def checkio_via_generator(text):
    #replace this for solution
    data={letter:text.lower().count(letter) for letter in list(string.ascii_lowercase)}
    return max(data,key=data.__getitem__)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(checkio("Hello World!"))
    assert checkio("Hello, World!") == "l", "Hello test"
    assert checkio_via_generator("How do you do?") == "o", "O is most wanted"
    assert checkio_via_generator("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio_via_generator("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")