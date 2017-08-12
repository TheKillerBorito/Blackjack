from random import *
from tkinter import *

global cards
global top

top = Tk()
top.title = "Blackjack"

#region DeckSetup
deckImage = []
cards = 0
for i in range(1,53):
    deckImage.append(i)
hearts = [1,2,3,4,5,6,7,8,9,10,10,10,10]
spades = [1,2,3,4,5,6,7,8,9,10,10,10,10]
diamonds = [1,2,3,4,5,6,7,8,9,10,10,10,10]
clubs = [1,2,3,4,5,6,7,8,9,10,10,10,10]
deck = hearts+spades+diamonds+clubs
zipDeck = list(zip(deckImage, deck))
shuffle(zipDeck)
dealer_hand = []
player_hand = []
#endregion
#region Functions
def handTotal(hand):
    total = 0
    hand.sort(reverse=True)
    for i in hand:
        if i == 1:
            ace = int(input("You have an ace, do you want it to be an 11 or 1?: "))
            if ace == 11:
                i = 11
        total += i
    return total
def compHandTotal(hand, ptotal):
    total = 0
    hand.sort(reverse=True)
    for i in hand:
        if i == 1:
            total1 = total + 1
            total11 = total + 11
            if total1 < 21 and total11 > 21:
                i = 1
            elif total11 > ptotal and total11 < 21:
                i = 11
            elif total11 == 21:
                i = 11
            else:
                i = 1
            print(i)
        total += i
    return total
def handPrint(hand):
    hand.sort(reverse = True)
    for i in hand:
        print(i)
def handAdd(hand,deck):
    hand.append(deck[0])
    del deck[0]
    return deck, hand
def totalCheck(player_total, dealer_total):
    if dealer_total > 21:
        print("YOU WIN")
    if player_total == 21:
        print('you win')
    elif dealer_total == 21:
        if player_total == 21:
            print("YOU WIN")
        else:
            print("YOU LOSE")
    elif player_total > dealer_total and (player_total < 21 and dealer_total < 21):
        print("YOU WIN")
    elif player_total == dealer_total:
        print("You win")
    else:
        print("YOU LOSE")
def dealerDraw(dhand, ptotal, d):
    print("DEALER HAND")
    handPrint(dealer_hand)
    dtotal = compHandTotal(dealer_hand, player_total)
    print("DEALER TOTAL")
    print(dtotal)
    while dtotal < 17:
        d, dhand = handAdd(dhand, d)
        print("NEW DEAL HAND")
        handPrint(dealer_hand)
        dtotal = compHandTotal(dealer_hand, player_total)
        print("DEALER NEW TOTAL")
        print(dtotal)
    totalCheck(ptotal, dtotal)
    return dhand, ptotal, d

def newImage(zipDeck):
    global cards
    global top
    if cards == 0:
        image_name1 = str(zipDeck[0][0])+".gif"
        file1 = PhotoImage(file = image_name1)
        label1 = Label(top, image = file1)
        label1.place(x=0, y=0)
        cards += 1
    if cards == 1:
        image_name2 = str(zipDeck[0][0])+".gif"
        file2 = PhotoImage(file=image_name2)
        label2 = Label(top, image=file2)
        label2.place(x=100, y=0)
        cards += 1


#endregion
#region Program

C = Canvas(top,height = 250, width = 250)

while True:
    if len(player_hand) <2:
        player_hand.append(zipDeck[0][1])
        image_name = str(zipDeck[0][0]) + ".gif"
        print(image_name)
        del zipDeck[0]
    if len(dealer_hand) < 2:
        dealer_hand.append(zipDeck[0][1])
        del zipDeck[0]
    if cards == 1:
        print("HERE1")
        #image_name1 = str(zipDeck[0][0])+".gif"
        file1 = PhotoImage(file = image_name)
        label1 = Label(top, image =file1)
        label1.place(x=0,y=0)
        C.pack()
    if cards == 2:
        print("HERE2")
        #image_name2 = str(zipDeck[0][0])+".gif"
        file2 = PhotoImage(file=image_name)
        label2 = Label(top, image=file2)
        label2.place(x=100, y=0)
        cards += 1
        C.pack()
    if len(dealer_hand) == 2 and len(player_hand) == 2:
        break
handPrint(player_hand)
player_total = handTotal(player_hand)
print('Dealers Hand')
print(dealer_hand[0])
print("?")
while True:
    hit = input("Would you like a new card?(y/n): ").lower()
    if hit == 'y':
        deck, player_hand = handAdd(player_hand, deck)
        print("NEW HAND")
        handPrint(player_hand)
        player_total = handTotal(player_hand)
        if len(player_hand) == 5 and player_total < 21:
            print("FIVE CARDS IN HAND WITHOUT GOING BUST, YOU WIN!!!")
            break
        if player_total > 21:
            dealerDraw(dealer_hand, player_total, deck)
            break
    else:
        #player_total = handTotal(player_hand)
        dealerDraw(dealer_hand, player_total, deck)
        break
#endregion

top.mainloop()
