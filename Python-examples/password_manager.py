
password = input("Enter the password : ")


def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("Username : " + user + ",\tPassword : " + passw)


def reset():
    name = input("Account name = ")
    new_password = input("Password = ")

    with open('password.txt', 'a') as f:  # with open is file operation where the with keyword opens and closes file automatically after the operation is over without using f.close() , also a is append and as f is name of file ie f
        # files have 'w' , 'a', 'r' write append read operations
        f.write(name + "|" + new_password + "\n")


while True:
    check = input(
        "Do u want to view or reset the password.Enter q to exit : ").lower()

    if check == "q":
        quit()
    if check == "view":
        view()
    elif check == "reset":
        reset()
    else:
        print("Invalid option")
        continue
