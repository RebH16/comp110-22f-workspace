"""Dictionary exercise tests."""

__author__ = "730568515"

from exercises.ex07.dictionary import invert, favorite_color, count


def test_invert_edge() -> None:
    """Tests an empty dict."""
    xs: dict[str, str] = {}
    assert invert(xs) == {}


def test_invert_normal() -> None:
    """Tests a normal dict."""
    xs: dict[str, str] = {"hello": "goodbye", "hi": "bye"}
    assert invert(xs) == {"goodbye": "hello", "bye": "hi"}


def test_invert_error() -> None:
    """Tests an error."""
    xs: dict[str, str] = {"hello": "goodbye", "hi": "goodbye"}
    assert invert(xs) == TypeError


def test_favorite_color_edge() -> None:
    """Tests an empty dict."""
    xs: dict[str, str] = {}
    assert favorite_color(xs) == ""


def test_favorite_color_normal() -> None:
    """Tests a normal dict."""
    xs: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(xs) == "blue"


def test_favorite_color_tie() -> None:
    """Tests a tie."""
    xs: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Rebecca": "yellow"}
    assert favorite_color(xs) == "yellow"


def test_count_edge() -> None:
    """Tests an empty list."""
    xs: list[str] = ()
    assert count(xs) == {}


def test_count_normal() -> None:
    """Tests a normal list."""
    xs: list[str] = ("Mark", "Anna", "Mark")
    assert count(xs) == {"Mark": 2, "Anna": 1}


def test_count_one() -> None:
    """Tests a list with one item."""
    xs: list[str] = ("Mark")
    assert count(xs) == {"Mark", 1}