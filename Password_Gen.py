import random
import string

def createpassword(length):
    character = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(character) for i in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the length of your password: "))
    password = createpassword(password_length)
    print("The Generated Password:", password)