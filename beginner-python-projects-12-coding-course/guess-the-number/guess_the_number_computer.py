import random


def check(user_input):

    if user_input == random_number:
        print(
            f"Yes you did it.Your choise: {user_input}, Computer's choise: {random_number}")
        return False
    elif user_input < random_number:
        print("Çok düşük.")
        return True
    else:
        print("çok yüksek")
        return True


random_number = random.randrange(1, 10)
check_continue = True
while check_continue:
    user_input = int(input("Lütfen 1 ile 10 arasında bir sayı girin: \n"))
    check_continue = check(user_input)
