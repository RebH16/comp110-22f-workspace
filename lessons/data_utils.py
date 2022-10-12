"""Some helpful utility functions for working with CSV files."""

from csv import DictReader

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