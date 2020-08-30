def adding(a, b):
    type1 = type(a)
    type2 = type(b)
    if type1 is not int:
        raise TypeError('The First Value must be an Number. Instead it is ' + str(type1))

    if type2 is not int:
        raise TypeError('The Second Value must be an Number. Instead it is ' + str(type2))

    return a + b



