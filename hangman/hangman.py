import random


def get_random_word():
    """
    Повертає випадкове слово зі списку можливих слів.
    """
    words = ["python", "java", "javascript", "php"]
    return random.choice(words)


def validate_letter(letter, guessed):
    """
    Перевіряє введену літеру.

    Повертає кортеж (is_valid, error_message):
    - is_valid: True, якщо введення правильне
    - error_message: текст помилки, якщо введення некоректне
    """
    if len(letter) != 1:
        return False, "Потрібно ввести лише одну літеру"

    if not letter.isalpha() or not letter.islower():
        return False, "Введіть маленьку англійську літеру"

    if letter in guessed:
        return False, "Ви вже вводили цю літеру"

    return True, ""


def update_hint(choice, hint, letter):
    """
    Оновлює підказку, відкриваючи всі входження вгаданої літери.

    Повертає оновлений рядок підказки.
    """
    return "".join(
        letter if choice[i] == letter else hint[i]
        for i in range(len(choice))
    )


def play_game():
    """
    Основний ігровий цикл Hangman.

    Обробляє введення користувача, кількість спроб,
    відкриття літер та визначення перемоги чи поразки.
    """
    choice = get_random_word()
    hint = "-" * len(choice)
    attempts = 8
    guessed = set()

    print("HANGMAN")

    while attempts > 0:
        print(hint)
        letter = input("Input a letter: ")

        valid, error = validate_letter(letter, guessed)
        if not valid:
            print(error)
            continue

        guessed.add(letter)

        if letter not in choice:
            print("Такої літери немає у слові")
            attempts -= 1
            continue

        hint = update_hint(choice, hint, letter)

        if hint == choice:
            print("Ви відгадали слово!")
            print("Ви перемогли!")
            return

    print("Ви програли!")


def main():
    """
    Головне меню програми.

    Дозволяє користувачу почати гру або вийти з програми.
    """
    print("HANGMAN")
    while True:
        cmd = input('Введіть "play" для початку гри або "exit" для виходу: ')
        if cmd == "play":
            play_game()
        elif cmd == "exit":
            break


main()
