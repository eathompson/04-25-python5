def is_flush(cards): #define a function that takes in a list of cards - don't need to specify in param that it's a list
    words = cards[0].split(' ') #divide first item into 3 words
    suit = words[2] #look at 2th item, aka 3rd word, the suit

    #look at everybody else to compare
    for card in cards:
        print("Looking at: "+card)
        if not card.endswith(suit):
            return False
    return True
     

result = is_flush(['5 of Clubs', '9 of Clubs', '8 of Clubs', 'Jack of Clubs', '2 of Clubs'])
print(result)