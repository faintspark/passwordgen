import random
import string

pool = string.ascii_letters + string.digits + string.punctuation

while True:
    length = input("Enter password length(Type 'quit' to exit): ")

    if length == "quit":
        break
    if not length.isdigit():
        print("enter a proper number")
        continue

    length = int(length)
    password = ""

    for i in range(length):
        password += random.choice(pool)

    print(f"Your password is: {password}")