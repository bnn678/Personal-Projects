import pygame
from pygame.locals import *
import random
import time

## Type "pygame.display.quit()" in the GUI to exit

## The first center is 87x87
## The second center is 187x187
## The third center is 287x287
class Game_Info_1(object):
    ## Enter tile info here
    bList = ['Jason','Hercules','Theseus','Odesseus','e','90','80']
    iList = ['753 B.C.','509 B.C.','27 B.C.','476 A.D.','264 B.C.','146 B.C.','60 B.C.','43 B.C.','72 B.C.', '44 B.C.']
    nList = ['k','l','m','n','o','90','80']
    gList = ['p','q','r','s','t','90','80']
    oList = ['u','v','w','x','y','90','80']
    mainList = [bList, iList, nList, gList, oList]

    def CheckRun():
        listCheck = ListCheck()
        if listCheck == False:
            print ("Lists are not the minimum length, please correct.")
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

        if (b > 5) and (i > 5) and (n > 5) and (g > 5) and (i > 5):
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

################# New Class #####################

class Game_Info_2(object):
    ## Enter tile info here
    mainList = ['I','V','M','C','II','IV','VIII',
                'XII','g','h','i','j','90','80',
                'k','l','m','n','o','90','80',
                'p','q','r','s','t','90','80',
                'u','v','w','x','y','90','80', '70', '60']

    ## Resets Checklist to a full list containing all items in mainList
    def FillCheckList(checkList):
        for x in range( len(mainList)-1 ):
            checkList.append(mainList[x])
        return checkList

    ## Returns a random letter from a given list
    def GetLetter(mainList, checkList):
        final = []
        for x in range(5):
            randomNum = random.randint(0,len(mainList)-1)
            
            while (mainList[randomNum] in checkList) == False:
                randomNum = random.randint(0,len(mainList)-1)
                
            final.append(mainList[randomNum])
            checkList.remove(mainList[randomNum])
        return final

##########################################################
########## Everything after is universal code ############
##########################################################

def GetGameType():
    game_type = raw_input("Would you like to enter words into each separate line: (y/n) ")
    if game_type == 'y':
        className = Game_Info_1
    elif game_type == 'n':
        className = Game_Info_2
    else:
        GetGameType()
    return className

game_type = GetGameType()



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
    game_type.FillCheckList(checkList)
    
    ## setup for the font
                          ####(font, size, bold, italic) 
    font = pygame.font.SysFont("Arial", 16, False, True)

    ## checkList catches repeat items from occuring
        ## x and y correspond to the x and y axis
    for x in range (5):
        currentList = Game_Info_1.GetLetter(mainList, checkList)
         
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

    ## build text
    BuildBingo()
    BuildLists()

    ## keep updating
    clock = pygame.time.Clock()
    while 1:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                return pygame.display.quit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return pygame.display.quit()
            elif event.type == MOUSEBUTTONDOWN:
                screen.blit(background, (0,0))
                BuildBingo()
                BuildLists()
            elif event.type == KEYDOWN and event.key == K_F1:
                TakeScreenshot(screen)
        pygame.display.update()

main()
