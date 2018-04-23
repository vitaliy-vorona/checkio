def popular_words(text, words):
    # your code here
    text = text.split()
    text_map = dict((k, 0)for k in words)
    for k in text:
        k = k.lower()
        if k in text_map.keys():
            text_map[k] = text_map[k]+1
    print(text_map)
    return text_map


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")