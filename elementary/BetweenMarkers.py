def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # your code here
    first_marker = text.find(begin)
    second_marker = text.find(end)

    if first_marker == -1 and second_marker != -1:
        return text[:second_marker]
    if second_marker == -1 and first_marker != -1:
        return text[text.find(begin) + len(begin):]
    if first_marker and second_marker == -1:
        return text
    if first_marker or second_marker != -1:
        return text[text.find(begin) + len(begin):second_marker]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    assert between_markers("Never send a human to do a machine's job.", "Never", "do") == " send a human to "
