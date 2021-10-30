#TODO has to be reworked since abc == cba however it's not anagram

def is_anagram(str1, str2):
    str1_list = sorted([x.lower() for x in str1])
    str2_list = sorted([x.lower() for x in str2])
    return str1_list == str2_list

print(is_anagram("AbbA", "BBaA"))  # True
