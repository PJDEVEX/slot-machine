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
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount


deposit()