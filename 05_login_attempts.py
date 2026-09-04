# Simple login system with a maximum of 3 password attempts.
correct_password = "1234"

for attempt in range(1, 4):
    entered_password = input("Enter the password: ")
    if entered_password == correct_password:
        print("Login Successfully")
        break
    else:
        if attempt < 3:
            print("Try Again")
else:
    print("Account locked. Maximum attempts reached.")
