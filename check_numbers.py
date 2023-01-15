def check_numbers(winning_numbers, user_numbers):
    main_match = set(winning_numbers[0]).intersection(user_numbers[0])
    match_count = len(main_match)
    powerball_match = winning_numbers[1] == user_numbers[1]

    if match_count == 5 and powerball_match:
        return "You won the grand prize!"
    elif match_count == 5 or (match_count == 4 and powerball_match) or (match_count == 3 and powerball_match):
        return "You won a prize!"
    else:
        return "Sorry, you did not win this time."