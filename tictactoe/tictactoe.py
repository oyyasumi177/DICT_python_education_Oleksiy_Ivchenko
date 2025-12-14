def print_field(f):
    """
    Друкує ігрове поле у вигляді 3х3 з рамкою.
    """
    print("---------")
    print(f"| {f[0][0]} {f[0][1]} {f[0][2]} |")
    print(f"| {f[1][0]} {f[1][1]} {f[1][2]} |")
    print(f"| {f[2][0]} {f[2][1]} {f[2][2]} |")
    print("---------")


def check_state(f):
    """
    Перевіряє стан гри:
    повертає 'X', '0', 'draw' або 'not finished'.
    """

    for i in range(3):
        if f[i][0] == f[i][1] == f[i][2] != "_":
            return f[i][0]

    for j in range(3):
        if f[0][j] == f[1][j] == f[2][j] != "_":
            return f[0][j]

    if f[0][0] == f[1][1] == f[2][2] != "_":
        return f[0][0]

    if f[0][2] == f[1][1] == f[2][0] != "_":
        return f[0][2]

    for row in f:
        if "_" in row:
            return "not finished"

    return "draw"


def get_coordinates():
    """
    Зчитує та перевіряє координати,
    поки користувач не введе коректні.
    Повертає (row, col).
    """
    while True:
        coords = input("Enter the coordinates: ").split()

        if len(coords) != 2 or not (coords[0].isdigit() and coords[1].isdigit()):
            print("You should enter numbers!")
            continue

        x = int(coords[0])
        y = int(coords[1])

        if x < 1 or x > 3 or y < 1 or y > 3:
            print("Coordinates should be from 1 to 3!")
            continue

        row = 3 - y
        col = x - 1
        return row, col


def main():
    """
    Основна логіка гри:
    створює поле, перемикає гравців
    та перевіряє кінцевий стан.
    """
    field = [
        ["_", "_", "_"],
        ["_", "_", "_"],
        ["_", "_", "_"]
    ]

    print_field(field)
    current_player = "X"

    while True:
        row, col = get_coordinates()

        if field[row][col] != "_":
            print("This cell is occupied! Choose another one!")
            continue

        field[row][col] = current_player
        print_field(field)

        result = check_state(field)

        if result == "X":
            print("X wins")
            break
        elif result == "0":
            print("0 wins")
            break
        elif result == "draw":
            print("Draw")
            break

        if current_player == "X":
            current_player = "0"
        else:
            current_player = "X"


main()

