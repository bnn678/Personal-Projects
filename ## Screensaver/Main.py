import pygame
from pygame.locals import *
import time

def ChangeScreenColor(currentRGB, hasMaxed):
    red = currentRGB[0]
    green = currentRGB[1]
    blue = currentRGB[2]

    changeScale = 5

    if hasMaxed == True:
        if red != 255:
            currentRGB = (red + changeScale, green, blue)
        elif green != 255:
            currentRGB = (red, green + changeScale, blue)
        elif blue != 255:
            currentRGB = (red, green, blue + changeScale)
            
    elif hasMaxed == False:
        if red != 0:
            currentRGB = (red - changeScale, green, blue)
        elif green != 0:
            currentRGB = (red, green - changeScale, blue)
        elif blue != 0:
            currentRGB = (red, green, blue - changeScale)
            
    return currentRGB

def Main():
    pygame.init()

    ## varible declarations
    global screen
    global background

    ## height and width of the screen
    screenDims = (800, 800)
    ## rate colors change on screen
    colorChangeScale = 5
    ## total number of times color can get darker
    colorChangeMax = 255/colorChangeScale
    ## current red, green, and blue amounts
    currentRGB = (250,250,250)
    ## Returns True if the RGB scale is bottomed (0,0,0) or False if it is maxed (255,255,255)
    hasMaxed = False

    ## build the window
    pygame.display.set_caption('Screensaver')
    screen = pygame.display.set_mode(screenDims)
    pygame.mouse.set_visible(1)

    ## build the background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(currentRGB)
    screen.blit(background,(0,0))

    ## keep updating
    clock = pygame.time.Clock()
    while 1:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                return pygame.display.quit()
            
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return pygame.display.quit()

        ## Finds whether the RGB should be increasing or decreasing
        if currentRGB == (255,255,255):
            hasMaxed = False
        elif currentRGB == (0,0,0):
            hasMaxed = True
            
        currentRGB = ChangeScreenColor(currentRGB, hasMaxed)

        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill(currentRGB)
        screen.blit(background,(0,0))
    
        pygame.display.flip()

Main()
