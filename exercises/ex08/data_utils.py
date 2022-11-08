"""Dictionary related utility functions."""

__author__ = "730568515"

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produces a list[str] of all values in a signle column.""" 
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Reads the top of a table."""
    result: dict[str, list[str]] = {}
    if N > len(table):
        N = len(table)
    for column in table:
        first_values: list[str] = []
        i: int = 0
        for i in range(N):
            first_values.append(table[column][i])
        result[column] = first_values
    return result


def select(table: dict[str, list[str]], column_copy: list[str]) -> dict[str, list[str]]:
    """Looks at select columns of data."""
    result: dict[str, list[str]] = {}
    for column in column_copy:
        result[column] = table[column]
    return result


def concat(table_one: dict[str, list[str]], table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two tables."""
    result: dict[str, list[str]] = {}
    for column in table_one:
        result[column] = table_one[column]
    for column in table_two:
        if column in table_one:
            result[column] = table_one[column] + table_two[column]
        else:
            result[column] = table_two[column]
    return result
        

def count(list: list[str]) -> dict[str, int]:
    """Counts items."""
    result: dict[str, int] = {}
    i: int = 0
    while i < len(list):
        if list[i] in result:
            result[list[i]] += 1
        else:
            result[list[i]] = 1
        i += 1
    return result