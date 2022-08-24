import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit #Naipes
        self.rank = rank #Hierarquia das cartas
        self.value = values[rank] #Biblioteca com o peso de cada carta
       
    def __str__(self):
        return self.rank+" of "+self.suit #imprimir uma carta especifica. Ex: Ás de Copas

class Deck:
    def __init__(self):
        
        self.all_cards = [] #Deck principal
        self.deckp1 = []    #Deck do Jogador 1
        self.deckp2 = []    #Deck do Jogador 2
        
        for item1 in suits:
            for item2 in ranks:
                self.all_cards.append(Card(item1,item2)) #Populando o deck principal
    
    def shuffleanddivide(self):
        
        random.shuffle(self.all_cards) #Misturando as cartas
     
        while len(self.all_cards)>0: #Enquanto tiver cartas no deck principal, tirar uma pro deck do Jogador 1 e outra pro J2
            self.deckp1.append(self.all_cards.pop(0))
            self.deckp2.append(self.all_cards.pop(-1))
        
        return [self.deckp1, self.deckp2]

getbothdecks = Deck()
deckjogadores = getbothdecks.shuffleanddivide()
winner = True

class GameOn:
    def __init__(self,deckp1,deckp2):
        self.deckp1 = deckjogadores[0]
        self.deckp2 = deckjogadores[1]
        self.decktable = []
        self.cardobj1 = []
        self.cardobj2 = []
        
    def Game(self):
        
        while winner:
            self.cardobj1 = self.deckp1.pop(-1)
            self.cardobj2 = self.deckp2.pop(-1)
            carta1= str(self.cardobj1)
            carta2= str(self.cardobj2)
            carta1= carta1.split()
            carta2= carta2.split()
            
                        
            if values[carta1[0]] > values[carta2[0]]:
                self.deckp1.append(self.cardobj1.pop(0))
                self.deckp1.append(self.cardobj2.pop(0))
                while len(self.decktable) >0:
                    self.deckp1.append(self.decktable.pop(0))
                if len(self.deckp1)==0 or len(self.deckp2)==0:
                    winner=False
                    break                        
                
            elif values[carta1[0]] < values[carta2[0]]:
                self.deckp2.append(self.cardobj1.pop(0))
                self.deckp2.append(self.cardobj2.pop(0))
                while len(self.decktable) >0:
                    self.deckp2.append(self.decktable.pop(0))
                if len(self.deckp1)==0 or len(self.deckp2)==0:
                    winner=False
                    break
            else:
                self.decktable.append(self.cardobj1.pop(0))
                self.decktable.append(self.cardobj2.pop(0))
        
    def Winner(self):
        if len(self.deckp1)==0:
            print('Player 2 wins!') 
        elif len(self.deckp2)==0:
            print('Player 1 wins!') 


marrumteste = GameOn(deckjogadores[0],deckjogadores[1])
outrocoiso = str(marrumteste)
print(outrocoiso)