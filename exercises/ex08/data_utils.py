"""Dictionary related utility functions."""

__author__ = "730568515"

# Define your functions below
from csv import DictReader
data: str = "../data/DictReader/nc_durham_2015_march_21_to_26.csv"

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a 'table'"""
    result: list[dict[str, str]] = []

    # Open the file
    file_handle = open(filename, "r", encoding="utf8")
    # Read the file
    csv_reader = DictReader(file_handle)
    # Close the file
    file_handle.close()
    return result

def column_values(table: list[dict[str, str]], column_name: str) -> list[str]:
    """Produces a column of the items who match the second parameter.""" 
    result: list[str] = {}
    for row in table:
        result.append(column_name)
    return result