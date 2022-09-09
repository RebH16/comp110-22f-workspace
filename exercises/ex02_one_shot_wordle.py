"""This code will run one-shot wordl as an intermediary lesson befroe making full wordle!"""

__author__ = "730568515"
# while index < secret_len:
#    if user_guess[index] == secret_word[index]:
#        emoji += GREEN_BOX
#    else:
#        emoji += WHITE_BOX
#    index += 1
"""Variable Definitions"""
secret_word: str = "python"
secret_len: int = len(secret_word)
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
i = 0
user_guess: str = input(f"What is your {secret_len}-letter guess? ")
emoji: str = ""
guessed_character_existance = False
alternate_indices = 0

while len(user_guess) != secret_len:
    user_guess = input(f"That was not {secret_len} letters! Try again: ")

"""Emoji set-up"""
# while i < secret_len:
#    if user_guess[i] == secret_word[i]:
#        emoji += GREEN_BOX
#    while guessed_character_existance is not True and alternate_indices < secret_len:
#        if secret_word[alternate_indices] == user_guess[i]:
#            guessed_character_existance = True
#            emoji += YELLOW_BOX
#        else:
#            alternate_indices += 1
#    i += 1
#    if guessed_character_existance == False:
#        emoji += WHITE_BOX

while i < secret_len:
    if user_guess[i] == secret_word[i]:
        emoji += GREEN_BOX
    else:
        emoji += WHITE_BOX
    i += 1

print(emoji)

if user_guess == secret_word:
    print("Woo! You got it!")

if user_guess != secret_word and len(user_guess) == secret_len:
    print("Not quite. Play again soon!")
