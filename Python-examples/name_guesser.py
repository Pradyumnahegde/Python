my_name = "Prad".lower()

hints = 0

def enter_name():
    return input('Enter the name : ').lower()

while True :
    name = enter_name()
    if name != my_name:
        print("you can use hints ")   
        hints+=1 
        if hints == 1:
            print("Hint 1 : Starts with 'P' ")
        elif hints == 2:
            print("Hint 2 ; Its a 4 letter word and its has 'a' and 'r' in it")
        elif hints == 3:
            print("Hint 3 : ends with 'd'")
        elif hints > 3:
            print("you have run out of hints, try again later")
            break
    else:
        print("Congratulations! You guessed it right!")
        break
