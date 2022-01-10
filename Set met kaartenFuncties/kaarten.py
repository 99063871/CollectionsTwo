import random

deck = ['Joker', 'Joker']
cards = ['Aas', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Boer', 'Dame', 'heer']

for b in range(len(cards)):#deze for loop zorgt ervoor dat alle kaarten er in gezet worden
    deck.append("Harten "+cards[b])
    deck.append("Ruiten "+cards[b])
    deck.append("Schoppen "+cards[b])
    deck.append("Klaveren "+cards[b])

random.shuffle(deck)#schud het deck

for a in range(7):
    print("Kaart",(a+1),":",deck[0])#print de bovenste 7 kaarten
    deck.remove(deck[0])#haalt de kaart weg nadat het geprint is

print("\ndeck (",len(deck),"kaarten:",deck)#print het overige deck