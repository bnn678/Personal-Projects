import pygame
from pygame.locals import *
import time
import os, sys

##class Mighty_Man(pygame.sprite.Sprite):    
##    def __init__(self, color, width, height):
##        pygame.sprite.Sprite.__init__(self)
##        self.image = Mighty_Man.png
##        self.image = image.convert()
##        self.rect = self.image.get_rect()
##
##    def Slice():
##        current_man = man_img_slice
##    def Unslice():
##        current_man = man_img

def load_image(name, colorkey=None):
    fullname = os.path.join('Sprites', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image #, image.get_rect()

def Update_Screen():
    ## Clean the screen of past images
    screen.blit(background, (0,0))
    ## Rebuild rocks in each img
    for x in rockpos_list:
        screen.blit(RockImg, x)
        blockade_list.append(x)
    ## Build correct man_img at correct pos
    screen.blit(current_man, (currentpos))

def Can_Move():
    if currentpos in blockade_list:
        print 'f'
        return False
    else:
        print 't'
        return True

def Main():
    pygame.init()

    ## varible declarations
    global screen
    global background
    global blockade_list

    blockade_list = []

    ## build the window
    pygame.display.set_caption('Mighty Man')
    screen = pygame.display.set_mode((600,400))
    pygame.mouse.set_visible(1)

    ## build the background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    screen.blit(background,(0,0))

    ## init main character imgs
    global man_img
    global man_imgSlice
    global current_man
##    man_img = pygame.image.load('Mighty_Man_Slice.png').convert()
##    man_img_slice = pygame.image.load('Mighty_Man_Slice.png').convert()
##    current_man = man_img
    man_img = load_image('Man2.png')
    man_img_slice = load_image('Mighty_Man_Slice.png')
    current_man = man_img

    ## init rock imgs
    global RockImg    
##    RockImg = pygame.image.load('Rock.png').convert()
    RockImg = load_image('Rock.png')

    print (type(man_img))
    print (type(man_img_slice))
    print (type(RockImg))
    
    global currentpos
    currentpos = (90, 50)
    global rockpos_list
    rockpos_list = [(90,90),(80,80)]

    Update_Screen()

    ## keep updating
    clock = pygame.time.Clock()
    while 1:
        clock.tick(60)

        for event in pygame.event.get():
            #######################################
            if event.type == QUIT:
                return pygame.display.quit()
            
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return pygame.display.quit()
            #######################################                
            elif event.type == KEYDOWN and event.key == K_a\
                 or event.type == KEYDOWN and event.key == K_LEFT:
                currentpos = ( currentpos[0] - 5, currentpos[1] )

            elif event.type == KEYDOWN and event.key == K_d\
                 or event.type == KEYDOWN and event.key == K_RIGHT:
                currentpos = ( currentpos[0] + 5, currentpos[1] )

            elif event.type == KEYDOWN and event.key == K_w\
                 or event.type == KEYDOWN and event.key == K_UP:
                currentpos = ( currentpos[0], currentpos[1] - 5 )

            elif event.type == KEYDOWN and event.key == K_s\
                 or event.type == KEYDOWN and event.key == K_DOWN:
                currentpos = ( currentpos[0], currentpos[1] + 5 )
            #######################################
            elif event.type == KEYDOWN and event.key == K_SPACE:
                current_man = man_img_slice
            elif event.type == KEYUP and event.key == K_SPACE:
                current_man = man_img

        Update_Screen()
        pygame.display.flip()

Main()
