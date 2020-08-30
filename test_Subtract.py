import pytest

from SubtractFunctions import subtracting

john = 5
dylan = 6
mike = 7
ven = 100
kat = 150


def test_add_elementary():
    assert subtracting(1, 2) == -1


def test_add_high_school():
    assert subtracting(8000600, 6405006) == 1595594


def test_add_characters():
    return_val = subtracting(1, 2)
    print(type(return_val))
    assert return_val == -1


def test_add_variable():
    assert subtracting(john, mike) == -2


def test_add_values_and_vars():
    assert subtracting(john, 5) == 0


def test_add_chars_and_vars_and_values():
    my_answer = subtracting(mike, 30)
    print(type(my_answer))
    assert my_answer == -23


def test_add_chars_and_vars():
    my_answer = subtracting(ven, kat)
    print(type(my_answer))
    assert my_answer == -50










