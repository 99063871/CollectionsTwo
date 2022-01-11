import random
import string

password = []

amountLetter = random.randint(2,6)
for a in range(amountLetter):
    password.append(random.choice(string.ascii_letters).upper())
print(password)