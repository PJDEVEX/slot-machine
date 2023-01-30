
# import python inbuit random lib to generate random numbers 
import random

# Global constants
# Maximum number of line in the slot game
MAX_LINES = 3
# Maximum and minimum amout player can bet on per line
MAX_BET = 200
MIN_BET = 1
# Number of rows and colomns of the slot machine
ROWS = 3
COLS = 3


# Symbols of the slot machine and their freaqancy
symbols_count = {
    "$": 2,
    "£": 4,
    "€": 6,
    "k": 8
}

# Value for winning each of symbol
symbol_value = {
    "$": 5,
    "£": 4,
    "€": 3,
    "k": 2
}


def check_winnings(columns, lines, bet, values):
    """
    deciding the winning of the bet
    if bet on one line, it is on topline
    if, on two lines, it is on top 2 lines
    if, on three lines, it is on all lins
    User cannot pick lines
    """
    winnings = 0
    winning_lines = []
    # check numbmer of lines
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            # Check the symbol of each column
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            # if all the symbol are the same, player wins
            # Cal how much a player win
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def slot_machine_spin(rows, cols, symbols):
    """
    Get slot machine to spin and randomly select
    symbols for each row and colomn
    """
    # add all they symbols to a all symbol list
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    # Randonly adding the symbols to each colomn
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    """
    Transposing symbols generated in spiining slot machine colomns 
    to rows and print them 
    """
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


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
        amount = input("What would you like to deposit? $ \n")
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
            f'Pleae enter the number of lines to bet on ("1-{MAX_LINES}") ? \n')
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
        amount = input("How much you would like to bet on each line? $ \n")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount


def spin(balance):
    """
    Repeating the algoritum of the application 
    as long as player would like to continue
    """
    lines = get_number_of_lines()
    while True:
        # call for the get bet fuction
        bet = get_bet()
        # callculate the total bet for the attempt
        total_bet = bet * lines

        # Check the sufficiancy of the available balance to contiune the game
        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}\n")

    slots = slot_machine_spin(ROWS, COLS, symbols_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    """
    Execute,
    1. deposit function
    2. check for the continuation of the game
    3. continue the game as player wishes to do so
    """
    # call for deposit function
    balance = deposit()
    while True:
        # Confirm the current blance
        print(f"Current balance is ${balance}")
        # letting the player decide on continuation of the game
        answer = input("Press enter to play (q to quit).\n")
        if answer == "q":
            print("Thanks for playing the game!")
            break
        # Indicating the balance as quit
        balance += spin(balance)

    print(f'Please collect your balance ${balance}.\n')


main()
