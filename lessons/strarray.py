"""Examples of "vectorized" opertaions via magic methods."""

from __future__ import annotations
from typing import Union

class StrArray:
    items: list[str]

    def __init__(self, items: list[str]):
        self.items = items

    def __repr__(self) -> str:
        return f"StrArray({self.items})"
    
    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        result: StrArray = StrArray([])
        if isinstance(rhs, str):
        # 1. Loop through every item in a self's items list
            for item in self.items:
                result.items.append(item + rhs)
        # 2. Concatenate the rhs paramenter
            # item += rhs
        # 3. Append the concatenated string to results' itmes list attribute
            # result.items.append(item)
        else:
            # Loop through each index of self's items
            # Concatenate the corresponding value of rhs's items at same index
            # Append the resulting string to result's items list
            assert len(self.items) == len(rhs.items)
            for i in range(len(self.items)):
                result.items.append(self.items[i] + rhs.items[i])
        return result
    

a: StrArray = StrArray(["Armando", "Pete", "Leaky"])
#             StrArray(['Armando', 'Pete', 'Leaky'])
b: StrArray = StrArray(["Bacot", "Nance", "Black"])
print(a)
print(a + "!")
print(a + " " + b)