import random
import string

password = []

specialReeks = ["@", "#", "$", "%", "&", "_", "?"]

amountLetter = random.randint(2,6)#kiest een random getal tussen 2 en 6
amountDigit = random.randint(4,7)#kiest een random getal tussen 4 en 7

for a in range(amountLetter):#deze loop pakt een random hoofdletter
    password.append(random.choice(string.ascii_letters).upper())

for c in range(3):#deze loop pakt 3 random tekens uit de specialReeks
    password.append(random.choice(specialReeks))

for c in range(amountDigit):#deze loop pakt random getallen
    password.append(random.choice(string.digits))

amountLetterL = 24 - len(password)#dit berekend hoeveel er nog bij moet om op 24 te komen
for x in range(amountLetterL):#deze loop pakt random kleine letters
    password.append(random.choice(string.ascii_letters).lower())
random.shuffle(password)#dit schud de list

def checkFunc():#deze function checkt of op 1,2,3 of de laatste een str zijn, als dat niet het geval is word er opnieuw geschud en gecheckt, als het klopt word het geprint
    strcheck1 = password[0].isalpha()
    strcheck2 = password[1].isalpha()
    strcheck3 = password[2].isalpha()
    strcheckLast = password[23].isalpha()

    if strcheck1 == False or strcheck2 == False or strcheck3 == False or strcheckLast == False:
        random.shuffle(password)
        checkFunc()
    else:
        print(password)

checkFunc()