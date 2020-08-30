import pytest

from DivideFunctions import dividing

billy = 5
bob = 10
joe = 15
ven = 20
kat = 25


def test_add_elementary():
    assert dividing(1, 2) == 0.5


def test_add_high_school():
    assert dividing(8, 2) == 4


def test_add_characters():
    return_val = dividing(1, 2)
    print(type(return_val))
    assert return_val == 0.5


def test_add_variable():
    assert dividing(bob, billy) == 2


def test_add_values_and_vars():
    assert dividing(billy, 5) == 1


def test_add_chars_and_vars_and_values():
    my_answer = dividing(joe, 30)
    print(type(my_answer))
    assert my_answer == 0.5


def test_add_chars_and_vars():
    my_answer = dividing(ven, kat)
    print(type(my_answer))
    assert my_answer == 0.8
