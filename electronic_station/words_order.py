def words_order(text: str, words: list) -> bool:
    # alternative best solution
    # text_words = {w for w in text.split(" ") if w in words}
    # return sorted(text_words, key=text.index) == words

    # check if dups in the words list
    if len(set(words)) != len(words):
        return False
    # iterate through the text and compare the words list order correctness
    for word in text.split(" "):
        if word in words and word != words[0]:
            return False
        if word not in words:
            continue
        else:
            words.pop(0)
            if len(words) == 0:
                return True
            continue
    return len(words) == 0


if __name__ == "__main__":
    print("Example:")
    # print(words_order("hi world im here", ["world", "here"]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert words_order("hi world im here", ["world", "here"]) == True
    assert words_order("hi world im here", ["here", "world"]) == False
    assert words_order("hi world im here", ["world"]) == True
    assert words_order("hi world im here", ["world", "here", "hi"]) == False
    assert words_order("hi world im here", ["world", "im", "here"]) == True
    assert words_order("hi world im here", ["world", "hi", "here"]) == False
    assert words_order("hi world im here", ["world", "world"]) == False
    assert words_order("hi world im here", ["country", "world"]) == False
    assert words_order("hi world im here", ["wo", "rld"]) == False
    assert words_order("", ["world", "here"]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
