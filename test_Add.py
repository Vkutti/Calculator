import pytest

from AddFunctions import adding

billy = 1
bob = 2
joe = 3
ven = 20
kat = 25


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (8000600, 6405006, 14405606),
    (billy, bob, 3),
    (billy, 5, 6),
    (ven, kat, 45),


])
def test_add(a, b, expected):
    assert adding(a, b) == expected


def test_add_high_school():
    assert adding(8000600, 6405006) == 14405606


def test_add_characters():
    return_val = adding(1, 2)
    print(type(return_val))
    assert return_val == 3


def test_add_variable():
    assert adding(billy, bob) == 3


def test_add_values_and_vars():
    assert adding(billy, 5) == 6


def test_add_chars_and_vars_and_values():
    my_answer = adding(joe, 30)
    print(type(my_answer))
    assert my_answer == 33


def test_add_chars_and_vars():
    my_answer = adding(joe, bob)
    print(type(my_answer))
    assert my_answer == 5







