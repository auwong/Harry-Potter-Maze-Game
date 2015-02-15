# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pygame, os

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

DISPLAYSURF = pygame.display.set_mode((1280, 800))
loading1Img = pygame.image.load('Loading1.png')
loading2Img = pygame.image.load('Loading2.png')
loading3Img = pygame.image.load('Loading3.png')
loading4Img = pygame.image.load('Loading4.png')

listLoading = [loading1Img, loading2Img, loading3Img, loading4Img]

for l in listLoading:
        pygame.Surface.blit(DISPLAYSURF, l, (0, -80, 1180, 600))
        pygame.display.update()
        pygame.time.wait(6000)

currentVersion = 'HPotter v22'

import sys
from pygame.locals import *
import random




random.seed()





Black = ( 0, 0, 0)
Gray = (128, 128, 128)
Green = ( 0, 128, 0)
Lime = ( 0, 255, 0)
Maroon = (128, 0, 0)
White = (0, 0, 0, 255)
Silver = (192, 192, 192)
SwordColor = (13, 106, 3)

###########################TITLE SCREEN CODE########################
pygame.mixer.music.load('GUZZ.mp3') #Play Music
def superFunction():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.mixer.music.play(-1, 0.0)

    COUNTER = 0

    #These are the various fonts for the title, characters, etc..
    titleFont = pygame.font.Font('freesansbold.ttf', 200)
    BASICFONT = pygame.font.Font('freesansbold.ttf', 30)
    CHARFONT = pygame.font.Font('freesansbold.ttf', 20)

    #Global variables that deal with screen ratios
    pixelBox = 15
    width=85#random.randint(42,82)
    height=20#random.randint(20,40)
    screenWidth = width*(pixelBox+1)-pixelBox
    screenHeight = height*(pixelBox+1)+1/2*pixelBox+1

    #The display surface for the program
    DISPLAYSURF = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption(currentVersion)

    #This is the main screen function with the title and all
    def titleScreen(COUNTER):
        titleSurf1 = titleFont.render('HPotter', True, Gray, Maroon)
        while True:
            DISPLAYSURF.fill(Maroon)
            screenCenter = (screenWidth/2-410, screenHeight/2-150)
            DISPLAYSURF.blit(titleSurf1, screenCenter)
            drawPressKeyMsg()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==KEYDOWN:
                    gamePiece = chooseYourCharacter(COUNTER) #Goes to the display character screen. COUNTER is a counter...
                    return gamePiece
            

    #Exits the program
    def terminate(): 
        pygame.quit()
        sys.exit()
        
    #Draws the message "Press a key to play    
    def drawPressKeyMsg(): 
        pressKeySurf = BASICFONT.render('Press a key to play.', True, Gray)
        pressKeyRect = pressKeySurf.get_rect()
        pressKeyRect.topleft = (screenWidth/2 - 340/2, screenHeight - 70)
        DISPLAYSURF.blit(pressKeySurf, pressKeyRect.topleft)

    def chooseYourCharacter(COUNTER):    
        #Characters - This code will take the large pictures and scale them down to an appropriate size: 187x300 pixels
        potterLGImg = pygame.image.load('potterLG.png')
        dobbyLGImg = pygame.image.load('dobbyLG.png')
        dumbleLGImg = pygame.image.load('dumbledoreLG.png')
        hagridLGImg = pygame.image.load('hagridLG.png')
        hermioneLGImg = pygame.image.load('hermioneLG.png')
        malfoyLGImg = pygame.image.load('malfoyLG.png')
        ronLGImg = pygame.image.load('ronLG.png')
        snapeLGImg = pygame.image.load('snapeLG.png')
        voldemortLGImg = pygame.image.load('voldemortLG.png')
   
            #This blits each character on to the screen            
            
        centerChars = screenHeight / 2 - 170 #Center of the text (char)
        DISPLAYSURF.fill(Maroon)
        DISPLAYSURF.blit(snapeLGImg, (0, centerChars))
        DISPLAYSURF.blit(dobbyLGImg, (150, centerChars))
        DISPLAYSURF.blit(hagridLGImg, (320, centerChars))
        DISPLAYSURF.blit(ronLGImg, (470, centerChars))
        DISPLAYSURF.blit(potterLGImg, (620, centerChars))
        DISPLAYSURF.blit(malfoyLGImg, (750, centerChars))
        DISPLAYSURF.blit(hermioneLGImg, (870, centerChars))
        DISPLAYSURF.blit(voldemortLGImg, (1010, centerChars))
        DISPLAYSURF.blit(dumbleLGImg, (1160, centerChars))
        
        SelectChar = BASICFONT.render('Select Your Character', True, Gray)
        DISPLAYSURF.blit(SelectChar, (screenWidth/2 - 280/2, 20))
        
        pygame.display.update()
        Snape = (CHARFONT.render('<Prof. Snape>',True,Gray))
        DISPLAYSURF.blit(Snape, (20, screenHeight-30))
        pygame.display.update()
        while True:
          
            #This is the text that will go under each picture of each character
            names = ['<Prof. Snape>', '<Dobby>', '<Hagrid>', '<Ron>', '<Potter>', '<Malfoy>', '<Hermione>', '<Voldemort>', '<Dumbledore>']
            listOchars = []
            for i in names:
                listOchars.append(CHARFONT.render(i,True,Gray))
            
            pygame.draw.rect(DISPLAYSURF, Maroon, (0,screenHeight-30,screenWidth, screenHeight))
            #DISPLAYSURF.blit(listOchars[0], (20, screenHeight-30))
            #pygame.display.update()
            
            #This code moves each characters name for the apprpiate key presses
            for event in pygame.event.get():
                if event.type==KEYDOWN:
                    if event.key==K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key==K_LEFT:
                        #COUNTER marks the position in the list and for each side-key press it will change by 1 0r -1
                        if COUNTER - 1 < 0:
                            COUNTER = 8
                            DISPLAYSURF.blit(listOchars[8], (1190, screenHeight-30))
                        else:
                            COUNTER-=1
                            if COUNTER == 0:
                                DISPLAYSURF.blit(listOchars[0], (20, screenHeight-30)) #Blits the name under the character
                            if COUNTER == 1:
                                DISPLAYSURF.blit(listOchars[1], (170, screenHeight-30))
                            if COUNTER == 2:
                                DISPLAYSURF.blit(listOchars[2], (365, screenHeight-30))
                            if COUNTER == 3:
                                DISPLAYSURF.blit(listOchars[3], (525, screenHeight-30))
                            if COUNTER == 4:
                                DISPLAYSURF.blit(listOchars[4], (655, screenHeight-30))
                            if COUNTER == 5:
                                DISPLAYSURF.blit(listOchars[5], (780, screenHeight-30))
                            if COUNTER == 6:
                                DISPLAYSURF.blit(listOchars[6], (900, screenHeight-30))
                            if COUNTER == 7:
                                DISPLAYSURF.blit(listOchars[7], (1030, screenHeight-30))
                            if COUNTER == 8:
                                DISPLAYSURF.blit(listOchars[8], (1190, screenHeight-30)) 
                        #pygame.display.update()
                            
                    #Same as above but for the right arrow key
                    elif event.key==K_RIGHT:
                        if COUNTER + 1 > 8:
                            COUNTER = 0
                            DISPLAYSURF.blit(listOchars[0], (20, screenHeight-30))
            
                        else:
                            COUNTER+=1
                            if COUNTER == 0:
                                DISPLAYSURF.blit(listOchars[0], (20, screenHeight-30))
                            if COUNTER == 1:
                                DISPLAYSURF.blit(listOchars[1], (170, screenHeight-30))
                            if COUNTER == 2:
                                DISPLAYSURF.blit(listOchars[2], (365, screenHeight-30))
                            if COUNTER == 3:
                                DISPLAYSURF.blit(listOchars[3], (525, screenHeight-30))
                            if COUNTER == 4:
                                DISPLAYSURF.blit(listOchars[4], (655, screenHeight-30))
                            if COUNTER == 5:
                                DISPLAYSURF.blit(listOchars[5], (780, screenHeight-30))
                            if COUNTER == 6:
                                DISPLAYSURF.blit(listOchars[6], (900, screenHeight-30))
                            if COUNTER == 7:
                                DISPLAYSURF.blit(listOchars[7], (1030, screenHeight-30))
                            if COUNTER == 8:
                                DISPLAYSURF.blit(listOchars[8], (1190, screenHeight-30))
                #If you press enter after you select your character, this should take you to the main code
                #And generate to maze and all that. Not sure how to get there from here...
                    elif event.key==K_RETURN:
                        return COUNTER #This is where the main game function mentioned above will go
                    pygame.display.update()
            #pygame.time.delay(200)
            #pygame.event.get() # clear event queue

            #We need some new music for the title screen. Any ideas?
     
    while True: # main game loop
        
        playerChar1 = titleScreen(COUNTER)
        return playerChar1
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()


        
###########################CODE FOR MAZE GENERATION##################################

os.environ['SDL_VIDEO_CENTERED'] = '1'

playerChar = superFunction()

class makeMaze:
    
    def __init__(self):
        self.M=[]
        self.width=random.randint(42,82)
        self.height=random.randint(20,40)
        self.start=random.randint(1,self.height-2) #Starting position on left side of maze
        
    def makemaze(self):    
        #Make a 2 dimensional list
        for a in range(self.height):
          self.M.append([])
          for b in range(self.width):
              self.M[a].append(1)


        #Formatting for later
        for i in self.M:
            i[self.width-1]=' '            
        return self.M
    def generate(self):

        newfile.seek(0)
        self.M[self.start][0]='S'
        x=0
        y=self.start
        while self.M[y][self.width-2] == 1: #While the right side is all 1's...
            vertical=0
            horizontal=0
            numberOne = random.randint(1,100)
            if numberOne == 1:
                horizontal+=1
            else:
                vertical+=random.randint(-1,1) #Changes the horizontal and vertical moves by a random index
                horizontal+=random.randint(-1,1)
            if (x + horizontal) >= 1 and (x + horizontal) <= (self.width - 1): #These two make sure the maze stays within the boundary
                if (y + vertical) >= 1 and (y + vertical) <= (self.height - 2):
                    if (vertical * horizontal) == 0: #Makes sure there are no diagonal moves
                        Check=[self.M[y+1][x]==1, self.M[y-1][x]==1, self.M[y][x-1]==1, self.M[y][x+1]==1] #checks above and below and left and right of current square
                        if sum(Check) >=2: #if both above and below are 1's:
                            x+=horizontal #Changes x and y by vert and hori
                            y+=vertical
                            self.M[y][x]=' '
                        else:
                            num=random.randint(1,20)
                            if num==2:
                                x+=horizontal #Changes x and y by vert and hori if these check out
                                y+=vertical
                                self.M[y][x]=' '             
            if x == self.width - 2:
                self.M[y][x] = 'E'

            else:
                pass    
    
    #Print out the maze in a vertical matrix
    def printMaze(self, newfile):
        for i in self.M:
            newfile.write(''.join(map(str,i)))
            newfile.write('\n')
        return newfile

    def openFile(self):
        newfile=open("MAZE GENERATION.txt", 'wt')
        return newfile
    
    def closeFile(self, newfile):
        newfile.close()
        
    def getWidth(self):
        return self.width
        
    def getHeight(self):
        return self.height
        
def instantiate():    
    return makeMaze()    


def buildNewMaze():
    outLay = maze1.openFile()
    maze1.makemaze()
    maze1.generate()
    outLay = maze1.printMaze(outLay)
    maze1.closeFile(outLay)



############################GUI CODE#########################################################################




#class for the floor and walls
class Landscape(object):
    def __init__(self,image,colorOfTile):#initializes image and colorOfTile
        self.image = image
        self.colorOfTile = colorOfTile
    
    def getColor(self):#returns the color
        return self.colorOfTile
    
    def getImg(self):#returns image
        return self.image
        
    def getFloor(self): #returns floor
        return floor.self

    

class Objects(object):#class for all objects
    def __init__(self): #initializes the floor list
        self.floor = []
    
    def makeCoord(self): #makes the map
        global DISPLAYSURF, screenWidth, screenHeight
        width = maze1.getWidth()
        height = maze1.getHeight()
        BASICFONT = pygame.font.Font('freesansbold.ttf', fontSize)
        pygame.display.set_caption(currentVersion)

    

        mazeFile = open("MAZE GENERATION.txt", 'rt')

    
        yCord = -pixelBox
        entrance = None
        for line in mazeFile:
            yCord += pixelBox+1
            xCord = 1
            count = 0
            for character in line:
                count += 1
                if count == width:
                    pass
                else:
                    if character == '1':
                        pygame.Surface.blit(DISPLAYSURF, wallObj.getImg(), (xCord, yCord, pixelBox, pixelBox))
                        xCord += pixelBox+1
                    if character == ' ':
                        pygame.Surface.blit(DISPLAYSURF, floorObj.getImg(), (xCord, yCord, pixelBox, pixelBox))
                        self.floor.append((xCord,yCord))
                        xCord += pixelBox+1
                    if character == 'S':
                        entrance = start(xCord, yCord, Lime)
                        xCord += pixelBox+1
                        
                    if character == 'E':
                        exit = stop(xCord, yCord, Maroon)
                        xCord += pixelBox+1
        
        mazeFile.close()
        Objects().Player(CHARACTER, entrance)
        snitchPos = Snitch().draw(entrance,exit)          
        return(entrance,snitchPos)
    
    def getFloor(self): #returns floor list
        return self.floor
    
    def Player(self, image, coordinate): #blits the image to the give coordinate
        DISPLAYSURF.blit(image, (coordinate))
    
    def move(self, d): #sets up move method
        pass
        
    def canMove(self, Coord):#checks to see if the object can move
        colorOfTile = Objects().getColor(Coord)
        if colorOfTile == Green:
            return True
        return False
    
    def getColor(self, Coord): #returns the color of that coordinate
        return DISPLAYSURF.get_at(Coord)
    
    def nextTile(self,currentCoord,d): #finds the next tile for the object to move to
        # Motion offsets for particular directions
        #     N  E  S   W
        DX = [0, 1*pixelBox+1, 0, -1*pixelBox-1]
        DY = [-1*pixelBox-1, 0, 1*pixelBox+1, 0]
        Coord = (currentCoord[0]+DX[d],currentCoord[1]+ DY[d])
        return Coord
    
def start(xCord, yCord, Color):
    pygame.draw.rect(DISPLAYSURF, Color, (xCord, yCord, pixelBox, pixelBox))
    entrance = (xCord, yCord)
    return entrance
    
def stop(xCord, yCord, Color):
    pygame.draw.rect(DISPLAYSURF, Color, (xCord, yCord, pixelBox, pixelBox))
    exit = (xCord, yCord)
    return exit

class Character(Objects): # class for you character
    def __init__(self): #intializes all floor coordinates list
        self.floor = []
        
    def canMove(self, currentCoord,d): # checks to see if your character can move
        Coord = Objects().nextTile(currentCoord,d)
        colorOfTile = Objects().getColor(Coord)
        if colorOfTile != Black:
            return True
        return False
    
    def move(self,d,currentCoord,coordDict,objDict,hasDict): #moves your character
        Coord = Objects().nextTile(currentCoord,d)
        colorOfTile = Objects().getColor(currentCoord)
        
        for Q in objDict:
            if currentCoord == coordDict[Q]:
                if Q == snitch:
                    soundObj = pygame.mixer.Sound('BELLS2.wav')
                    soundObj.play()
                    coordDict[Q] = (-1,-1)
                if Q == book:
                    soundObj = pygame.mixer.Sound('Book.wav')
                    soundObj.play()
                    coordDict[Q] = (-1,-1)
                if Q == poly:
                    soundObj = pygame.mixer.Sound('PolyJuice.wav')
                    soundObj.play()
                    coordDict[Q] = (-1,-1)
                if Q == sword:
                    soundObj = pygame.mixer.Sound('FindSword.wav')
                    soundObj.play()
                    coordDict[Q] = (-1,-1)
                if Q == dragon:
                    soundObj = pygame.mixer.Sound('FindDragon.wav')
                    soundObj.play()
                    coordDict[Q] = (-1,-1)
                if Q == portalo or portalb:
                    pass
            else:
                pass
        
        
        if colorOfTile == Lime:
            pygame.draw.rect(DISPLAYSURF, Lime, (currentCoord[0], currentCoord[1], pixelBox, pixelBox))
        if colorOfTile == Maroon:
            pygame.draw.rect(DISPLAYSURF, Maroon, (currentCoord[0], currentCoord[1], pixelBox, pixelBox))
        if colorOfTile == floorObj.getColor() or colorOfTile == SwordColor:
            pygame.Surface.blit(DISPLAYSURF, floorObj.getImg(), (currentCoord[0], currentCoord[1], pixelBox, pixelBox))
        if coordDict[portalo] == currentCoord:
            pygame.Surface.blit(DISPLAYSURF, objDict[portalo].getImg(), (currentCoord[0], currentCoord[1], pixelBox, pixelBox))
        if coordDict[portalb] == currentCoord:
            pygame.Surface.blit(DISPLAYSURF, objDict[portalb].getImg(), (currentCoord[0], currentCoord[1], pixelBox, pixelBox))
        if hasDict[portalo] == True:
            pygame.Surface.blit(DISPLAYSURF, objDict[portalo].getImg(), (currentCoord[0], currentCoord[1], pixelBox, pixelBox))
        if hasDict[portalb] == True:
            pygame.Surface.blit(DISPLAYSURF, objDict[portalb].getImg(), (currentCoord[0], currentCoord[1], pixelBox, pixelBox))
        if coordDict[portalo] == Coord:
            pygame.Surface.blit(DISPLAYSURF, CHARACTER, (coordDict[portalb][0], coordDict[portalb][1], pixelBox, pixelBox))
            pygame.Surface.blit(DISPLAYSURF, objDict[portalo].getImg(), (coordDict[portalo][0], coordDict[portalo][1], pixelBox, pixelBox))
            return Coord
        if coordDict[portalb] == Coord:
            pygame.Surface.blit(DISPLAYSURF, CHARACTER, (coordDict[portalo][0], coordDict[portalo][1], pixelBox, pixelBox))
            pygame.Surface.blit(DISPLAYSURF, objDict[portalb].getImg(), (coordDict[portalb][0], coordDict[portalb][1], pixelBox, pixelBox))
            return Coord
        try:
            Objects().Player(CHARACTER, Coord)
            return(Coord)
        except:
            return currentCoord
    
    def noMove(self, currentCoord,coordDict,objDict): #returns character to beginning and plays sound
        soundObj = pygame.mixer.Sound('dp_frogger_squash.wav')
        soundObj.play()
        colorOfTile = Objects().getColor(currentCoord)
        if colorOfTile == floorObj.getColor() or colorOfTile == SwordColor:
            pygame.Surface.blit(DISPLAYSURF, floorObj.getImg(), (currentCoord[0], currentCoord[1], pixelBox, pixelBox))
        if colorOfTile == Maroon:
            pygame.draw.rect(DISPLAYSURF, Maroon, (currentCoord[0], currentCoord[1], pixelBox, pixelBox))
        if coordDict[portalo] == currentCoord:
            pygame.Surface.blit(DISPLAYSURF, objDict[portalo].getImg(), (currentCoord[0], currentCoord[1], pixelBox, pixelBox))
        if coordDict[portalb] == currentCoord:
            pygame.Surface.blit(DISPLAYSURF, objDict[portalb].getImg(), (currentCoord[0], currentCoord[1], pixelBox, pixelBox))
        Objects().Player(CHARACTER, beginPos)
        return(beginPos)

        
        

        
class Snitch(Objects): #class for snitch
    def __init__(self): #initializes
        pass
        
    def draw(self, startCoord,endCoord): # Spawns snitch somewhere near the middle of the map
        if ((startCoord[0]+endCoord[0])/2-1)%16==0: # Makes sure snitch doesn't spawn initially between grids
            middle=((startCoord[0]+endCoord[0])/2,1)
        else:
            middle=((startCoord[0]+endCoord[0])/2+8,1)
        while super(Snitch,self).canMove(middle)==False:  # Makes sure snitch spawns on gray tile
            snitchY=middle[1]+pixelBox+1
            middle=(middle[0],snitchY)
        Objects().Player(SNITCH,middle) # Draws snitch
        return(middle) 
    
    def move(self,currentCoord,pCoord,img,coordDict): # Moves the snitch
        d=random.randint(0,3)
        Coord = Objects().nextTile(currentCoord,d)
        while Coord == pCoord:
            d=random.randint(0,3)
            Coord = Objects().nextTile(currentCoord,d)
        colorOfTile = Objects().getColor(currentCoord)

    
        if Snitch().canMove(Coord,coordDict,currentCoord) == True:
            if colorOfTile == floorObj.getColor():
                pygame.Surface.blit(DISPLAYSURF, floorObj.getImg(), (currentCoord[0], currentCoord[1], pixelBox, pixelBox))
            if currentCoord == pCoord:
                pygame.Surface.blit(DISPLAYSURF, CHARACTER, (currentCoord[0], currentCoord[1], pixelBox, pixelBox))
            Objects().Player(img, Coord)
            return(Coord)
        else:
            return(currentCoord)
        
    def getImg(self): #returns object's image
        return self.image
        
    def checkFor(self,oCoord,pCoord): #compares two coordinates
        if oCoord == pCoord:
            return True
        return False
    
    def canMove(self,Coord,coordDict,currentCoord):
        for c in coordDict:
            if coordDict[c] == Coord and Coord != currentCoord:
                return False
        colorOfTile = Objects().getColor(Coord)
        if colorOfTile == Green:
            return True
        return False
        

        



class Extras(Landscape, Snitch): #class for all the extras that are not the snitch,character,or snake
    def __init__(self,image): #sets extra image
        self.image = image
        
    def draw(self,floor,character): # draws the extras onto the landscape
        cor = random.choice(floor)
        pygame.Surface.blit(DISPLAYSURF, character, (cor[0], cor[1], pixelBox, pixelBox))
        index = floor.index(cor)
        floor = floor[:index] + floor[index+1:]
        return cor,floor


        
class Snake(Extras,Landscape): #Snake object
    def __init__(self,image): #sets snake image
        self.image = image
        
    def move(self,currentCoord,pCoord,img,coordDict): #moves the snake
        d=random.randint(0,3)
        Coord = Objects().nextTile(currentCoord,d)
        colorOfTile = Objects().getColor(currentCoord)

        if Snake(img).canMove(Coord,coordDict,currentCoord) == True:
            if colorOfTile == floorObj.getColor():
                pygame.Surface.blit(DISPLAYSURF, floorObj.getImg(), (currentCoord[0], currentCoord[1], pixelBox, pixelBox))
            if currentCoord == pCoord:
                pygame.Surface.blit(DISPLAYSURF, CHARACTER, (currentCoord[0], currentCoord[1], pixelBox, pixelBox))
            Objects().Player(img, Coord)
            return(Coord)
        else:
            return(currentCoord)
        
    def canMove(self,Coord,coordDict,currentCoord): #checks to see if the snake can move
        for c in coordDict:
            if c != player and coordDict[c] == Coord and Coord != currentCoord:
                return False
        colorOfTile = Objects().getColor(Coord)
        if colorOfTile == Green or coordDict[player] == Coord:
            return True
        return False
    
    def loseItems(self,isDict,hasDict,coordDict,objDict): #redraws all the items if the player hits the snake
        isDict[snake],hasDict[snake] = False,False
        floor = charObj.getFloor()
        coordD = {}
        for h in hasDict:
            if hasDict[h] == True:
                coordD[h] = coordDict[h]
        for f in range(len(floor)):
            if floor[f] in coordD:
                floor = floor[:f] + floor[f+1:]
                
        coordDict[player] = beginPos
        pygame.Surface.blit(DISPLAYSURF, CHARACTER, (beginPos[0], beginPos[1], pixelBox, pixelBox))
        pygame.Surface.blit(DISPLAYSURF, objDict[snake].getImg(), (coordDict[snake][0], coordDict[snake][1], pixelBox, pixelBox))
        for x in objDict:
            if x != player and x != snake and hasDict[x] == True:
                coordDict[x],floor = objDict[x].draw(floor,objDict[x].getImg())
                while coordDict[x] == coordDict[snake]:
                    coordDict[x],floor = objDict[x].draw(floor,objDict[x].getImg())
                hasDict[x] = False
                isDict[x] = False
        return isDict,hasDict,coordDict,objDict
    
def theTerminator(pCoord,hasDict): #checks to see if the player has all the objects and is on the exit
    colorOfTile = Objects().getColor(pCoord)
    for d in hasDict:
        if d != player and d != portalo and d != portalb and hasDict[d] == False:
            return False
    if colorOfTile == Maroon:
        return True
    return False

    



pygame.mixer.init()



##########################GAME LOOP###########################

def RUNTHEGAME(playerChar):
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    global Gray, Black, Green, Lime, playerHasSnitch, Maroon, White, pixelBox, newfile
    global maze1,fontSize, DISPLAYSURF, wallObj, floorObj, CHARACTER, SNITCH, SnitchCoord, PlayCoord
    global blankSpace, playerHasSnitch, beginPos, charObj, snitch,book,poly,sword,dragon,snake,player,portalb,portalo
    Black = ( 0, 0, 0)
    Gray = (128, 128, 128)
    Green = ( 0, 128, 0)
    Lime = ( 0, 255, 0)
    Maroon = (128, 0, 0)
    White = (0, 0, 0, 255)  
    
    newfile = open('MAZE GENERATION.txt', 'wt')   
    
    maze1 = instantiate()
    
    buildNewMaze()    
    pixelBox = 15
    screenWidth = maze1.getWidth()*(pixelBox+1)-pixelBox
    screenHeight = maze1.getHeight()*(pixelBox+1)+1/2*pixelBox+1
    #THese are having trouble...
    
        #GUI
    DISPLAYSURF = pygame.display.set_mode((screenWidth, screenHeight))
    fontSize = 18
    
    #initiate floor and walls class
    floorImg = pygame.image.load('Floor.png').convert()
    wallImg = pygame.image.load('Wall.png').convert()
    floorObj = Landscape(floorImg,Green)
    wallObj = Landscape(wallImg,Black)

    #Characters
    potterImg = pygame.image.load('Harry.png')
    dobbyImg = pygame.image.load('Dobby.png')
    dumbleImg = pygame.image.load('Dumbledore.png')
    hagridImg = pygame.image.load('Hagrid.png')
    hermioneImg = pygame.image.load('Hermione.png')
    malfoyImg = pygame.image.load('Malfoy.png')
    ronImg = pygame.image.load('Ron.png')
    snapeImg = pygame.image.load('Snape.png')
    voldemortImg = pygame.image.load('Voldemort.png')    
    
    snitchImg = pygame.image.load('Snitch.png')
    monsterBookImg = pygame.image.load('MonsterBook.png')
    polyImg = pygame.image.load('Polyjuice.png')
    snakeImg = pygame.image.load('Snake.png')
    swordImg = pygame.image.load('Sword.png')
    dragonImg = pygame.image.load('Dragon.png')
    portaloImg = pygame.image.load('PortalO.png')
    portalbImg = pygame.image.load('PortalB.png')
    
    #selected character
    
    CHARACTERTUPLE = (snapeImg, dobbyImg, hagridImg, ronImg, potterImg, malfoyImg, hermioneImg, voldemortImg, dumbleImg)
    CHARACTER = CHARACTERTUPLE[playerChar]
    SNITCH = snitchImg
    
    PlayCoord=(0,0)
    pygame.mixer.music.load('Vines.mp3') #Play Music
    pygame.mixer.music.play(1, 0.0)
    snitchObj = Snitch()
    charObj = Character()
    obj = Objects()
    endCoords=charObj.makeCoord()
    PlayCoord=endCoords[0]
    SnitchCoord=endCoords[1]
    beginPos = PlayCoord
    SbeginPos = SnitchCoord
    keyChoices = [273, 275, 274, 276]
    keys=pygame.key.get_pressed()
    initialSum = sum(keys)
    charMove=3
    
    #make extras objects
    monsterBookObj = Extras(monsterBookImg)
    polyObj = Extras(polyImg)
    snakeObj = Snake(snakeImg)
    swordObj = Extras(swordImg)
    dragonObj = Extras(dragonImg)
    portaloObj = Extras(portaloImg)
    portalbObj = Extras(portalbImg)
    floor = charObj.getFloor()
    
    #make extras coordinates
    MonsterCoord,floor = monsterBookObj.draw(floor,monsterBookObj.getImg())
    PolyCoord,floor = polyObj.draw(floor,polyObj.getImg())
    SnakeCoord, floor = snakeObj.draw(floor,snakeObj.getImg())
    SwordCoord, floor = swordObj.draw(floor,swordObj.getImg())
    DragonCoord, floor = dragonObj.draw(floor,dragonObj.getImg())
    PortalOCoord, floor = portaloObj.draw(floor,portaloObj.getImg())
    PortalBCoord, floor = portalbObj.draw(floor,portalbObj.getImg())
    
    
    global polyCharacter
    snitch,book,poly,sword,dragon,snake,player,portalo,portalb = 'snitch','book','poly','sword','dragon','snake','player','portalo','portalb'
    polyCharacter = [CHARACTER]
    hasDict = {snitch:False,book:False,poly:False,sword:False,dragon:False,snake:False,portalo:False,portalb:False,player:True}
    isDict = {snitch:False,book:False,poly:False,sword:False,dragon:False,snake:False,player:True}
    coordDict = {player:PlayCoord,snitch:SnitchCoord,book:MonsterCoord,poly:PolyCoord,sword:SwordCoord,dragon:DragonCoord,snake:SnakeCoord,portalo:PortalOCoord,portalb:PortalBCoord}
    objDict = {player:charObj,snitch:monsterBookObj,book:monsterBookObj,poly:polyObj,sword:swordObj,dragon:dragonObj,snake:snakeObj,portalo:portaloObj,portalb:portalbObj}
    otherMove = 0
    moving = [book,snake,dragon]
    appendTime = False
    goPortal=True
    poss = polyCharacter[0]
    while poss == CHARACTER:
        poss = random.choice(CHARACTERTUPLE)
    polyCharacter.append(poss)
    
    while True: # main game loop
        #starts music
        if pygame.mixer.music.get_busy():
            pass
        else:
            pygame.mixer.music.load('Trancendentalism.mp3') #Play Music
            pygame.mixer.music.play(1, 0.0)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
    
        #moves snitch
        if isDict[snitch] == False and hasDict[snitch] == False:
            isDict[snitch] = snitchObj.checkFor(coordDict[snitch],coordDict[player])
            if isDict[snitch] == False:
                coordDict[snitch]=snitchObj.move(coordDict[snitch],coordDict[player],SNITCH,coordDict)
            else:
                hasDict[snitch] = True
        else:
            hasDict[snitch] == True
        
        #checks to see if the player gets any of the extras
        #if the extra is the polyjuice potion, it sets the character equal to the new character
        #if extra is one of the portals, it sets character's coord to other portal's coord
        for s in hasDict:
            if hasDict[s] == False:
                hasDict[s] = snitchObj.checkFor(coordDict[s],coordDict[player])
                if s == poly and hasDict[poly] == True:
                    appendTime = True
                if s == portalb and hasDict[portalb] == True:
                    goPortal=False
                    
                elif s == portalo and hasDict[portalo] == True:
                    goPortal=False
                
            if hasDict[poly] == True and appendTime == True:
                length = len(polyCharacter)
                CHARACTER = polyCharacter[length-1]
                poss = polyCharacter[length-1]
                while poss == polyCharacter[length-1]:
                    poss = random.choice(CHARACTERTUPLE)
                polyCharacter.append(poss)
                appendTime = False

        #checks to see if the snake has found the player
        if objDict[snake].checkFor(coordDict[snake],coordDict[player]) == True:
            if hasDict[sword] == True:
                soundObj = pygame.mixer.Sound('SnakeHit.wav')
                soundObj.play()
                pygame.Surface.blit(DISPLAYSURF, CHARACTER, (coordDict[snake][0], coordDict[snake][1], pixelBox, pixelBox))
                coordDict[snake] = [-1,-1]
            else:
                isDict,hasDict,coordDict,objDict = objDict[snake].loseItems(isDict,hasDict,coordDict,objDict)
                soundObj = pygame.mixer.Sound('SnakeBite.wav')
                soundObj.play()
            
        #moves the book, dragon, and snake
        if otherMove == 3:
            for m in moving:
                if isDict[m] == False and hasDict[m] == False:
                    isDict[m] = objDict[m].checkFor(coordDict[m],coordDict[player])
                    if isDict[m] == False:
                        coordDict[m]=objDict[m].move(coordDict[m],coordDict[player],objDict[m].getImg(),coordDict)
                    else:
                        hasDict[m] = True
                else:
                    hasDict[m] == True
            
            otherMove = 0
        else:
            otherMove += 1

    
            
        
        keys =pygame.key.get_pressed()
        if sum(keys) - initialSum==1:
            if keys[K_ESCAPE]:
                pygame.quit()
                sys.exit()
            elif charMove==3:
                keysPressedIndex = keys.index(1)
                
                #checks to teleport
                if hasDict[portalo]==True and goPortal==False:# and s == portalo:
                    coordDict[player]=coordDict[portalb]
                    pygame.Surface.blit(DISPLAYSURF, CHARACTER, (coordDict[portalo][0], coordDict[portalo][1], pixelBox, pixelBox))
                    pygame.Surface.blit(DISPLAYSURF, floorImg, (coordDict[portalo][0], coordDict[portalo][1], pixelBox, pixelBox))
                    pygame.Surface.blit(DISPLAYSURF, objDict[portalo].getImg(), (coordDict[portalo][0], coordDict[portalo][1], pixelBox, pixelBox))
                    goPortal=True
                    hasDict[portalo]=False
                
                elif hasDict[portalb] == True and goPortal==False:# and s == portalb:
                    coordDict[player]=coordDict[portalo]
                    pygame.Surface.blit(DISPLAYSURF, CHARACTER, (coordDict[portalb][0], coordDict[portalb][1], pixelBox, pixelBox))
                    pygame.Surface.blit(DISPLAYSURF, floorImg, (coordDict[portalb][0], coordDict[portalb][1], pixelBox, pixelBox))
                    pygame.Surface.blit(DISPLAYSURF, objDict[portalb].getImg(), (coordDict[portalb][0], coordDict[portalb][1], pixelBox, pixelBox))
                    goPortal=True
                    hasDict[portalb]=False
                    
                try:
                    #moves character
                    keyChoicesIndex = keyChoices.index(keysPressedIndex)
                    if objDict[player].canMove(coordDict[player],keyChoicesIndex):
                        coordDict[player] = objDict[player].move(keyChoicesIndex,coordDict[player],coordDict,objDict,hasDict)
                    else:
                        coordDict[player] = objDict[player].noMove(coordDict[player],coordDict,objDict)
                except:
                    pass
                charMove=0
            else:
                charMove+=1
        
        pygame.time.delay(50)
        pygame.display.update()
        
        #checks to see if the player has all the objects and is on the exit
        #if theTerminator == True it restarts the game
        if theTerminator(coordDict[player],hasDict):
            pygame.mixer.stop()
            DISPLAYSURF = pygame.display.set_mode((1280, 800))
            mischiefLGImg = pygame.image.load('MischiefManaged.png')
            pygame.Surface.blit(DISPLAYSURF, mischiefLGImg, (0, 0, 1280, 800))
            soundObj = pygame.mixer.Sound('crazyclimberfall.wav')
            soundObj.play()
            pygame.display.update()
            pygame.time.wait(2000)            
            RUNTHEGAME(playerChar)
            
            
RUNTHEGAME(playerChar)        

# <codecell>

pygame.quit()
sys.exit

