import itertools


def is_stressful(subj):
    red = ["help", "asap", "urgent"]

    list_of_unclean_words = [''.join(chunk) for i, chunk in itertools.groupby(subj, key=lambda i: i.isalpha())]
    single_word = ''.join(x for x in subj if x.isalpha()).lower()
    list_of_clean_words = []
    for word in list_of_unclean_words:
        list_of_clean_words.append(''.join(chunk for chunk, _ in itertools.groupby(word)).lower())
    list_of_clean_words.append(single_word)

    is_urgent = check_for_red_word(list_of_clean_words, single_word, red)

    if subj.endswith('!!!'):
        return True
    elif subj.isupper():
        return True

    return is_urgent


def check_for_red_word(content_list, single_word, red_list):
    for word in red_list:
        if word in content_list or word in single_word:
            return True
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    assert is_stressful("UUUURGGGEEEEENT here") == True, "Third"
    assert is_stressful("h!e!l!p") == True, "Fourth"
    assert is_stressful("We need you A.S.A.P.!!") == True, "Fifth"
    assert is_stressful("Heeeeeey!!! I’m having so much fun!") == False, "Sixth"
    assert is_stressful("where are you?!!!!") == True, "Seventh"
    print('Done! Go Check it!')
