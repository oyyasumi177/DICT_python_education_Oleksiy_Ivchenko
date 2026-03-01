class CoffeeMachine:
    """Клас для симуляції роботи кавомашини."""

    def __init__(self):
        """Ініціалізація початкових запасів кавомашини."""
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

    def show_remaining(self):
        """Виводить поточний стан ресурсів у консоль."""
        print("\nThe coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")

    def check_resources(self, w_need, m_need, b_need):
        """Перевіряє, чи достатньо інгредієнтів для приготування кави."""
        if self.water < w_need:
            print("Sorry, not enough water!")
            return False
        if self.milk < m_need:
            print("Sorry, not enough milk!")
            return False
        if self.beans < b_need:
            print("Sorry, not enough coffee beans!")
            return False
        if self.cups < 1:
            print("Sorry, not enough disposable cups!")
            return False
        return True

    def buy(self):
        """Обробляє процес купівлі обраного напою."""
        print("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        choice = input("> ")

        if choice == "back":
            return

        if choice == "1":
            if self.check_resources(250, 0, 16):
                print("I have enough resources, making you a coffee!")
                self.water -= 250
                self.beans -= 16
                self.money += 4
                self.cups -= 1
        elif choice == "2":
            if self.check_resources(350, 75, 20):
                print("I have enough resources, making you a coffee!")
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.money += 7
                self.cups -= 1
        elif choice == "3":
            if self.check_resources(200, 100, 12):
                print("I have enough resources, making you a coffee!")
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.money += 6
                self.cups -= 1

    def fill(self):
        """Додає вказану користувачем кількість ресурсів до машини."""
        self.water += int(input("Write how many ml of water do you want to add:\n> "))
        self.milk += int(input("Write how many ml of milk do you want to add:\n> "))
        self.beans += int(input("Write how many grams of coffee beans do you want to add:\n> "))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:\n> "))

    def take(self):
        """Видає всі накопичені гроші та обнуляє баланс."""
        print(f"I gave you {self.money}")
        self.money = 0

    def start(self):
        """Запускає головний цикл взаємодії з користувачем."""
        while True:
            print("\nWrite action (buy, fill, take, remaining, exit):")
            action = input("> ")

            if action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.show_remaining()
            elif action == "exit":
                break


coffee_machine = CoffeeMachine()
coffee_machine.start()