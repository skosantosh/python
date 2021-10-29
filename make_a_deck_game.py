# make deck card and shuffle it
import random
cardfaces = []
suilts = ['Pan', 'Ita', 'Surath', 'Chid']
royals = ['J', 'Q', 'K', 'A']
deck = []

for i in range(2, 11):
    cardfaces.append(str(i))


for j in range(4):
    cardfaces.append(royals[j])

for s in range(4):
    for c in range(13):

        card = (cardfaces[c] + " of " + suilts[s])
        deck.append(card)
        print('Crd ' + " " + card)

# card = str((cardfaces[c]) + "of" + str(suilts[s])


random.shuffle(deck)

for m in range(52):
    mydeck = deck[m]
    print(f"{m} ko  {mydeck}")
