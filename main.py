import random

def powerball():
    # Generate 5 random numbers between 1 and 50
    main_numbers = random.sample(range(1, 50), 5)

    # Generate 1 random number between 1 and 20 for the Powerball
    powerball_number = random.randint(1, 20)

    return main_numbers, powerball_number

def check_numbers(winning_numbers, user_numbers):
    # Check main numbers
    main_match = set(winning_numbers[0]).intersection(user_numbers[0])
    match_count = len(main_match)
    
    # Check Powerball
    powerball_match = winning_numbers[1] == user_numbers[1]

    if match_count == 5 and powerball_match:
        return "You won the grand prize!"
    elif match_count == 5 or (match_count == 4 and powerball_match) or (match_count == 3 and powerball_match):
        return "You won a prize!"
    else:
        return "Sorry, you did not win this time."
    
while True:
    try:
        user_input = input("Enter your 5 main numbers separated by commas: ")
        user_numbers_list = [int(i) for i in user_input.split(",")]
        if (len(user_numbers_list) != 5) or any(i < 1 or i > 50 for i in user_numbers_list):
            raise ValueError("Invalid input. Please enter 5 numbers between 1 and 50 separated by commas.")
        break
    except ValueError as e:
        print(e)
        
while True:
    try:
        user_powerball = int(input("Enter your Powerball number: "))
        if user_powerball < 1 or user_powerball > 20:
            raise ValueError("Invalid input. Please enter a number between 1 and 20.")
        break
    except ValueError as e:
        print(e)

user_numbers = (user_numbers_list, user_powerball)
winning_numbers = powerball()
print("Winning Numbers:", winning_numbers[0])
print("Powerball Number:", winning_numbers[1])

print(check_numbers(winning_numbers, user_numbers))
