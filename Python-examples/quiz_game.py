print("Welcome to quiz game")

playing = input("Do you want to play the game : ")

if playing.lower() != "yes" :
    quit()

print("Okay lets play")
score = 0

answer = input("whats does www stand for : ")
if answer.lower() == "world wide web":
    print("Correct answer")
    score+=1
else :
    print("Incorrect")

answer = input("Whats the name of value 3.14 : ")
if answer.lower() == "pi":
    print("Correct")
    score+=1
else:
    print("Incorrect")

answer = input("Whats the sweetest fruit : ")
if answer.lower() == "mango":
    print("Correct")
    score+=1
else:
    print("Incorrect")

print("You got " + str(score) + "score")
print("Congratulations you got " + str((score/3) * 100) + "%")