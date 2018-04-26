def checkio(expression):
    dic_of_brackets = {']': '[', ')': '(', '}': '{'}
    open_brackets = ['[', '(', '{']
    close_brackets = [']', ')', '}']
    list_of_brackets = []

    for i in expression:
        if i in open_brackets:
            list_of_brackets.append(i)
        elif i in close_brackets:
            bracket = dic_of_brackets.get(i)
            if len(list_of_brackets) == 0:
                return False
            if list_of_brackets[len(list_of_brackets) - 1] != bracket:
                return False
            list_of_brackets.pop(-1)
    return len(list_of_brackets) == 0

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
