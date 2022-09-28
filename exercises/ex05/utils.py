"""This module contains 3 functions that adapt lists."""


__author__ = "730568515"


def only_evens(list: list[int]) -> list:
    """Takes in a list and makes a list with only even numbers from that initial list."""
    i: int = 0
    even_list: list[int] = [] 
    while i < len(list):
        if list[i] % 2 == 0:
            even_list.append(list[i])
        i += 1
    return even_list


def concat(first_list: list[int], second_list: list[int]) -> list:
    """Combines two lists so that the second list is added to the first list."""
    combined_list: list = []
    i: int = 0
    while i < len(first_list):
        combined_list.append(first_list[i])
        i += 1
    i = 0
    while i < len(second_list):
        combined_list.append(second_list[i])
        i += 1
    return combined_list


def sub(a_list: list[int], start_index: int, end_index: int) -> list:
    """Creates a new list from a portion of the original list."""
    i: int = start_index
    y: int = end_index
    new_list: list = []
    if i < 0:
        i = 0
    if i > len(a_list) or y <= 0:
        return []
    if y >= len(a_list):
        y = len(a_list)
    while i < y:
        new_list.append(a_list[i])
        i += 1
    return new_list