print("Hello! My name is Ivchenko_Bot")
print("I was created in 2025")
print("Please, remind me your name")
name = input()
print("What a great name you have, " + name + "!")
print("Let me guess your name")
print("Enter remainders of dividing your age by 3, 5 and 7.")
age1 = int(input())
age2 = int(input())
age3 = int(input())
age = (age1 * 70 + age2 * 21 + age3 * 15) % 105
print("Your age is " + str(age) + "; that's a good time to start programming!")
print("Now I will prove to you that I can count any number you want.")
number = int(input())
for i in range(number + 1):
    print(f"{i} !")
print("Let's test your programming knowledge.")
print("What programming language do we use?")
print("1. java")
print("2. python")
print("3. c++")
print("4. c#")

while True:
    answer = int(input())
    if answer == 2:
        break
    else: print("Please, try again.")
print("Congratulations, have a nice day!")
print("Completed, have a nice day!")