import sqlite3
from db import create_tables, add_user, add_numbers, add_history
from user_input import get_user_numbers
from powerball import powerball, check_numbers

# Create tables in the database
create_tables()

# Get user information
user_name = input("Enter your name: ")
user_email = input("Enter your email: ")
user_password = input("Enter your password: ")

# Add user to the users table
add_user(user_name, user_email, user_password)

# Connect to the database
conn = sqlite3.connect("powerball.db")
c = conn.cursor()

# Get user_id based on the user's email
c.execute("SELECT id FROM users WHERE email = ?", (user_email,))
user_id = c.fetchone()[0]

conn.close()

# Get user's numbers or generate random numbers
user_choice = input("Enter 1 to choose your numbers or 2 to generate random numbers: ")
if user_choice == "1":
    user_numbers = get_user_numbers()
else:
    user_numbers = powerball()

# Add user's numbers to the numbers table
add_numbers(user_id, user_numbers[0], user_numbers[1])

# Generate winning numbers
winning_numbers = powerball()

# Add winning numbers to the history table
add_history(winning_numbers[0], winning_numbers[1], '2022-01-01')

# Check if user won
result = check_numbers(winning_numbers, user_numbers)
print(result)
