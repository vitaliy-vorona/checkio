# count all elements in the list in recursive manner


def checkio(massiv):
    if len(massiv) == 0:
        return 0
    else:
        return massiv[0] + checkio(massiv[1:])
