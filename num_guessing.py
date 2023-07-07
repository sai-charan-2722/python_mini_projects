import random

z = int(input("Enter the top range: "))
x = random.randint(0, z)
guesses = 0
while True:
    guesses += 1
    y = int(input("Enter a number: "))
    if x == y:
        print("your guess is correct")
        break
    else:
        if y > x:
            print("Try a smaller number!")
        else:
            print("Try a greater number!")
print("You got it Correct in", guesses, "guesses")
