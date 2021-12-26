boodschappenlijst = {

}

def boodschappenlijstFunc():
    item = input("Wat wilt u aan uw boodschappenlijstje toevoegen?").strip()
    if item != "stop":
        amount = input("Hoeveel "+item+" wilt u toevoegen?").strip()
        boodschappenlijst[item] = int(amount)
        boodschappenlijstFunc()
    else:
        dict.fromkeys(boodschappenlijst)
        print(boodschappenlijst)

boodschappenlijstFunc()