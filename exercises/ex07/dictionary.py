
"""Dictionary exercise."""

__author__ = "730568515"


def main() -> None:
    """Main function."""
    invert()
    favorite_color()
    count()


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and items in a dictionary."""
    inverted_dict = {dictionary[key]: key for key in dictionary}
    return inverted_dict


def favorite_color(colors: dict[str, str]) -> str:
    """Counts what color appears the most frequently."""
    values = list(colors.values())
    most_common_color: str = max(set(values), key=values.count)
    return most_common_color


def count(input_list: list[str]) -> dict[str, int]:
    """Counts what value is the most frequent in the given dictionary."""
    dictionary_count: dict[str, int] = {}
    for item in input_list:
        if item in dictionary_count:
            dictionary_count[item] += 1
        else:
            dictionary_count[item] = 1
    return dictionary_count