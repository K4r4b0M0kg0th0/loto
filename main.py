# main.py
from winning_numbers import powerball, winning_numbers_history
from check_numbers import check_numbers
from user_input import get_user_numbers, saved_numbers

def main():
    use_saved = input("Do you want to use a saved set of numbers? (y/n): ")
    if use_saved.lower() == "y":
        if len(saved_numbers) == 0:
            print("There are no saved numbers.")
            user_numbers = get_user_numbers()
        else:
            print("Saved numbers:", saved_numbers)
            user_name = input("Enter the name of the saved set of numbers you want to use: ")
            if user_name in saved_numbers:
                user_numbers = saved_numbers[user_name]
            else:
                print("Invalid name.")
                user_numbers = get_user_numbers()
    else:
        user_numbers = get_user_numbers()
    winning_numbers = powerball()

    print("Winning Numbers:", winning_numbers[0])
    print("Powerball Number:", winning_numbers[1])
    print(check_numbers(winning_numbers, user_numbers))
    print("Winning numbers history:", winning_numbers_history)
    print("Saved numbers:", saved_numbers)

if __name__ == "__main__":
    main()