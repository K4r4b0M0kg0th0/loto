# winning_numbers.py
import random
winning_numbers_history = []

def powerball():
    main_numbers = random.sample(range(1, 50), 5)
    powerball_number = random.randint(1, 20)
    winning_numbers_history.append((main_numbers, powerball_number))
    return main_numbers, powerball_number

__all__ = ['winning_numbers_history']
