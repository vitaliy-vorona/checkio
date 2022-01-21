def popular_words(text, words):
    # your code here
    text = text.split()
    words_map = dict((k, 0) for k in words)
    for i in text:
        i = i.lower()
        if i in words_map.keys():
            words_map[i] += 1
    return words_map


p = popular_words("when I was bla bla bla and something else", ["bla", "I"])
print(p)
#
# if __name__ == '__main__':
#     # print("Example:")
# #     print(popular_words('''
# # When I was One
# # I had just begun
# # When I was Two
# # I was nearly new
# # ''', ['i', 'was', 'three', 'near']))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert popular_words('''
# When I was One
# I had just begun
# When I was Two
# I was nearly new
# ''', ['i', 'was', 'three', 'near']) == {
#         'i': 4,
#         'was': 3,
#         'three': 0,
#         'near': 0
#     }
#     print("Coding complete? Click 'Check' to earn cool rewards!")
