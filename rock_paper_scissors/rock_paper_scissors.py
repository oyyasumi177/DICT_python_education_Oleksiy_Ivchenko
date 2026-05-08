import random

name = input("Enter your name: ")
print(f"Hello, {name}")

rating = 0
try:
    f = open("rating.txt", "r")
    for line in f:
        data = line.split()
        if data[0] == name:
            rating = int(data[1])
    f.close()
except FileNotFoundError:
    pass

inp_options = input("> ").strip()
if inp_options == "":
    options = ["rock", "paper", "scissors"]
else:
    options = [opt.strip() for opt in inp_options.split(",")]

print("Okay, let's start")

while True:
    user_input = input("> ").strip()

    if user_input == "!exit":
        print("Bye!")
        break

    if user_input == "!rating":
        print(f"Your rating: {rating}")
        continue

    if user_input not in options:
        print("Invalid input")
        continue

    computer_choice = random.choice(options)

    if user_input == computer_choice:
        print(f"There is a draw ({computer_choice})")
        rating += 50
    else:
        user_idx = options.index(user_input)
        reordered = options[user_idx + 1:] + options[:user_idx]

        half = len(reordered) // 2
        losers = reordered[half:]

        if computer_choice in losers:
            print(f"Well done. The computer chose {computer_choice} and failed")
            rating += 100
        else:
            print(f"Sorry, but the computer chose {computer_choice}")