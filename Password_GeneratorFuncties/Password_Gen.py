import random
import string

password = []

amountLetter = random.randint(2,6)
for a in range(amountLetter):
    password.append(random.choice(string.ascii_letters).upper())

for x in range(8, 20):
    password.append(random.choice(string.ascii_letters).lower())
print(password)