"""Choose your own adventure main file."""

author = "730568515"

player: str = ""
toy_name: str = ""
points: int = 0
happiness_points: int = 0
xp: int = points
from random import randint

def main() -> None:
    points: int = 0
    greet()
    menu()

def greet() -> None:
    print(f"Welcome to Tamagotchi Caretaker! In this game you will accumuate happiness points by playing with your tamagotchi, you can then spend these for food which will increase your tamagotchis xp.")
    global player
    global toy_name
    player = input("What is your name? ")
    toy_name = input("What would you like to name your tamagotchi? ")

def menu() -> None:
    global toy_name
    global player
    global happiness_points
    user_choice = input(f"Would you like to: \n A) Play with {toy_name} \n B) Feed {toy_name} \n C) Leave the game \n")
    if user_choice == "A" or user_choice == "a":
        play()
    elif user_choice == "B" or user_choice == "b":
        feed(happiness_points)
    elif user_choice == "C" or user_choice == "c":
        game_over(points)
    else:
        print("Sorry that was not an option, try again:")
        menu()

def play() -> None:
    global toy_name
    global player
    global happiness_points
    guess: str = input(f"Excellent choice! Your tamagotchi is excited to play with you! {toy_name} is thinking of a number between 1 and 10. What number do you think it is {player}?\n")
    num: str = str(randint(1,10))
    if guess == num:
        print(f"Good job! You guessed {toy_name}'s number! 5 points has been added to your happiness tally and you will now be returned to the menu.")
        happiness_points += 5
        menu()
    else:
        print(f"I'm sorry that guess was incorrect, the number was {num}. 1 point was added to your happiness tally. You will now be returned to the menu.")
        happiness_points += 1
        menu()

def feed(points) -> int:
    global happiness_points
    xp: int = 0
    print(f"Hello {player}, {toy_name} is excited to eat! Here you can exchange happiness points for food to increase your tamagotchis xp. You have {happiness_points} happiness points")
    order = input("What would you like: \n A: Apple (10xp for 1 happiness point) \n B: Broccoli (50xp for 5 happinss points) \n C: Chocolate Cake (100xp for 8 happiness points)")
    if order == "A" and happiness_points >= 1:
        happiness_points = happiness_points - 1
        xp += 10
        print(f"Excellent choice, your xp is now {xp} and you have {happiness_points} happiness points, you will be returned to the menu.")
        menu()
    elif order == "B" and happiness_points >= 5:
        happiness_points = happiness_points - 5
        xp += 50
        print(f"Excellent choice, your xp is now {xp} and you have {happiness_points} happiness points, you will be returned to the menu.")
        menu()
    elif order == "C" and happiness_points >= 8:
        happiness_points = happiness_points - 8
        xp += 100
        print(f"Excellent choice, your xp is now {xp} and you have {happiness_points} happiness points, you will be returned to the menu.")
        menu()
    else:
        print("Sorry, that was not an option or you could not afford that food. You will be returned to the menu.")
        menu()
    xp = points
    return points

def game_over(points) -> None:
    print(f"Thank you for playing! You ended the game with {points} xp. Play again soon!")

if __name__ == "__main__":
    main()