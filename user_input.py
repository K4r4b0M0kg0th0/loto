def get_user_numbers():
    user_input = input("Enter your 5 main numbers separated by commas: ")
    user_numbers_list = [int(i) for i in user_input.split(",")]
    if (len(user_numbers_list) != 5) or any(i < 1 or i > 50 for i in user_numbers_list):
        raise ValueError("Invalid input. Please enter 5 numbers between 1 and 50 separated by commas.")
    user_powerball = int(input("Enter your Powerball number: "))
    if user_powerball < 1 or user_powerball > 20:
        raise ValueError("Invalid input. Please enter a number between 1 and 20.")
    user_numbers = (user_numbers_list, user_powerball)
    return user_numbers
