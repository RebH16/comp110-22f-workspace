"""This module contains tests for the utils module."""


__author__ = "730568515"


from exercises.ex05.utils import only_evens, sub, concat


"""Tests for only_evens."""


def test_only_evens_empty() -> None:
    """Tests for when the list is empty."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_only_evens() -> None:
    """Tests for when the list only contains evens."""
    xs: list[int] = [2, 4, 8, 10, 12]
    assert only_evens(xs) == xs


def test_only_evens_only_odds() -> None:
    """Tests for when the list only contains odds."""
    xs: list[int] = [3, 5, 7, 13, 15]
    assert only_evens(xs) == []


"""Tests for concat."""


def test_concat_empty() -> None:
    """Tests for when the lists are empty."""
    xs: list = []
    xl: list = []
    assert concat(xs, xl) == []


def test_concat_empty_full() -> None:
    """Tests for when one list is empty."""
    xs: list = []
    xl: list = [1, 2, 3, 4, 5]
    assert concat(xs, xl) == xl


def test_concat_full_full() -> None:
    """Tests for when both lists have contents."""
    xs: list = [1, 2, 3]
    xl: list = [4, 5, 6]
    assert concat(xs, xl) == xs + xl


"""Tests for sub."""


def test_sub_empty() -> None:
    """Tests for when the list is empty."""
    list: list = []
    xs: int = 0
    xl: int = 0
    assert sub(list, xs, xl) == []


def test_sub_negative_start() -> None:
    """Tests for when the start index is negative."""
    list: list = [0, 1, 2, 3, 4]
    xs: int = -2
    xl: int = 0
    assert sub(list, xs, xl) == []


def test_sub_big_end() -> None:
    """Tests for when the end index is larger than the list length."""
    list: list = [0, 1, 2, 3, 4]
    xs: int = 0
    xl: int = 10
    assert sub(list, xs, xl) == [0, 1, 2, 3, 4]