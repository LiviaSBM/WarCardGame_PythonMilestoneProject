#Milestone Project of Python Bootcamp - From zero to hero
#War Card Game

#Definition of cards' suits, ranks and values for further hierarchy settings:
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card:
    #Class for setting up all cards with their suits, ranks and values
    def __init__(self,suit,rank):
        self.suit = suit #Card's suit
        self.rank = rank #Card's rank
        self.value = values[rank] #Card's values
       
    def __str__(self):
        return self.rank+" of "+self.suit #Print card name (i.e: Three of Hearts)

class Deck:
    def __init__(self):
        
        self.all_cards = [] #Main deck (all cards) - empty object
        self.deckp1 = []    #Player 1 Deck
        self.deckp2 = []    #Player 2 Deck
        
        for item1 in suits:
            for item2 in ranks:
                self.all_cards.append(Card(item1,item2)) #Creating main deck
    
    def shuffleanddivide(self):
        
        random.shuffle(self.all_cards) #Shuffling the cards
     
        while len(self.all_cards)>0:
            #While there's cards within the main deck, allocate 1 for P1 and another for P2
            self.deckp1.append(self.all_cards.pop(0))
            self.deckp2.append(self.all_cards.pop(-1))
        
        return [self.deckp1, self.deckp2] #Return deck of P1 and P2

getbothdecks = Deck()
deckjogadores = getbothdecks.shuffleanddivide()


class CardsOnTable:
    def __init__(self,deck01,deck02):
        self.deck01 = deckjogadores[0] #Player 1 deck
        self.deck02 = deckjogadores[1] #Player 2 deck
        self.tabledeck = [] #Epty tab;r deck
                
    def cardsontable(self):
        self.tabledeck.append(self.deck01.pop(-1)) #Adding 1 card from P1 to Table Deck
        self.tabledeck.append(self.deck02.pop(-1)) #Adding 2 card from P1 to Table Deck
        
        return self.tabledeck, self.deck01, self.deck02 

teste1 = CardsOnTable(deckjogadores[0],deckjogadores[1])
teste1importacao = teste1.cardsontable()

class GameTurn:
    def __init__(self,cardp1,cardp2,deckjogador1,deckjogador2):
        self.cardp1, self.cardp2 = teste1importacao[0] 
        self.deckjogador1 = teste1importacao[1]
        self.deckjogador2 = teste1importacao[2]
        self.tempdecktable = [] #Cards left on table
        
        
    def cardcomparison(self):
        #Creating variables to get the rank of each card
        splitc1 = str(self.cardp1)
        splitc2 = str(self.cardp2)
        splitc1 = splitc1.split()
        splitc2 = splitc2.split()
        
        #Below, we compare both cards. The one with the highest rank wins
        if values[splitc1[0]]>values[splitc2[0]]:
            
            self.deckjogador1.append(self.cardp1)
            self.deckjogador1.append(self.cardp2)
            self.deckjogador1.extend(self.tempdecktable)
            self.tempdecktable = []
            
            return self.deckjogador1, self.deckjogador2
        
        elif values[splitc1[0]]<values[splitc2[0]]:
            self.deckjogador2.append(self.cardp1)
            self.deckjogador2.append(self.cardp2)
            self.deckjogador1.extend(self.tempdecktable)
            self.tempdecktable = []
            
            return self.deckjogador1, self.deckjogador2
            #If both cards are even, they're added to the table desk and cumulated 
            #to the next round
        else:
            self.tempdecktable.append(self.cardp1)
            self.tempdecktable.append(self.cardp2)
            
            return self.deckjogador1, self.deckjogador2

teste2 = GameTurn(teste1importacao[0],teste1importacao[1],deckjogadores[0],deckjogadores[1])
teste2 = teste2.cardcomparison()

class GameRoll:
    
    def __init__(self,deckp1,deckp2):
        self.deckjogador1 = teste2[0]
        self.deckjogador2 = teste2[1]
        
    def gameon(self):
        winner = True
        
        while winner:
            #Retrieving previous classes in order to roll the game until one of both players wins
            teste1 = CardsOnTable(self.deckjogador1,self.deckjogador2)
            teste1importacao = teste1.cardsontable()
            
            teste2 = GameTurn(teste1importacao[0],teste1importacao[0],teste1importacao[1],teste1importacao[2])
            teste2importacao = teste2.cardcomparison()
            
            
            if len(self.deckjogador2) == 0:
                winner= False
                return "Player 1 wins!"
                break
                
            elif len(self.deckjogador1) == 0:
                winner= False
                return "Player 2 wins!"
                break


rodadasemwhile = GameRoll(teste2[0],teste2[1])
resultadofinal = rodadasemwhile.gameon()
print(resultadofinal)           