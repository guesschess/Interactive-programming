# Discriptions:
# The value of the cards in Blackjack:
# 1.number card has value equals to the number
# 2.K,Q,J has value 10
# 3.Ace has value 1 or 11(player's choice)
# =================================================
# Values of a Blackjack hand
# 1. Key observation: Never count two Aces as 11
# 2. Let hand_value be the sum of the card values with
#    Aces as 1
#    If the hand has no Aces:
#       return hand_value
#    else
#       if hand_value + 10 <=21
#          return hand_value + 10
#       else
#          return hand_value

# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []
            # create Hand object

    def __str__(self):
        pass
            # return a string representation of a hand

    def add_card(self, card):
        self.hand.append(card)
            # add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bus
        # compute the value of the hand, see Blackjack video
        Aces = False
        value = 0
        for card in self.hand:
            value += VALUES.get(card.get_rank())
            if card.get_rank()=="A":
                Aces = True
        if value < 11 and Aces == True:
            value += 10 
        return value

                                             
    def draw(self, canvas, pos):
        add_append = 0 
        for card in self.hand:
            card.draw(canvas, (pos[0]+add_append, pos[1]))
            add_append += 80
          
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = [] # create a Deck object
        for i in SUITS:
            for j in RANKS:
                self.deck.append(Card(i,j))

    def shuffle(self):
        # shuffle the deck
        random.shuffle(self.deck)    

    def deal_card(self):
        return self.deck.pop()
    # deal a card object from the deck    
    
    def __str__(self):
        pass	# return a string representing the deck


#define event handlers for buttons
def deal():
    global outcome, in_play
    global player,dealer, score, deck
    if in_play:
        score -=1    
    in_play = True
    outcome = ""
    deck = Deck()
    player = Hand()
    dealer = Hand()
    deck.shuffle()
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())    

def hit():
    global player, in_play, outcome, score, deck
    if in_play:
        if player.get_value() <= 21:
            player.add_card(deck.deal_card())
            
        if player.get_value() > 21:
            outcome = "Player has busted and loses."
            score -=1
            in_play = False
            print ""   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global in_play, outcome, score, dealer, player
    if in_play:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
        if dealer.get_value() > 21:
            outcome = "Dealer has busted. Player wins."
            score +=1
        elif dealer.get_value() < player.get_value():
            outcome = "Player wins."
            score +=1
        else:
            outcome = "Dealer wins."
            score -=1

    in_play = False   
 
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Blackjack", (100,100), 30, "Blue")
    canvas.draw_text("Score " + str(score), (350,100), 20, "Black")
    canvas.draw_text("Dealer", (50,200), 20, "Black")
    canvas.draw_text( outcome, (200, 200), 28, "Black")
    canvas.draw_text("Player", (50,400), 20, "Black")
    if in_play:
        canvas.draw_text("Hit or stand?", (220, 400), 20,"Black")
    else:
        canvas.draw_text("New deal?", (220, 400), 20, "Black")
    dealer.draw(canvas, (50, 220))
    
    if in_play:
        canvas.draw_image(card_back,CARD_BACK_CENTER,CARD_BACK_SIZE,
                          (50+ CARD_BACK_CENTER[0], 220+CARD_BACK_CENTER[1]),
                          CARD_SIZE)
    player.draw(canvas,(50,420))

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
