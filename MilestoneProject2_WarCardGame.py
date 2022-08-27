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


class CardsOnTable:
    def __init__(self,deck01,deck02):
        self.deck01 = deckjogadores[0] #deck do jogador 1
        self.deck02 = deckjogadores[1] #deck do jogador 2
        self.tabledeck = []
                
    def cardsontable(self):
        self.tabledeck.append(self.deck01.pop(-1))
        self.tabledeck.append(self.deck02.pop(-1))
        
        return self.tabledeck, self.deck01, self.deck02 
        #cartas da mesa, deck REDUZIDO dos J1 e J2

teste1 = CardsOnTable(deckjogadores[0],deckjogadores[1])
teste1importacao = teste1.cardsontable()

class GameTurn:
    def __init__(self,cardp1,cardp2,deckjogador1,deckjogador2):
        self.cardp1, self.cardp2 = teste1importacao[0]    #Carta de cada jogador
        #self.cardp2 = teste1importacao[1]
        self.deckjogador1 = teste1importacao[1]           #Deck de cada jogador
        self.deckjogador2 = teste1importacao[2]
        self.tempdecktable = []                           #Cartas acumuladas na mesa
        
        
    def cardcomparison(self):
        splitc1 = str(self.cardp1)
        splitc2 = str(self.cardp2)
        splitc1 = splitc1.split()
        splitc2 = splitc2.split()
        
        if values[splitc1[0]]>values[splitc2[0]]:
            
            self.deckjogador1.append(self.cardp1)
            self.deckjogador1.append(self.cardp2)
            self.deckjogador1.extend(self.tempdecktable)
            self.tempdecktable = []
            
            return self.deckjogador1, self.deckjogador2
            
            #return f"esse é o comprimento: {len(self.cardp1)} e 
            # {len(self.cardp2)} e {len(self.tempdecktable)} e 
            # {len(self.deckjogador1)}"
            #return "pero que si"
        
        elif values[splitc1[0]]<values[splitc2[0]]:
            self.deckjogador2.append(self.cardp1)
            self.deckjogador2.append(self.cardp2)
            self.deckjogador1.extend(self.tempdecktable)
            self.tempdecktable = []
            
            return self.deckjogador1, self.deckjogador2
            
        else:
            self.tempdecktable.append(self.cardp1)
            self.tempdecktable.append(self.cardp2)
            
            return self.deckjogador1, self.deckjogador2

teste2 = GameTurn(teste1importacao[0],teste1importacao[1],deckjogadores[0],deckjogadores[1])
teste2 = teste2.cardcomparison()