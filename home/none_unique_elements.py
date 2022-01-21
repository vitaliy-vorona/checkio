def none_unique_numbers(data):
    non_unique_values = []
    for i in list(data):
        if list(data).count(i) > 1:
            non_unique_values.append(i)
    return non_unique_values


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(none_unique_numbers([1]), list), "The result must be a list"
    assert none_unique_numbers([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert none_unique_numbers([1, 2, 3, 4, 5]) == [], "2nd example"
    assert none_unique_numbers([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert none_unique_numbers([10, 9, 10, 10, 9, 8]) == [
        10,
        9,
        10,
        10,
        9,
    ], "4th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
