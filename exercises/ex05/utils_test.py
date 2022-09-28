__author__ = "730568515"

"""Tests for only_evens."""
from exercises.ex05.utils import only_evens

def test_only_evens_empty() -> None:
    xs: list[int] = []
    assert only_evens(xs) == []

def test_only_evens_only_evens() -> None:
    xs: list[int] = [2, 4, 8, 10, 12]
    assert only_evens(xs) == xs

def test_only_evens_only_odds() -> None:
    xs: list[int] = [3, 5, 7, 13, 15]
    assert only_evens(xs) == []

"""Tests for concat."""
from exercises.ex05.utils import concat

def test_concat_empty() -> None:
    xs: list = []
    xl: list = []
    assert concat(xs, xl) == [[]]

def test_concat_empty_full() -> None:
    xs: list = []
    xl: list = [1, 2, 3, 4, 5]
    assert concat(xs, xl) == [xl]

def test_concat_full_full() -> None:
    xs: list = [1, 2, 3]
    xl: list = [4, 5, 6]
    assert concat(xs, xl) == [xs + [xl]]