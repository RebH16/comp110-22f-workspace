"""Maximising Pythons built in language with lists."""

__author__ = "730568515"


def all(num_list: list[int], num: int) -> bool:
    """Shows if the numbers in a list are all equal to a specific number."""
    i: int = 0
    if len(num_list) == 0:
        return False
    while i <= len(num_list) - 1:
        if num_list[i] != num: 
            return False
        i += 1
    else:
        return True


def max(input: list[int]) -> int:
    """Finds the largest number in a list."""
    i: int = 0
    max_value: int = input[0]
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    while i < len(input):
        if max_value < input[i]:
            max_value = input[i]
        i += 1
    return max_value


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """Assess if two lists are exactly the same."""
    i: int = 0
    true_condition: int = 0
    bool_condition: bool = True
    if len(list_one) != len(list_two):
        return False
    while i < len(list_one):
        if list_one[i] == list_two[i]:
            true_condition += 1
        i += 1
    if true_condition == len(list_one):
        bool_condition = True
    else:
        bool_condition = False
    return bool_condition