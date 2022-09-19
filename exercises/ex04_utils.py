"""Maximising Pythons built in language with lists."""

__author__ = "730568515"

def all(num_list: list[int], num: int) -> bool:
    i: int = 0
    truth_check: int = 0
    while i <= len(num_list) - 1:
        if num_list[i] == num:
            truth_check += 1    
        i += 1
    if truth_check == len(num_list) - 1:
        return True
    else:
        return False