"""Maximising Pythons built in language with lists."""

__author__ = "730568515"

def all(num_list: list[int], num: int) -> bool:
    i: int = 0
    while i <= len(num_list) - 1:
        if num_list[i] != num: 
            return False
        i += 1
    else:
        return True

def max(input: list[int]) -> int:
    i: int = 0
    max_value: int = 0
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    while i < len(input):
        if max_value < input[i]:
            max_value = input[i]
        i += 1
    return max_value

def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    i: int = 0
    true_condition: int = 0
    while i < len(list_one):
        if list_one[i] == list_two[i]:
            true_condition += 1
        i += 1
    if true_condition == len(list_one):
        true_condition = True
    else:
        true_condition = False
    return true_condition