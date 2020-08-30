import pytest

from MultiplayFunctions import multiplying

billy = 5
bob = 10
joe = 15
ven = 20
kat = 25


def test_add_elementary():
    assert multiplying(1, 2) == 2


def test_add_high_school():
    assert multiplying(8000600, 6405006) == 51243891003600


def test_add_characters():
    return_val = multiplying(1, 2)
    print(type(return_val))
    assert return_val == 2


def test_add_variable():
    assert multiplying(billy, bob) == 50


def test_add_values_and_vars():
    assert multiplying(billy, 5) == 25


def test_add_chars_and_vars_and_values():
    my_answer = multiplying(joe, 30)
    print(type(my_answer))
    assert my_answer == 450


def test_add_chars_and_vars():
    my_answer = multiplying(ven, kat)
    my_answer2 = multiplying(billy, joe)
    print(type(my_answer))
    print(type(my_answer2))
    assert my_answer * my_answer2 == 37500
