import random
import time

while True:
    print("Which level do you want? Enter a number:")
    print("1 - simple operations with numbers 2-9")
    print("2 - integral squares of 11-29")
    level_input = input("> ")
    if level_input in ["1", "2"]:
        level = int(level_input)
        break
    print("Incorrect format.")

correct_answers = 0
questions_count = 0
start_time = time.time()

while questions_count < 5:
    if level == 1:
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        op = random.choice(['+', '-', '*'])
        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        else:
            result = a * b
        print(f"{a} {op} {b}")
    else:
        a = random.randint(11, 29)
        result = a ** 2
        print(a)

    while True:
        try:
            answer = int(input("> "))
            if answer == result:
                print("Right!")
                correct_answers += 1
            else:
                print("Wrong!")
            questions_count += 1
            break
        except ValueError:
            print("Incorrect format.")

end_time = time.time()
total_time = round(end_time - start_time, 1)

print(f"Your mark is {correct_answers}/5. Time taken: {total_time} seconds.")
print("Would you like to save the result? Enter yes or no.")
save_choice = input("> ").lower()

if save_choice in ["yes", "y"]:
    name = input("What is your name? ")

    if level == 1:
        desc = "simple operations with numbers 2-9"
    else:
        desc = "integral squares of 11-29"

    f = open("results.txt", "a")
    f.write(f"{name}: {correct_answers}/5 in level {level} ({desc}). Time: {total_time}s\n")
    f.close()
    print('The results are saved in "results.txt".')