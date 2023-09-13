import string
import random

characters = string.ascii_letters + string.digits
password_length = 15
password = ""

for index in range(password_length):
    password = password + random.choice(characters)

print(f"\nGenerated password: {password}\n")
