import random

num = input("Type a number : ")

if num.isdigit():
    num = int(num)

    if num <=0:
        print("Enter number larger than 0")
        quit()
else:
    print("enter number next time")
    quit()

random_number = random.randint(1,num)

guess = 0

while True:
    guess+=1
    guess_num = input("Guess the number : ")

    if guess_num.isdigit():
        guess_num = int(guess_num)

    else: 
        print("Enter a number next time")
        continue

    if guess_num == random_number:
        print("Correct")
        break
    elif guess_num > random_number:
        print("Youre above the number")
    else :
        print("You are below the number")

print("you got it in", guess, "guesses")