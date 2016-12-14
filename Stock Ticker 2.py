#Stock Ticker

import random, sys, pygame
from pygame.locals import *
from win32api import GetSystemMetrics

FPS = 30 #frames per second to update the DISPLAYSURF
screenWidth  =  GetSystemMetrics(0) #Sets Width baised on monitor size
screenHeight =  GetSystemMetrics(1) #Sets Height baised on monitor size
Width = screenWidth
Height= screenHeight

#COLOURS
BLACK     = (  0,   0,   0)
WHITE     = (255, 255, 255)
GREY      = (105, 105, 105)
RED       = (255,   0,   0)
BLUE      = (  0, 138, 230)
YELLOW    = (255, 255,   0)
ORANGE    = (244, 197,  66)
GOLD      = (221, 202,  77)
GREEN     = ( 77, 221, 111)
PINK      = (255, 168, 171)
WHITE     = (255, 255, 255)
DARKGRAY  = ( 64,  64,  64)
LIGHTGRAY = (212, 208, 200)

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, myfont, numfont, space, spaceV, spaceHC, spaceVC

    # Pygame initialization and basic set up
    pygame.init()
    FPSCLOCK = pygame.time.Clock()

    DISPLAYSURF = pygame.display.set_mode((screenWidth, screenHeight), RESIZABLE | FULLSCREEN)
    #FAKESURF = DISPLAYSURF.copy()
    
    pygame.display.set_caption('Stock Ticker')
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    myfont    = pygame.font.Font('freesansbold.ttf',int(Width/40))
    numfont   = pygame.font.Font('freesansbold.ttf',int(Width/70))

    space = Width/46
    spaceV = Height / 1.75  #Set vertical height of board
    spaceV = spaceV / 10    #set vertical hieght of playing field
    spaceHC = (space/2)
    spaceVC = (spaceV/2)
    playerCnt = 1
    player1 = ''
    player2 = ''
    player3 = ''
    player4 = ''
    hasRolled = False
#    pic = pygame.surface.Surface((50, 50))

    class Player(object):
        def __init__(self,name,money):
            self.name = name
            self.money = money
    class Game(object):
        def __init__(self,players):
            self.players = Player # a list of players
            self.running = False
        def dice_rolling(self):
            #ROLL DICE
            rollDice = []
            rollDice1 = ''
            rollDice2 = ''
            rollDice3 = ''
            dice1 = ['GRAIN','INDUST','BONDS','OIL','SILVER','GOLD']
            dice2 = ['UP','DOWN']
            dice3 = ['5','10','20','DIV']

            rollDice1 = random.choice(dice1)
            rollDice2 = random.choice(dice2)
            rollDice3 = random.choice(dice3)
            rollDice = [rollDice1,rollDice2,rollDice3]
            print(rollDice)
        def win(self,player):
            print("{} wins!".format(player.name))
        def run(self):
            self.running = True
            while self.running:
                board()
                for player in self.players:
                    roll = dice_rolling()
#    Game().run()
    print(playerCnt)
    startScreen()
    
    while True:
        for event in pygame.event.get(): # event handling loop
            pygame.event.pump()
            if event.type == pygame.QUIT:
                # Player clicked the "X" at the corner of the window.
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            #elif event.type == VIDEORESIZE:
            #    DISPLAYSURF = pygame.display.set_mode(screenWidth,screenHeight,  HWSURFACE|DOUBLEBUF|RESIZABLE)
            #    DISPLAYSURF(pygame.transform.scale(FAKESURF, screenWidth,screnHeight),(0,0))
        if playerCnt == 1:
            players = [player1]
            player1 = Player("Player 0ne", 5000)
        if playerCnt == 2:
            players = [player1,player2]
            player1 = Player("Player 0ne", 5000)
            player2 = Player("Player Two", 5000)
        if players == 3:
            player1 = Player("Player 0ne", 5000)
            player2 = Player("Player Two", 5000)
            player3 = Player("Player Three", 5000)
        if players == 4:
            player1 = Player("Player 0ne", 5000)
            player2 = Player("Player Two", 5000)
            player3 = Player("Player Three", 5000)
            player4 = Player("Player Four", 5000)

        #SET UP GAME  
       # player1 = Player("Player One", 5000)

        board()
        x = 1

        blitText(player1.name,20,WHITE,0,255,30,0)
        blitText("$"+str(player1.money), 20, WHITE, 0, 255,170,0)
 
        indicator(RED,23,3)
        indicator(BLACK,23,4)
        indicator(BLUE,23,5)
        indicator(YELLOW,23,6)
        indicator(WHITE,23,7) 
        indicator(GREEN,23,8)

        
        pygame.display.update()        
        FPSCLOCK.tick()
        
def indicator(colour,x,y):
        global space, spaceV, spaceHC, spaceVC
        pygame.draw.circle(DISPLAYSURF,colour,(int(space*x-spaceHC),int(spaceV*y+spaceVC)),int(space/2))                       

def startScreen():
    DISPLAYSURF.fill(GREY)

    # Position the title image.
    titleImage = pygame.image.load('title.png')
    titleImage = pygame.transform.scale(titleImage,(screenWidth,screenHeight))
    rect = titleImage.get_rect()
    
    
    DISPLAYSURF.fill(GREY)


    DISPLAYSURF.blit(titleImage,rect)
    pygame.display.flip()
    #blitText('Stock Ticker',40,BLACK,0,255,Width/2,Height/3)
    blitText('PRESS ENTER TO CONTINUE',20,WHITE,0,255,(Width/4+Width/4+Width/4),(Height/4+Height/4*2))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit() 
                return
        pygame.display.update()
        FPSCLOCK.tick()

def blitText(printText,size,color,rotation,textAlpha,x,y):
    blitFont = pygame.font.Font('freesansbold.ttf',size)
    text = blitFont.render(printText,True,color)
    text = pygame.transform.rotate(text,rotation)
    text.set_alpha(textAlpha)
    DISPLAYSURF.blit(text, [x,y])

    
def board():
    DISPLAYSURF.fill(GREY)
    global myfont
    space = Width/46        #Get DISPLAYSURF width and divide by 43 to get board length
    line = space       
    spaceV = Height / 1.75  #Set vertical height of board
    spaceV = spaceV / 10    #set vertical hieght of playing field
     
    pygame.draw.rect(DISPLAYSURF, BLUE,  (0,spaceV,Width,spaceV*10))

    #Draw Each Colour Horizontal line
    pygame.draw.rect(DISPLAYSURF, WHITE, (space, spaceV*2, Width - space*2,spaceV+1))        
    pygame.draw.rect(DISPLAYSURF, GOLD,  (space, spaceV*3, Width - space*2, spaceV+1))
    pygame.draw.rect(DISPLAYSURF, WHITE, (space, spaceV*4, Width - space*2, spaceV+1))
    pygame.draw.rect(DISPLAYSURF, ORANGE,(space, spaceV*5, Width - space*2, spaceV+1))
    pygame.draw.rect(DISPLAYSURF, GREEN, (space, spaceV*6, Width - space*2, spaceV+1))
    pygame.draw.rect(DISPLAYSURF, PINK,  (space, spaceV*7, Width - space*2, spaceV+1))
    pygame.draw.rect(DISPLAYSURF, YELLOW,(space, spaceV*8, Width - space*2, spaceV+1)) 
    pygame.draw.rect(DISPLAYSURF, WHITE, (space, spaceV*9, Width - space*2, spaceV+1))

   
    text = myfont.render("DIVIDEND PAYING STOCKS",False,GREY)
    text = pygame.transform.rotate(text,25)
    text.set_alpha(150)
    DISPLAYSURF.blit(text, [space*27,spaceV*3])

    text = myfont.render("DIVIDENDS NOT PAYABLE",False,GREY)
    text = pygame.transform.rotate(text,25)
    text.set_alpha(150)
    DISPLAYSURF.blit(text, [space*5,spaceV*3])

    blitText("O F F   M A R K E T",int(Width/70),GREY,-90,80,(space*2+5),(spaceV*4-10))
    blitText("SPLIT",int(Width/70),GREY,90,80,(space*43+5),(spaceV*5+15))
    blitText("GLD",int(Width/80),BLACK,90,225,(space+(space/4)),(spaceV*3+3))
    blitText("SIL",int(Width/80),BLACK,90,255,(space+(space/4)),(spaceV*4+3))
    blitText("OIL",int(Width/80),BLACK,90,255,(space+(space/4)),(spaceV*5+3))
    blitText("BND",int(Width/80),BLACK,90,255,(space+(space/4)),(spaceV*6+3))
    blitText("IND",int(Width/80),BLACK,90,255,(space+(space/4)),(spaceV*7+3))
    blitText("GRN",int(Width/80),BLACK,90,255,(space+(space/4)),(spaceV*8+3))
    blitText("GLD",int(Width/80),BLACK,-90,225,(space*44+(space/4)),(spaceV*3+3))
    blitText("SIL",int(Width/80),BLACK,-90,255,(space*44+(space/4)),(spaceV*4+3))
    blitText("OIL",int(Width/80),BLACK,-90,255,(space*44+(space/4)),(spaceV*5+3))
    blitText("BND",int(Width/80),BLACK,-90,255,(space*44+(space/4)),(spaceV*6+3))
    blitText("IND",int(Width/80),BLACK,-90,255,(space*44+(space/4)),(spaceV*7+3))
    blitText("GRN",int(Width/80),BLACK,-90,255,(space*44+(space/4)),(spaceV*8+3))
    blitText("PAR",int(Width/80),GREY,-90,80,(space*22+2),(spaceV*8+2))
    blitText("PAR",int(Width/80),GREY, 90,80,(space*22+2),(spaceV*7+2))
    blitText("PAR",int(Width/80),GREY,-90,80,(space*22+2),(spaceV*6+2))
    blitText("PAR",int(Width/80),GREY, 90,80,(space*22+2),(spaceV*5+2))
    blitText("PAR",int(Width/80),GREY,-90,80,(space*22+2),(spaceV*4+2))
    blitText("PAR",int(Width/80),GREY, 90,80,(space*22+2),(spaceV*3+2))

#Print TOP Numbers
    i=2
    sideNums=0
    while i < 23:
        if (len(str(sideNums)) == 1):
            text = numfont.render(str(sideNums)+"  ",True,BLACK)
        elif (len(str(sideNums)) == 2):
            text = numfont.render(str(sideNums)+" ",True,BLACK)
        else:
            text = numfont.render(str(sideNums),True,BLACK)
        text = pygame.transform.rotate(text,90)
        DISPLAYSURF.blit(text, [space*i+5,spaceV*2])
        i = i+1
        sideNums = sideNums + 5
    i = 23
    sideNums2= 100
    while i < 44:
        text = numfont.render(str(sideNums2),True,BLACK)
        text = pygame.transform.rotate(text,90)
        DISPLAYSURF.blit(text, [space*i+5,spaceV*2])
        i = i+1
        sideNums2 = sideNums2 + 5
    while (line+space < Width - space):
        pygame.draw.line(DISPLAYSURF, BLACK, (line,spaceV*2),(line,spaceV*10),1)
        line = line + space
#Print LOWER Numbers
    i=2
    sideNums=0
    while i < 23:
        if (len(str(sideNums)) == 1):
            text = numfont.render("  "+str(sideNums),True,BLACK)
        elif (len(str(sideNums)) == 2):
            text = numfont.render(" "+str(sideNums),True,BLACK)
        else:
            text = numfont.render(str(sideNums),True,BLACK)
        text = pygame.transform.rotate(text,-90)
        DISPLAYSURF.blit(text, [space*i+5,spaceV*9])
        i = i+1
        sideNums = sideNums + 5        
    i = 23
    sideNums2= 100
    while i < 44:
        text = numfont.render(str(sideNums2),True,BLACK)
        text = pygame.transform.rotate(text,-90)
        DISPLAYSURF.blit(text, [space*i+5,spaceV*9])
        i = i+1
        sideNums2 = sideNums2 + 5
    while (line+space < Width - space):
        pygame.draw.line(DISPLAYSURF, BLACK, (line,spaceV*9),(line,spaceV*10),1)
        line = line + space

#draw horizontal lines
    pygame.draw.line(DISPLAYSURF, BLACK, (space,spaceV*3),(space*45,spaceV*3))    
    pygame.draw.line(DISPLAYSURF, BLACK, (space,spaceV*4),(space*45,spaceV*4))
    pygame.draw.line(DISPLAYSURF, BLACK, (space,spaceV*5),(space*45,spaceV*5))
    pygame.draw.line(DISPLAYSURF, BLACK, (space,spaceV*6),(space*45,spaceV*6))
    pygame.draw.line(DISPLAYSURF, BLACK, (space,spaceV*7),(space*45,spaceV*7))
    pygame.draw.line(DISPLAYSURF, BLACK, (space,spaceV*8),(space*45,spaceV*8))
    pygame.draw.line(DISPLAYSURF, BLACK, (space,spaceV*9),(space*45,spaceV*9))

    pygame.draw.line(DISPLAYSURF, BLUE, (space,spaceV),(space,spaceV*10),2)
    pygame.draw.rect(DISPLAYSURF, BLUE, (space,    spaceV*10, Width - space*2, spaceV))

    pygame.draw.rect(DISPLAYSURF, BLUE, (space,    spaceV*2,  space+1,         spaceV+1))    #TOP LEFT
    pygame.draw.rect(DISPLAYSURF, BLUE, (space,    spaceV*9+1,  space+1,         spaceV))    #BOTTOM LEFT
    pygame.draw.rect(DISPLAYSURF, BLUE, (space*23, spaceV*2,  space+1,         spaceV*8))    #CENTER
    pygame.draw.rect(DISPLAYSURF, BLUE, (space*44, spaceV*2,  space+1,         spaceV+1))    #TOP RIGHT
    pygame.draw.rect(DISPLAYSURF, BLUE, (space*44, spaceV*9+1,  space+1,         spaceV))

   # pygame.display.update()
    

if __name__ == '__main__':
    main()
