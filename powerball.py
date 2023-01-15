import random

def powerball():
    main_numbers = random.sample(range(1, 50), 5)
    powerball = random.randint(1, 20)
    return (main_numbers, powerball)

def check_numbers(winning_numbers, user_numbers):
    main_match = len(set(winning_numbers[0]).intersection(user_numbers[0]))
    if main_match == 5 and winning_numbers[1] == user_numbers[1]:
        return "Jackpot! You won the grand prize."
    elif main_match == 5:
        return "Congratulations! You won the second prize."
    elif main_match == 4 and winning_numbers[1] == user_numbers[1]:
        return "Congratulations! You won the third prize."
    elif main_match == 4 or (main_match == 3 and winning_numbers[1] == user_numbers[1]):
        return "Congratulations! You won a lower prize."
    else:
        return "Sorry, you did not win this time."