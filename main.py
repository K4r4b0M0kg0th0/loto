# main.py
from winning_numbers import powerball, winning_numbers_history
from check_numbers import check_numbers
from user_input import get_user_numbers

user_numbers = get_user_numbers()
winning_numbers = powerball()

print("Winning Numbers:", winning_numbers[0])
print("Powerball Number:", winning_numbers[1])

print(check_numbers(winning_numbers, user_numbers))
print("Winning numbers history:", winning_numbers_history)
