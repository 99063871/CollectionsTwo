boodschappenlijst = {

}

a = 1

def boodschappenlijstFunc():
    item = input("Wat wilt u aan uw boodschappenlijstje toevoegen?")
    if item != "stop":
        amount = input("Hoeveel "+item+" wilt u toevoegen?")
        boodschappenlijst[item] = int(amount)
        boodschappenlijstFunc()
    else:
        dict.fromkeys(boodschappenlijst)
        print(boodschappenlijst)

boodschappenlijstFunc()