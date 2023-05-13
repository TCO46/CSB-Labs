uname = input("Username: ")
pwd = input("Password: ")
repwd = input("Repeat password: ")

if(pwd != repwd):
    print("Passwords not match. Please input again.")
elif(len(pwd) < 8):
    print("Invalid password. Please input again.")
elif(bool(char.isdigit() for char in pwd) != True):
    print("Invalid password. Please input again.")
else:
    email = input("Email: ")
    if(email.find("@") == -1 or email.find(".") == -1):
        print("Invalid email. Please input again.")
    elif(email.find(".") == -1 and email.find("@") == -1):
        print("Invalid email. Please input again.")
    else:
        print("Registered successfully.")

