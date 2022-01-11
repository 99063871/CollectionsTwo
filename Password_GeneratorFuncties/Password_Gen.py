import random
import string

password = []

specialReeks = ["@", "#", "$", "%", "&", "_", "?"]

amountLetter = random.randint(2,6)
amountDigit = random.randint(4,7)

for a in range(amountLetter):
    password.append(random.choice(string.ascii_letters).upper())

for x in range(8, 20):
    password.append(random.choice(string.ascii_letters).lower())

for c in range(3):
    password.append(random.choice(specialReeks))

for c in range(amountDigit):
    password.append(random.choice(string.digits))

print(password)
random.shuffle(password)
print(password)