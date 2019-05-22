"""
A virtual vending machine.
"""
# A list of coins allowed
ACCEPTABLE_COINS = [200, 100, 25, 10, 5]

def insert_coin(coin, inserted_coins):
    """
    Accepts a coin and appends it to inserted_coins list.
    """
    if coin not in ACCEPTABLE_COINS:
        raise ValueError
    inserted_coins.append(coin)


def return_change(balance):
    """
    Returns balance in coins.
    """
    change = []
    while balance:
        for coin in ACCEPTABLE_COINS:
            if balance % coin == 0:
                change.append(coin)
                balance -= coin
                break

    return sorted(change, reverse=True)


class InsufficientFunds(Exception):
    """
    Exception used to indicate that there isn't
    enough money to make a purchase.
    """
