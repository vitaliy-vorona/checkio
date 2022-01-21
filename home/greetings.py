names = "Mr__John_Smith, Ms__Samantha_Wolf,Mrs__Violetta_Ford,Mr__Duglas_Adams"


# Place solution in the following function (and remove this line):
def greet_people(names):
    names = names.replace("__", ". ")
    names = names.replace("_", " ")
    names = names.split(",")
    formatted_names = []
    for name in names:
        name = "Hello, " + name.lstrip()
        formatted_names.append(name)
        print(formatted_names)
    return formatted_names


print("\n".join(greet_people(names)))
