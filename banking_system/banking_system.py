import random
import sqlite3


def luhn_check(card_num):
    if not card_num.isdigit() or len(card_num) != 16:
        return False
    check_sum = 0
    for i in range(16):
        digit = int(card_num[i])
        if (i + 1) % 2 != 0:
            digit = digit * 2
            if digit > 9:
                digit = digit - 9
        check_sum = check_sum + digit
    return check_sum % 10 == 0


conn = sqlite3.connect("card.s3db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS card (id INTEGER PRIMARY KEY, number TEXT, pin TEXT, balance INTEGER DEFAULT 0)")
conn.commit()

while True:
    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit")

    choice = input("> ").strip()
    print("")

    if choice == "1":
        bin_num = "400000"

        while True:
            account_id = ""
            for i in range(9):
                account_id = account_id + str(random.randint(0, 9))

            checksum = str(random.randint(0, 9))
            card_number = bin_num + account_id + checksum

            if luhn_check(card_number):
                break

        pin = ""
        for i in range(4):
            pin = pin + str(random.randint(0, 9))

        cursor.execute("INSERT INTO card (number, pin) VALUES (?, ?)", (card_number, pin))
        conn.commit()

        print("Your card has been created")
        print("Your card number:")
        print(card_number)
        print("Your card PIN:")
        print(pin)
        print("")

    elif choice == "2":
        print("Enter your card number:")
        input_card = input("> ").strip()
        print("Enter your PIN:")
        input_pin = input("> ").strip()
        print("")

        if luhn_check(input_card):
            cursor.execute("SELECT pin, balance FROM card WHERE number = ?", (input_card,))
            row = cursor.fetchone()

            if row is not None and row[0] == input_pin:
                print("You have successfully logged in!")
                print("")

                logged_in = True
                while logged_in:
                    print("1. Balance")
                    print("2. Add income")
                    print("3. Do transfer")
                    print("4. Close account")
                    print("5. Log out")
                    print("0. Exit")

                    sub_choice = input("> ").strip()
                    print("")

                    if sub_choice == "1":
                        cursor.execute("SELECT balance FROM card WHERE number = ?", (input_card,))
                        current_balance = cursor.fetchone()[0]
                        print("Balance: " + str(current_balance))
                        print("")

                    elif sub_choice == "2":
                        print("Enter income:")
                        income = int(input("> ").strip())
                        cursor.execute("UPDATE card SET balance = balance + ? WHERE number = ?", (income, input_card))
                        conn.commit()
                        print("Income was added!")
                        print("")

                    elif sub_choice == "3":
                        print("Transfer")
                        print("Enter card number:")
                        target_card = input("> ").strip()

                        if target_card == input_card:
                            print("You can't transfer money to the same account!")
                            print("")
                            continue

                        if not luhn_check(target_card):
                            print("Probably you made a mistake in the card number. Please try again!")
                            print("")
                            continue

                        cursor.execute("SELECT id FROM card WHERE number = ?", (target_card,))
                        target_row = cursor.fetchone()

                        if target_row is None:
                            print("Such a card does not exist.")
                            print("")
                            continue

                        print("Enter how much money you want to transfer:")
                        transfer_amount = int(input("> ").strip())

                        cursor.execute("SELECT balance FROM card WHERE number = ?", (input_card,))
                        my_balance = cursor.fetchone()[0]

                        if transfer_amount > my_balance:
                            print("Not enough money!")
                            print("")
                        else:
                            cursor.execute("UPDATE card SET balance = balance - ? WHERE number = ?", (transfer_amount, input_card))
                            cursor.execute("UPDATE card SET balance = balance + ? WHERE number = ?", (transfer_amount, target_card))
                            conn.commit()
                            print("Success!")
                            print("")

                    elif sub_choice == "4":
                        cursor.execute("DELETE FROM card WHERE number = ?", (input_card,))
                        conn.commit()
                        print("The account has been closed!")
                        print("")
                        logged_in = False

                    elif sub_choice == "5":
                        print("You have successfully logged out!")
                        print("")
                        logged_in = False

                    elif sub_choice == "0":
                        print("Bye!")
                        conn.close()
                        exit()
            else:
                print("Wrong card number or PIN!")
                print("")
        else:
            print("Wrong card number or PIN!")
            print("")

    elif choice == "0":
        print("Bye!")
        conn.close()
        break