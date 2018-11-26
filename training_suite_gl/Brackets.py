

def checkio(s):
    open_b = ['{', '[', '(']

    close_b = ['}', ']', ')']

    dic_brackets = {'}': '{', ']': '[', ')': '('}

    brackets = []
    for i in s:
        if i in open_b:
            brackets.append(i)
            continue
        if i in close_b:
            if len(brackets) == 0:
                return False
            if dic_brackets.get(i) != brackets[len(brackets) - 1]:
                return False
            brackets.pop()
    return len(brackets) == 0



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"