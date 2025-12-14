import random


def get_number_of_friends():
    """
    Запитує у користувача кількість людей, що приєднаються до вечірки.
    Повертає введене число як int.
    """
    return int(input("Enter the number of friends joining (including you):\n"))


def get_friends_list(num):
    """
    Зчитує імена друзів і створює словник у форматі:
    {"Ivan": 0, "Anna": 0, ...}
    Повертає словник friends.
    """
    print("Enter the name of every friend (including you), each on a new line:")
    friends = {}

    for _ in range(num):
        name = input()
        friends[name] = 0

    return friends


def split_bill(total, count):
    """
    Повертає рівну частину рахунку:
    total / count, округлену до 2 знаків.
    """
    return round(total / count, 2)


def choose_lucky(friends):
    """
    Вибирає випадкове ім’я серед ключів словника friends.
    Повертає ім’я lucky.
    """
    lucky = random.choice(list(friends.keys()))
    print(f"{lucky} is the lucky one!")
    return lucky


def recalculate_with_lucky(friends, total, lucky):
    """
    Перераховує суму для кожного друга, враховуючи lucky:
    lucky платить 0, інші ділять total між (n - 1).
    Повертає оновлений словник friends.
    """
    num_people = len(friends) - 1
    new_split = round(total / num_people, 2)

    for person in friends:
        friends[person] = 0 if person == lucky else new_split

    return friends


def main():
    """
    Основна логіка програми поділу витрат:
    - зчитування кількості людей
    - зчитування імен
    - поділ суми
    - опціональний вибір lucky
    - перерахунок суми при необхідності
    """
    num = get_number_of_friends()

    if num <= 0:
        print("No one is joining for the party")
        return

    friends = get_friends_list(num)

    total = int(input("Enter the total amount:\n"))
    split = split_bill(total, num)

    for person in friends:
        friends[person] = split

    answer = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')

    if answer == "Yes":
        lucky = choose_lucky(friends)
        friends = recalculate_with_lucky(friends, total, lucky)
        print(friends)
    else:
        print("No one is going to be lucky")
        print(friends)

main()

