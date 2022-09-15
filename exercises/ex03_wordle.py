"""Creating a fully formatted Wordle!"""

__author__ = "730568515"

from mimetypes import guess_all_extensions


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
secret: str = "codes"

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

#Part 2
def emojified(guess, secret) -> str:
    "Checks for letter correctness and outputs a yellow, white, or green emoji block."
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

#Part 3
def input_guess(expected_length) -> str:
    """Ensuring a logical guess as the input."""
    user_guess = input(f"Enter a {expected_length} character word: ")
    while len(user_guess) != expected_length:
        user_guess = input(f"That was not {expected_length} chars! Try again: ") 
    return user_guess

#Part 4
def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn_number : int = 1
    guess: str = ""
    while turn_number <= 6 and secret != guess:
        print(f"=== Turn {turn_number}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        turn_number += 1 
    if secret == guess:
        print(f"You won in {turn_number - 1}/6 turns!")
    if secret != guess and turn_number > 6:
        print("X/6 - Sorry, try again tomorrow!")

#Allows the code to run as a module
if __name__ == "__main__":
    main()