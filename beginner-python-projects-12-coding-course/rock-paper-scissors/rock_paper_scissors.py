import random


def check(user_input):
    if not user_input in rps:
        user_input = check(input(
            "Please dont push without r p s keyword. \n Choice your rps: Rock (r), Paper (p), Scissors (s) \n").lower())
    return user_input


user_continue = True
count_win = 0
rps = ["r", "p", "s"]
while user_continue:
    user_choice = check(
        input("Choice your rps: Rock (r), Paper (p), Scissors (s) \n").lower())
    computer_choice = random.choice(rps)
    if user_choice == "p":
        if computer_choice == "p":
            print("we draw.")
        elif computer_choice == "s":
            print(f"you are loser. computer choice {computer_choice}")
        else:
            count_win += 1
            print(f"You win.  computer choice {computer_choice}")
    elif user_choice == "s":
        if computer_choice == "s":
            print("we draw.")
        elif computer_choice == "r":
            print(f"you are loser.  computer choice {computer_choice}")
        else:
            count_win += 1
            print(f"You win.  computer choice {computer_choice}")
    elif user_choice == "r":
        if computer_choice == "r":
            print(f"we draw.  computer choice {computer_choice}")
        elif computer_choice == "p":
            print(f"you are loser.  computer choice {computer_choice}")
        else:
            count_win += 1
            print(f"You win. computer choice {computer_choice}")
    if input("Contunie game: Yes (y) or No (n)").lower() == "n":
        print(f"Thanks for games. You win count {count_win}")
        user_continue = False
