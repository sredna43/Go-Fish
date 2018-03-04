#GO FISH
#12/10/2016
#CS121 Group project
#Anders O., Megan B., Christopher C., Benjamin S., Caroline U.

''' Welcome to the St. Olaf version of Go Fish! '''

''' This project was a blast to work on, and it is a fully functional
    (although perhaps not the prettiest) game of Go Fish with a 
    St. Olaf College flair to it. Feel free to take a peak at the code
    and make your own changes as you see fit. Enjoy! '''

import pygame, random, sys, time
from pygame.locals import *


pygame.init()
FPS = 30
WINDOWWIDTH = 1000 # Creates window size
WINDOWHEIGHT = 630 # Creates window size


DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)

pygame.display.set_caption('Go Fish') # Creates Title of Window

#Sounds from freesounds.org
shuffleSound = pygame.mixer.Sound('Sounds/shuffle.ogg')
cardPluck = pygame.mixer.Sound('Sounds/Pluck.ogg')
playingMusic = pygame.mixer.Sound('Sounds/MontyPython.ogg')

#From St. Olaf website
startMenuMusic = pygame.mixer.Sound('Sounds/FramFram.ogg')

startMenuMusic.play(-1)


#variables for playing the game

STARTMENU = 'startmenu'
PLAYING = 'playing'
RULES = 'rules'
GAMEWON = 'gamewon'

#gamemode to begin game
GAMEMODE = STARTMENU
SONG = 'MontyPython'


#colors         R    G    B
TABLEGREEN = ( 47, 178,  69)
WHITE      = (255, 255, 255)
BLACK      = (  0,   0,   0)
OLAFYELLOW = (255, 213,   0)
BROWN      = (114,  90,  42)
LIGHTBROWN = (161, 120,  37)
GRAY       = (200, 200, 200)

Boardimg = pygame.image.load('Images/board.jpg').convert()
SONG = 'MontyPython'


# -*- coding: cp1252 -*-
#/usr/bin/env python
#Simon H. Larsen
#Buttons
#Project startet: d. 26. august 2012
class Button:
    def create_button(self, surface, color, x, y, length, height, width, text, text_color):
    # Creates buttons
        surface = self.draw_button(surface, color, length, height, x, y, width)
        surface = self.write_text(surface, text, text_color, length, height, x, y)
        self.rect = pygame.Rect(x,y, length, height)
        return surface

    def write_text(self, surface, text, text_color, length, height, x, y):
    # Writes text on the buttons
        font_size = int(length//len(text))
        myFont = pygame.font.SysFont("Calibri", font_size)
        myText = myFont.render(text, 1, text_color)
        surface.blit(myText, ((x+length/2) - myText.get_width()/2, (y+height/2) - myText.get_height()/2))
        return surface

    def draw_button(self, surface, color, length, height, x, y, width):
    # Draws the button to the display window
        for i in range(1,10):
            s = pygame.Surface((length+(i*2),height+(i*2)))
            s.fill(color)
            alpha = (255/(i+2))
            if alpha <= 0:
                alpha = 1
            s.set_alpha(alpha)
            pygame.draw.rect(s, color, (x-i,y-i,length+i,height+i), width)
            surface.blit(s, (x-i,y-i))
        pygame.draw.rect(surface, color, (x,y,length,height), 0)
        pygame.draw.rect(surface, (190,190,190), (x,y,length,height), 1)
        return surface

    def pressed(self, mouse):
    # Recognized when a button is pressed
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        return True
                    else: return False
                else: return False
            else: return False
        else: return False

class Menu:
    def __init__(self, playgame, surface):
        self.playgame = playgame
        self.surface = surface
        self.StartButton = Button()
        self.RulesButton = Button()
        self.QuitButton = Button()
        self.BackButton = Button()
        self.Background = pygame.image.load('Images/background.png').convert()

    def startMenu(self):
        #sets up sizes relative to number of buttons
        #global GAMEMODE
        l = 250
        h = 125
        w = 0
        y = (WINDOWHEIGHT/2)
        x = (WINDOWWIDTH/2) - (l/2)
        self.surface.fill(TABLEGREEN)
        self.surface.blit(self.Background, (0,0))
        self.StartButton.create_button(self.surface, BLACK, x, y, l, h, w, 'PLAY', OLAFYELLOW) # Creates Play button
        self.RulesButton.create_button(self.surface, BLACK, x, y+h+20, l, h-75, w, 'RULES', LIGHTBROWN) # Creates Rules button
        self.QuitButton.create_button(self.surface, BLACK, x, y+h+90, l, h-75, w, 'QUIT', LIGHTBROWN) # Creates Quit button
        pygame.display.flip()
        while self.playgame == STARTMENU:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == MOUSEBUTTONDOWN:
                    if self.StartButton.pressed(mouse):
                        print('Play ball!')
                        self.playgame = PLAYING
                        shuffleSound.play()
                        playingMusic.play(-1)
                        startMenuMusic.stop()
                        self.surface.blit(Boardimg, (0,0))
                        return PLAYING

                    elif self.RulesButton.pressed(mouse):
                        print('Rules')
                        self.playgame = RULES
                        self.showRules()

                    elif self.QuitButton.pressed(mouse):
                        print('Quit')
                        pygame.quit()
                        sys.exit()


    def showRules(self):
    # Recognizes when the Rules button is pressed, and displays ther rules page
            f = open('Go Fish Rules.txt','r')
            text = f.read()
            f.close()
            text_size = 24
            textlines = text.split('\n')
            myFont = pygame.font.Font('freesansbold.ttf', text_size)
            self.surface.fill(TABLEGREEN)
            self.BackButton.create_button(self.surface, BROWN, 750, 550, 60, 40, 0, 'BACK', LIGHTBROWN) # Creates Back button
            pygame.display.flip()
            y = 10
            for aline in textlines:
                myText = myFont.render(aline, True, WHITE, TABLEGREEN)
                self.surface.blit(myText, (10,y))
                pygame.display.update()
                y += text_size
            while self.playgame == RULES:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == MOUSEBUTTONDOWN:
                        if self.BackButton.pressed(pygame.mouse.get_pos()): # Recognizes that the back button is pressed
                            self.playgame = STARTMENU # If button is pressed, goes to the start menu
                            main()

class Deck:
    def __init__(self):
        self.values = ('a', '2', '3', '4', '5', '6', '7', '8', '9',
                       '10', 'j', 'q', 'k')
        self.suits = ('clubs', 'hearts', 'spades', 'diamonds')
        self.deck = [] # Deck is a list
        self.cardimgs = [] # Card Images is a list
        for suit in self.suits:
            for value in self.values:
                self.deck.append((value, suit)) # Calls each value of each suit
                self.cardimgs.append('Images/' +suit+ '-' +value+ '-75.png') # This calls the card image file for each card
        self.deckimgs = {} # Key is card value, value is the card image
        i = 0
        for acard in self.deck:
            self.deckimgs[acard] = pygame.image.load(self.cardimgs[i]) # Adds card images to the dictionary deckimgs
            i += 1
        self.deckimgs['cardback'] = pygame.image.load('Images/cardback.png')
        random.shuffle(self.deck) # Shuffles deck

    def getCardimgs(self):
    # Displays Card
        return self.deckimgs

    def drawCard(self):
    # Removes a card from the deck
        return self.deck.pop(0)

    def getLen(self):
    # Gets the length of the deck
        return len(self.deck)

    def Deal(self):
    # Deals cards at the beginning of the game
        hand1 = [] # Creates 4 empty hands
        hand2 = []
        hand3 = []
        hand4 = []
        for i in range(5):
            hand1.append(self.drawCard()) # Draws cards for each hand
            hand2.append(self.drawCard())
            hand3.append(self.drawCard())
            hand4.append(self.drawCard())
        hands = [hand1, hand2, hand3, hand4] # Puts the four hands in a list called hands
        return hands

class Hand:
    def __init__(self, cards):
        self.cards = cards

    def addCard(self, card):
        self.cards.append(card) # adds cards to the hand
        return self.cards

    def removeCard(self, card):
        self.cards.remove(card) # remove cards from hand
        return self.cards

    def getHand(self):
        return self.cards # gets card values for a hand

    def getLen(self):
        return len(self.cards) # gets the length of a hand

class Card(pygame.sprite.Sprite):
    def __init__(self, cardimg, cardval, xpos, ypos):
        pygame.sprite.Sprite.__init__(self)
        self.image = cardimg
        self.cardval = cardval
        self.xpos = xpos # each card holds its own x coordinate
        self.ypos = ypos # each card holds its own y coordinate
        self.rect = pygame.Rect((self.xpos, self.ypos),(75, 107))

    def Draw(self):
        DISPLAYSURF.blit(self.image, (self.xpos, self.ypos)) # Draws one card on another
        pygame.display.update(self.rect) # Updates the whole window

    def clicked(self, mouse):
    # Recognizes when a mouse click happens on a card
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.topleft[0]+30:
                    if mouse[1] < self.rect.bottomright[1]:
                        return True
                    else: return False
                else: return False
            else: return False
        else: return False

    def getValue(self):
    # Returns the suit and value of a card
        return self.cardval

class AI:
    global MOVES
    def __init__(self, hand, thisAI):
        self.hand = hand.getHand()
        self.handobj = hand
        self.thisAI = thisAI

    def getMove(self):
        time.sleep(.2) # Response time of AI
        numlist = []
        cardlist = []
        if len(self.hand) == 0:
            gameWon(self.handobj) # If the number of cards in a hand is 0, the game is WON!
        if len(self.hand) == 1:
            return self.hand[0] # If there is one card in the hand, return the card
        for cardval in self.hand:
            numlist.append(cardval[0]) # Builds a list of the card values in the hand of the AI
            cardlist.append(cardval) # Creates a list of the cards and number in the hand of an AI
        cval = self.hand[random.randrange(0, len(self.hand))] # Finds a random card in the hand
        for acardval in numlist:
            for aKey in list(MOVES.keys()):
                if acardval in MOVES[aKey][-1:-4]:
                    return acardval                
        for i in range(len(numlist)-1):
            if numlist.pop(i) in numlist:
                for acard in cardlist:
                    if len(numlist) > 1 and random.randrange(0,3) == 1: # If you have more than one card of a certain value, the AI is more likely to ask for that card
                        if acard[0] == numlist.pop(i):
                            cardvalue = acard
                            return cardvalue
                    else: return cval
            else: return cval # Asks for a card

    def getOpponent(self):
        self.players = ['You','Chip','Digit','Hacker'] # A list of players
        self.players.remove(self.thisAI) # Removes self from the list, so the AI doesn't ask itself for a card
        print(MOVES)
        for aKey in list(MOVES.keys()):
            if self.cardvalue[0] in MOVES[aKey]:
                if aKey != self.thisAI:
                    return aKey
        return self.players[random.randrange(0,3)] # AI randomly chooses an opponent to ask for a card

    def makePlay(self):
        drawPlay(self.thisAI+"'s turn") # Displays text in the game window
        self.cardvalue = self.getMove()
        self.opponentText = self.getOpponent()
        self.opponent = HANDS[self.opponentText] # Looks at the opponent's hand
        MOVES[self.thisAI].append(self.cardvalue[0])
        checkQuit()
        drawPlay('Hey ' +self.opponentText+ ', got any ' +self.cardvalue[0]+"'s?") # Displays text in the game window
        #Function for matching cards
        self.matches = checkMatch(self.opponent, self.cardvalue)
        if self.matches[0] != '': # Checks if a match was made
            for amatch in self.matches:
                self.handobj.addCard(amatch) # Add card to one players hand
                self.opponent.removeCard(amatch) # Remove card from the other players hand
                fk = fourKind(self.handobj)
                if fk:
                    SCORES[self.thisAI] += 1
                cardPluck.play()
            self.makePlay()
        else:
            checkQuit()
            drawPlay('Go Fish!') # If there is no match, print "Go Fish!"
            if DECK.getLen() > 0:
                self.handobj.addCard(DECK.drawCard())
            fk = fourKind(self.handobj)
            if fk:
                SCORES[self.thisAI] += 1
            cardPluck.play()
            gameWon(self.handobj)
            return None

def drawPlay(text):
# Prints words on the screen to give directions about which players turn it is
    x = (WINDOWWIDTH/2)-(len(text)*5)
    for size in range(24,37):
        time.sleep(.01)
        myFont = pygame.font.Font('freesansbold.ttf', size)
        myText = myFont.render(text, True, OLAFYELLOW, BLACK)
        rect = myText.get_rect()
        DISPLAYSURF.blit(myText, (x, WINDOWHEIGHT-177))
        pygame.display.update()
        x -= 2
    time.sleep(.8)
    updateScreen() # Updates display

def deleteFour(hand, cardValue):
# Deletes the four matching cards in the hand
    delList = []
    for acard in hand.getHand():
        if acard[0] == cardValue:
            delList.append(acard)
    for delCard in delList:
        hand.removeCard(delCard)

def fourKind(hand):
# Distinguishes 4 of a kind, and put them into a list
    checkinglist = []
    matchedlist = []
    fourofakind = []
    occurences = 0
    ret = False
    cards = hand.getHand()
    for acard in cards:
        checkinglist.append(acard[0])
    checkinglist.sort()
    for item in checkinglist:
        occurences = checkinglist.count(item)
        if occurences > 3:
            matchedlist.append(item)
    if len(matchedlist) > 0: # If you four of a kind, it returns true
        deleteFour(hand, matchedlist[0])
        drawPlay('Four of a kind!')
        ret = True
    return ret

def gameWon(hand):
    scorekeys = list(SCORES.keys())
    scorevalues = list(SCORES.values())
    if len(hand.getHand()) == 0: # If one player has 0 hands in their hand...
            winner = scorekeys[scorevalues.index(max(scorevalues))] # The winner is the person who has the highest score
            showWinner(winner)

def showWinner(winner):
    DISPLAYSURF.fill(BLACK)
    if winner == 'You':
        text = winner + 'win!' # If the player wins, display "You win!"
    else:
        text = winner + 'wins!' # If an AI wins, display the name of the AI
    myFont = pygame.font.Font('freesansbold.ttf', 64)
    myText = myFont.render(text, True, OLAFYELLOW, BLACK)
    DISPLAYSURF.blit(myText, (WINDOWWIDTH/2 - len(winner)*5, WINDOWHEIGHT/2))
    pygame.display.flip()
    GAMEMODE = MENU.startMenu()
    time.sleep(5)
    main()

def terminate():
# Terminates Game
    pygame.quit() # GAMEMODE = MENU.startMenu() ? ? ?  Would this work?
    sys.exit()

def checkQuit():
# If you press the X in the corner of the screen, the window will close
    global SONG
    for event in pygame.event.get(QUIT):
        terminate()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()

def checkMatch(hand, cardCheck):
# Checks if cards match
    checkHand = hand.getHand()
    matches = ['']
    cardnum = cardCheck[0]
    for acard in checkHand:
        acardnum = acard[0]
        if acardnum == cardnum:
            if '' in matches:
                matches.remove('')
            matches.append(acard)
    if '' not in matches:
        drawPlay('Yes!')
    print('matches: ', matches)
    return matches

def drawScore():
# Displays the scores of all player in the window
    x = WINDOWWIDTH/2 - 140
    y = WINDOWHEIGHT/2 - 50
    myFont = pygame.font.Font('freesansbold.ttf', 16)
    textlist = ['Scores','-------------']
    players = ['You','Chip','Digit','Hacker']
    eraser = myFont.render('                    ', True, BLACK, BLACK) # erases old score and displays new score

    for i in range(6):
        DISPLAYSURF.blit(eraser, (x,y))
        y += 16
    y = WINDOWHEIGHT/2 - 50
    for aplayer in players:
        textlist.append(aplayer+ ': ' +str(SCORES[aplayer]))
    for text in textlist:
        myText = myFont.render(text, True, LIGHTBROWN, BLACK)
        DISPLAYSURF.blit(myText, (x,y))
        y += 16

def updateScreen():
# Shows cange in players hands, etc.
    global playerSprites, SONG
    surface = DISPLAYSURF
    decklen = DECK.getLen()
    surface.blit(Boardimg, (0,0))
    cardback = CARDIMAGES['cardback']
    cardbackrotate = pygame.transform.rotate(cardback, 90)
    for i in range(decklen):
        if decklen > 0:
            surface.blit(cardback, (WINDOWWIDTH/2 - (39 - i/7), WINDOWHEIGHT/2 - (57 + i/6)))
    AI1len = AI1HAND.getLen() # Lenght of each of the hands
    AI2len = AI2HAND.getLen()
    AI3len = AI3HAND.getLen()
    PLAYERlen = PLAYERHAND.getLen()
    yTop = WINDOWHEIGHT/2 - (AI1len*15) # Sets Coordinates for the cards in the hand of AI1
    for i in range(AI1len):
        surface.blit(cardbackrotate, (10, yTop))
        yTop += 30
    yTop = WINDOWHEIGHT/2 - (AI3len*15) # Sets Coordinates for the cards in the hand of AI3
    for i in range(AI3len):
        surface.blit(cardbackrotate, (WINDOWWIDTH-117, yTop))
        yTop += 30
    xLeft = WINDOWWIDTH/2 - (AI2len*15) # Sets Coordinates for the cards in the hand of AI2
    for i in range(AI2len):
        surface.blit(cardback, (xLeft, 10))
        xLeft += 30
    xLeft = WINDOWWIDTH/2 - (PLAYERlen * 15)
    indvalue = 1
    playerhandlist = PLAYERHAND.getHand()
    playerhandlist.sort()
    listind = 0
    phand = pygame.sprite.Group()
    playerSprites = []
    for acard in playerhandlist:
        card = Card(CARDIMAGES[acard], acard, xLeft, WINDOWHEIGHT-117)
        card.Draw()
        playerSprites.append(card)
        xLeft += 30
        indvalue += 1
        listind += 1
    myFont = pygame.font.Font('freesansbold.ttf', 16)
    if TURN == 'Chip':
        chipColor = OLAFYELLOW # If its a player's turn, their name changes color
    else:
        chipColor = LIGHTBROWN
    if TURN == 'Digit':
        digitColor = OLAFYELLOW
    else:
        digitColor = LIGHTBROWN
    if TURN == 'Hacker':
        hackerColor = OLAFYELLOW
    else:
        hackerColor = LIGHTBROWN

    chip = myFont.render('Chip', True, chipColor, BLACK)
    digit = myFont.render('Digit', True, digitColor, BLACK)
    hacker = myFont.render('Hacker', True, hackerColor, BLACK)
    DISPLAYSURF.blit(chip, (140, WINDOWHEIGHT/2))
    DISPLAYSURF.blit(digit, (WINDOWWIDTH/2 - 20, 140))
    DISPLAYSURF.blit(hacker, (WINDOWWIDTH - 190, WINDOWHEIGHT/2))
    fram = myFont.render('MUSIC: Fram', True, LIGHTBROWN, BLACK)
    monty = myFont.render('MUSIC: Monty', True, LIGHTBROWN, BLACK)
    nothing = myFont.render('MUSIC: Off', True, LIGHTBROWN, BLACK)
    if SONG == 'MontyPython':
        TEXT = 'Monty'
    elif SONG == 'FramFram':
        TEXT = 'Fram'
    else:
        TEXT = SONG
    soundButton.create_button(DISPLAYSURF, BROWN, 10, 10, 50, 30, 0, TEXT, GRAY)
    #do stuff with turns and whatnot here
    drawScore()
    pygame.display.flip()

def whoFirst():
    first = ['You','Chip','Digit','Hacker']
    return first[random.randrange(0,4)]

DECK = Deck()
dealtCards = DECK.Deal()
CARDIMAGES = DECK.getCardimgs()
PLAYERHAND = Hand(dealtCards[0])
AI1HAND = Hand(dealtCards[1])
AI2HAND = Hand(dealtCards[2])
AI3HAND = Hand(dealtCards[3])
HANDS = {'You':PLAYERHAND, 'Chip':AI1HAND,
                'Digit':AI2HAND, 'Hacker':AI3HAND}
MENU = Menu(GAMEMODE, DISPLAYSURF)
SCORES = {'You':0, 'Chip':0, 'Digit':0, 'Hacker':0}
TURN = whoFirst()
CHIP = AI(AI1HAND, 'Chip')
DIGIT = AI(AI2HAND, 'Digit')
HACKER = AI(AI3HAND, 'Hacker')
playerSprites = []
LASTSONG = SONG
soundButton = Button()
MOVES = {'You':[' '],'Chip':[' '], 'Digit':[' '], 'Hacker':[' ']}

def main():
# This implements ALL the functions!
    global TURN, SONG, LASTSONG, MOVES
    GAMEMODE = MENU.startMenu()
    while GAMEMODE == PLAYING:
        while TURN == 'You':
            TURN = 'mine'
            updateScreen()
            drawPlay('Your turn, ask who?')
            gameWon(PLAYERHAND)
            checkQuit()
            while TURN == 'mine':
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        checkQuit()
                        mousepos = pygame.mouse.get_pos()
                        if mousepos[0] < 140 and mousepos[1] > 70:
                            opponent1 = 'Chip'
                            drawPlay('Hey Chip, ')
                        elif mousepos[1] < 150 and mousepos[0] > 100:
                            opponent1 = 'Digit'
                            drawPlay('Hey digit, ')
                        elif mousepos[0] > 800:
                            opponent1 = 'Hacker'
                            drawPlay('Hey Hacker, ')
                        elif soundButton.pressed(mousepos):
                            if SONG == 'MontyPython':
                                SONG = 'FramFram'
                                playingMusic.stop()
                                startMenuMusic.play(-1)
                                updateScreen()
                            elif SONG == 'FramFram':
                                SONG = 'None'
                                playingMusic.stop()
                                startMenuMusic.stop()
                                updateScreen()
                            else:
                                SONG = 'MontyPython'
                                startMenuMusic.stop()
                                playingMusic.play(-1)
                                updateScreen()
                        else:
                            for acard in playerSprites:
                                if acard.clicked(mousepos):
                                    drawPlay('Any ' +acard.getValue()[0]+ "'s?")
                                    matches = checkMatch(HANDS[opponent1], acard.getValue())
                                    MOVES['You'].append(acard.getValue()[0])
                                    if matches[0] != '':
                                        for amatch in matches:
                                            PLAYERHAND.addCard(amatch)
                                            HANDS[opponent1].removeCard(amatch)
                                            fk = fourKind(PLAYERHAND)
                                            print(fk)
                                            if fk:
                                                SCORES['You'] += 1
                                            cardPluck.play()
                                        TURN = 'You'
                                    else:
                                        checkQuit()
                                        TURN = 'Chip'
                                        drawPlay('Go Fish!')
                                        if DECK.getLen() > 0:
                                            drawnCard = DECK.drawCard()
                                            PLAYERHAND.addCard(drawnCard)
                                        fk = fourKind(PLAYERHAND)
                                        if fk:
                                            SCORES['You'] += 1
                                        gameWon(PLAYERHAND)
                                        cardPluck.play()
                                        updateScreen()
                    elif event.type == QUIT:
                        terminate()

        if TURN == 'Chip':
            updateScreen()
            checkQuit()
            CHIP.makePlay()
            for event in pygame.event.get():
                mousepos = pygame.mouse.get_pos()
                if event.type == MOUSEBUTTONDOWN:
                        if soundButton.pressed(mousepos):
                            if SONG == 'MontyPython':
                                SONG = 'FramFram'
                                playingMusic.stop()
                                startMenuMusic.play(-1)
                                updateScreen()
                            elif SONG == 'FramFram':
                                SONG = 'None'
                                playingMusic.stop()
                                startMenuMusic.stop()
                                updateScreen()
                            else:
                                SONG = 'MontyPython'
                                startMenuMusic.stop()
                                playingMusic.play(-1)
                                updateScreen()
            cardPluck.play()
            TURN = 'Digit'

        if TURN == 'Digit':
            updateScreen()
            checkQuit()
            DIGIT.makePlay()
            for event in pygame.event.get():
                mousepos = pygame.mouse.get_pos()
                if event.type == MOUSEBUTTONDOWN:
                        if soundButton.pressed(mousepos):
                            if SONG == 'MontyPython':
                                SONG = 'FramFram'
                                playingMusic.stop()
                                startMenuMusic.play(-1)
                                updateScreen()
                            elif SONG == 'FramFram':
                                SONG = 'None'
                                playingMusic.stop()
                                startMenuMusic.stop()
                                updateScreen()
                            else:
                                SONG = 'MontyPython'
                                startMenuMusic.stop()
                                playingMusic.play(-1)
                                updateScreen()
            cardPluck.play()
            TURN = 'Hacker'

        if TURN == 'Hacker':
            updateScreen()
            checkQuit()
            HACKER.makePlay()
            cardPluck.play()
            for event in pygame.event.get():
                mousepos = pygame.mouse.get_pos()
                if event.type == MOUSEBUTTONDOWN:
                        if soundButton.pressed(mousepos):
                            if SONG == 'MontyPython':
                                SONG = 'FramFram'
                                playingMusic.stop()
                                startMenuMusic.play(-1)
                                updateScreen()
                            elif SONG == 'FramFram':
                                SONG = 'None'
                                playingMusic.stop()
                                startMenuMusic.stop()
                                updateScreen()
                            else:
                                SONG = 'MontyPython'
                                startMenuMusic.stop()
                                playingMusic.play(-1)
                                updateScreen()
            TURN = 'You'
        LASTSONG = SONG
        pygame.event.clear()

if __name__ == '__main__':

    main()
