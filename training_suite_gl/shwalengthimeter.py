test_strings = ["kawabunga", "metro2013", "moon", "orange"]


def shwalengthimeter(test_strings):
    vowels = ("a", "e", "o", "i", "u", "y")

    formatted_strings = ['{}{} {}'.format('shwa', string[2:], str(len(string))) if string[1] in vowels else
                        '{}{} {}'.format('shwa', string[1:], str(len(string))) for string in test_strings]

    return formatted_strings


print(shwalengthimeter(test_strings))
