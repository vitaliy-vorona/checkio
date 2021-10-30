import re


def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    # classic
    index = 0
    for index in range(len(text)):
        if text[index].isalpha():
            text = text[index:]
            break

    for index in range(len(text)):
        if text[index].isalpha() or text[index] == "'":
            continue
        else:
            break

    if index == len(text)-1:
        return text[:index+1]
    return text[:index]

def first_word_2(text: str) -> str:
    #With pattern and comprehension list
    string_with_no_punctuations = re.split(r'[ ,.]', text)
    print("string_with_no_punctuations ", string_with_no_punctuations)
    text = [str for str in string_with_no_punctuations if str != ""]
    return text[0]




if __name__ == '__main__':
        print("Example:")
        print(first_word("Hello world"))

        # These "asserts" are used for self-checking and not for an auto-testing
        assert first_word("Hello world") == "Hello"
        assert first_word(" a word ") == "a"
        assert first_word("don't touch it") == "don't"
        assert first_word("greetings, friends") == "greetings"
        assert first_word("... and so on ...") == "and"
        assert first_word("hi") == "hi"

        assert first_word_2("Hello world") == "Hello"
        assert first_word_2(" a word ") == "a"
        assert first_word_2("don't touch it") == "don't"
        assert first_word_2("greetings, friends") == "greetings"
        assert first_word_2("... and so on ...") == "and"
        assert first_word_2("hi") == "hi"
        print("Coding complete? Click 'Check' to earn cool rewards!")
