"""EX01: Chardle - A step toward Wordle."""

__author__ = "730568515"

"Part 1"

full_word: str = input("Enter a 5-character word: ")
if len(full_word) < 5:
    print("Error: Word must contain 5 characters")
    exit()
single_character: str = input("Enter a single character: ")
if len(single_character) > 1:
    print("Error: Character must be a single character.")
    exit()
if len(single_character) == 0:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + single_character + " in " + full_word)

character_count = 0

if full_word[0] == single_character:
    print(single_character + " found at index 0")
    character_count = character_count + 1
if full_word[1] == single_character:
    print(single_character + " found at index 1")
    character_count = character_count + 1
if full_word[2] == single_character:
    print(single_character + " found at index 2")
    character_count = character_count + 1
if full_word[3] == single_character:
    print(single_character + " found at index 3")
    character_count = character_count + 1
if full_word[4] == single_character:
    print(single_character + " found at index 4")
    character_count = character_count + 1

if character_count == 0:
    print("No instances of " + str(single_character) + " found in " + str(full_word))
if character_count == 1:
    print("1 instance of " + str(single_character) + " found in " + str(full_word))
if character_count == 2:
    print("2 instances of " + str(single_character) + " found in " + str(full_word))
if character_count == 3:
    print("3 instances of " + str(single_character) + " found in " + str(full_word))
if character_count == 4:
    print("4 instances of " + str(single_character) + " found in " + str(full_word))
if character_count == 5:
    print("5 instances of " + str(single_character) + " found in " + str(full_word))