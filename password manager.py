
pwd = input("What is the master password?")

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "Password:", passw)


def add():
    name = input("Account name: ")
    pwd = input("Password: ")


    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + '\n')



while True:
    mode = input("Would you like to view or add a password? ").lower()

    if mode == "q":
        break
    if mode == "view":
        view()

    elif mode == "add":
        add()

    else: 
        print("Invalid Mode!")