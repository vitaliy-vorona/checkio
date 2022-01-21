"""
Stephan and Sophia forget about security and use simple passwords for everything.
Help Nikola develop a password security check module.
The password will be considered strong enough if its length is greater than or equal to 10 symbols,
it has at least one digit, as well as containing one uppercase letter and one lowercase letter in it.
The password contains only ASCII latin letters or digits.
"""


def checkio(data):
    uppercase = False
    lowercase = False
    is_digit = False

    if len(data) >= 10 and len(data) <= 64:
        for i in data:
            if i.isdigit():
                is_digit = True
            if i.islower():
                lowercase = True
            if i.isupper():
                uppercase = True
        if uppercase and lowercase and is_digit:
            return True
    return False


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("A1213pokl") == False, "1st example"
    assert checkio("bAse730onE4") == True, "2nd example"
    assert checkio("asasasasasasasaas") == False, "3rd example"
    assert checkio("QWERTYqwerty") == False, "4th example"
    assert checkio("123456123456") == False, "5th example"
    assert checkio("ULFFunH8ni") == True, "6th example"
    assert checkio("QwErTy911poqqqq") == True, "7th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
