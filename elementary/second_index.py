def second_index(text: str, symbol: str):
    """
        returns the second index of a symbol in a given text
    """
    # your code here
    first_index = text.find(symbol)
    second_index = text[first_index + 1:].find(symbol)
    if second_index == -1:
        return None
    return first_index + second_index + 1


if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "d") is None, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')
