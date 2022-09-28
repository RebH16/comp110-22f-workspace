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
    """Combines two lists so that the second list is added to the first list"""
    first_list.append(second_list)
    return first_list

def sub(a_list: list[int], start_index: int, end_index: int) -> list:
    """Creates a new list from a portion of the original list"""
    list_start = a_list.pop[:end_index]
    list_end = a_list.pop[start_index:]
    full_list = list_start + list_end
    return full_list