import pygame
from pygame.locals import *
import random
import time

## Type "pygame.display.quit()" in the GUI to exit

## The first center is 87x87
## The second center is 187x187
## The third center is 287x287

## Enter tile info here
bList = ['Theseus','Eros','Oedipus','Perseus','Jason','Hercules','Odysseus','Aeneas']
iList = ['753 B.C.','509 B.C.','27 B.C.','476 B.C.','264 B.C.','146 B.C.','60 B.C','43 B.C.','72 B.C.','44 B.C.']
nList = ['Numa Popilius','Tarqunius','Octavian','Iulius Caesar','Romulus','Tiberius','Hadrian']
gList = ['Graeae','Fates','Furies','Gorgons','Arachne','Tantulus']
oList = ['Apollo','Diana','Vulcan','Jupiter','Prometheus','Neptune','Venus']
mainList = [bList, iList, nList, gList, oList]

def CheckRun():
    listCheck = ListCheck()
    if listCheck == False:
        print ("Lists are not the same length, please correct.")
    elif listCheck == True:
        main()

## Resets Checklist to a full list containing all items in mainList
def FillCheckList(checkList):
    length = ( len(bList) + len(iList) + len(nList) + len(gList) + len(oList) )
    b = len(bList)
    i = len(iList)
    n = len(nList)
    g = len(gList)
    o = len(oList)
    count = -1
        
    for x in range (length-1):
        count += 1
        if count <= (b-1):
            checkList.append(bList[x])
        elif count <= ( (b+i) -1):
            checkList.append(iList[x- (b) ])            
        elif count <= ( (b+i+n) -1):
            checkList.append(nList[x- (b+i) ])            
        elif count <= ( (b+i+n+g) -1):
            checkList.append(gList[x- (b+i+n) ])            
        elif count <= ( (b+i+n+g+o) -1):
            checkList.append(oList[x- (b+i+n+g) ])            
    return checkList

## Checks equal length for all the lists
def ListCheck():
    b = len(bList)
    i = len(iList)
    n = len(nList)
    g = len(gList)
    o = len(oList)

    if (b >= 5) and (i >= 5) and (n >= 5) and (g >= 5) and (i >= 5):
       return True
    else:
        return False

## Returns a random letter from a given list
def GetLetter(mainList,checkList):
    final = []
    for x in range(5):
        randomNum = random.randint(0,4)
        currentList = mainList[x]

        while (currentList[randomNum] in checkList) == False:
            randomNum = random.randint(0,len(currentList)-1)

        final.append(currentList[randomNum])
        checkList.remove(currentList[randomNum])

    return final

##########################################################
########## Everything after is universal code ############
##########################################################

## Screenshot function
    ## All varibles are purely for the name of the save file
def TakeScreenshot(screen):
    time_taken = time.asctime(time.localtime(time.time()))
    time_taken = time_taken.replace(" ", "_")
    time_taken = time_taken.replace(":", ".")
    save_file = "H:/" +time_taken+ ".png"
    pygame.image.save(screen, save_file)
    print ("A screen shot has been taken and saved as : %s") % (save_file)

def BuildBingo():
    ## display BINGO
    font = pygame.font.SysFont("bold", 40, True, False)
    bingo = ['B','I','N','G','O']
    
    y = -1
    for x in bingo:
        y += 1
        current = font.render(x, 1, (0,0,0))
        rectDims = pygame.Surface.get_rect(current)
        width = rectDims[2]
        height = rectDims[3]
        screen.blit(current, (37+100*y-width/2, 37-height/2))

def BuildLists():
    checkList = []
    checkList = FillCheckList(checkList)
    
    ## setup for the font
                          ####(font, size, bold, italic) 
    font = pygame.font.SysFont("Arial", 16, False, True)

    ## checkList catches repeat items from occuring
        ## x and y correspond to the x and y axis
    for x in range (5):
        currentList = GetLetter(mainList, checkList)
         
        for y in range (5):
            text = font.render( (currentList[y]) , 1, (0, 0, 0))

            rectDims = pygame.Surface.get_rect(text)
            width = rectDims[2]
            height = rectDims[3]
            ## this is where you set the center point of each line
            textpos = ( (37 + 100*y)-width/2, (137 + 100*x)-height/2 ) 
            screen.blit(text, textpos)

## Main exe.   
def main():    
    pygame.init()
    global screen

    ## build the window
    pygame.display.set_caption('Bingo')
    screen = pygame.display.set_mode((475,575))
    pygame.mouse.set_visible(1)

    ## build the background
    background = pygame.image.load('BingoFinal.png').convert()
    screen.blit(background,(0,0))

    ## build the text
    BuildBingo()
    BuildLists()
    
    running = True

    ## keep updating
    clock = pygame.time.Clock()
    while 1:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                screen.blit(background,(0,0))
                BuildBingo()
                BuildLists()
            elif event.type == KEYDOWN and event.key == K_F1:
                TakeScreenshot(screen)

        if running == False:
            break
        else:
            pygame.display.flip()
        
    ##pygame.image.save(screen, "currentFile.png")

CheckRun()
