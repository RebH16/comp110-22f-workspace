"""Creating a fully formatted Wordle!"""

__author__ = "730568515"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
secret = "Codes"
#Part 1
def contains_char(searched_string, searched_character) -> bool: 
    """Searches for individual character in full string."""
    assert len(searched_character) == 1
    i = 0
    character_existance = False
    while i < len(searched_string):
        if searched_character == searched_string[i]:
            character_existance = True
            return character_existance
        i += 1
    return character_existance

def emojified(guess, secret) -> str:
    "Checks for letter correctness and outputs a yellow, white, or green emoji block"
    assert len(guess) == len (secret)
    i: int = 0
    emoji = ""
    while i < len(secret):
        if guess[i] == secret[i]:
            emoji += GREEN_BOX   
        elif contains_char(secret, guess[i]):
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
        i += 1
    return emoji
#def input_guess(expected_length) -> bool:
#    input(f"Enter a {len(secret)} character word: ")