def adding(a, b):

    if a is None:
        return b
    if b is None:
        return a

    type1 = type(a)
    type2 = type(b)

    acceptable_types = [int, float, complex]

    check_type(acceptable_types, type1, 'First')
    check_type(acceptable_types, type2, 'Second')

    return a + b


def check_type(acceptable_types, type, foo):
    if type not in acceptable_types:
        raise TypeError(f'{foo} input parameter must be an int. Instead it is {str(type)}')



