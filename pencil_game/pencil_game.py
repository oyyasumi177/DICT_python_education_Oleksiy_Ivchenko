import random

PLAYER = "John"
BOT = "Jack"
PLAYERS = [PLAYER, BOT]


def get_pencils():
    """Запитує та повертає коректну кількість олівців."""
    while True:
        value = input("How many pencils would you like to use:\n")
        if not value.isdigit():
            print("The number of pencils should be numeric")
            continue

        value = int(value)
        if value <= 0:
            print("The number of pencils should be positive")
            continue

        return value


def get_first_player():
    """Запитує ім'я першого гравця та перевіряє коректність."""
    while True:
        name = input(f"Who will be the first ({PLAYER}, {BOT}):\n")
        if name not in PLAYERS:
            print(f"Choose between '{PLAYER}' and '{BOT}'")
            continue
        return name


def get_player_move(pencils):
    """Повертає коректний хід гравця (1–3 олівці)."""
    while True:
        move = input()
        if move not in ["1", "2", "3"]:
            print("Possible values: '1', '2' or '3'")
            continue

        move = int(move)
        if move > pencils:
            print("Too many pencils were taken")
            continue

        return move


def get_bot_move(pencils):
    """
    Повертає хід бота за виграшною стратегією.
    Програшні позиції: 1, 5, 9, 13...
    """
    move = (pencils - 1) % 4
    if move == 0:
        return random.randint(1, min(3, pencils))
    return move


def main():
    """
    Основна логіка гри "Олівці".
    Гравець, який бере останній олівець, програє.
    """
    pencils = get_pencils()
    current_player = get_first_player()

    while pencils > 0:
        print("|" * pencils)
        print(f"{current_player}'s turn!")

        if current_player == BOT:
            taken = get_bot_move(pencils)
            print(taken)
        else:
            taken = get_player_move(pencils)

        pencils -= taken
        current_player = PLAYER if current_player == BOT else BOT

    print(f"{current_player} won!")

main()