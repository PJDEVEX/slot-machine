

# Global constants
# Maximum number of line in the slot game
MAX_LINES = 3
# Maximum and minimum amout player can bet on per line
MAX_BET = 200
MIN_BET = 1


def deposit():
    """
    Function to accept deposits for the game from the users
    It allows to,
    1. Accept deposits
    2. Ensure amounts are equal or greater than $1 and multiples of
    ones
    3. The value entered is a digit.
    """
    while True:
        amount = input("What would you like to deposit? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount


def get_number_of_lines():
    """
    To know number of lines a player would like to bet on
    1. it is within 1-3 (can change if needed)
    2. ensure it is a number
    3. continue to request untill get vaild response
    """
    while True:
        lines = input(
            f'Pleae enter the number of lines to bet on ("1-{MAX_LINES}") ? ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    """
    Getting bets from the player per line
    """
    while True:
        amount = input("What would you like to bet on each line? $ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount


def main():
    """
    Execute all the function of the programe
    """
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    print(balance, lines, bet)


main()
