import random


def random_number_generator(random_number_start_point, random_number_end_point):
    if random_number_end_point != random_number_start_point:
        return random.randrange(random_number_start_point, random_number_end_point)
    else:
        return random_number_start_point


random_number_start_point = 0
random_number_end_point = 100

while True:
    random_number = random_number_generator(random_number_start_point,
                                            random_number_end_point)
    user_info = input(
        f"My guess is {random_number}. Please give me info. (L:low , H:high, C: correct)").lower()
    if user_info == "c":
        print("Nice game")
        break
    elif user_info == "h":
        random_number_end_point = random_number-1

    elif user_info == "l":
        random_number_start_point = random_number+1
