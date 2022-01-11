import random
import string

string.ascii_letters
string.digits
string.punctuation

randomletter = random.choice(string.ascii_letters)
randomletterC = random.choice(string.ascii_letters).upper()
randomdigit = random.choice(string.digits)
randomspecial = random.choice(string.punctuation)
print(randomletter)
print(randomletterC)
print(randomdigit)
print(randomspecial)