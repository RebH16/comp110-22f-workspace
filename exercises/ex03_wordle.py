"""Creating a fully formatted Wordle!"""

__author__ = "730568515"

#Part 1
def contains_char(searched_string, searched_character) -> bool: 
    """Searches for individual character in full string."""
    assert len(searched_character) == 1
    if searched_character == searched_string:
        return True
    else:
        return False

