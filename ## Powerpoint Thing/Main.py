import pygame
from pygame.locals import *
import time

main_displays = ['Blood','Sleep','Manhood','Birds','Sight','Naivete','Destiny'
                 ,'Greed','Water','Fear','Murder','Supernatural','Cleanliness'
                 ,'Manipulation','Mind','Guilt','Envy','18','19','20','21','22'
                 ,'23','24','25']
main_defs = ['1x','2x','3x','4x','5x','6x','7x','8x','9x','10x','11x','12x'
             ,'13x','14x','15x','16x','17x','18x','19x','20x','21x','22x'
             ,'23x','24x','25x']
main_defs2 = ['x','x','x','x','x','x','x','x','x','x','x','x'
             ,'13x','14x','15x','16x','17x','18x','19x','20x','21x','22x'
             ,'23x','24x','25x']

def Get_Current_Item(current_num):
    final = []
    final.append(main_displays[current_num])
    final.append(main_defs[current_num])
    final.append(main_defs2[current_num])

    return final

def Build_Item_1():
    font = pygame.font.SysFont("Arial", 16, False, True)
    
    text = Get_Current_Item(current_num)
    item_1 = text[0] ; item_1 = font.render(item_1, 1, (255, 255, 255))

    rectDims = pygame.Surface.get_rect(screen)
    width_screen = rectDims[2]
    heigth_screen = rectDims[3]
    
    rectDims = pygame.Surface.get_rect(item_1)
    width_item = rectDims[2]
    heigth_item = rectDims[3]
    
    textpos = ( (width_screen/2)-(width_item/2), (heigth_screen/2)-(heigth_item/2))
    
    screen.blit(item_1, textpos)

def Build_Item_2():
    font = pygame.font.SysFont("Arial", 16, False, True)
    
    text = Get_Current_Item(current_num)
    
    item_2 = text[1] ; item_2 = font.render(item_2, 1, (255, 255, 255))
    
    rectDims = pygame.Surface.get_rect(screen)
    width_screen = rectDims[2]
    heigth_screen = rectDims[3]
    
    rectDims = pygame.Surface.get_rect(item_2)
    width_item = rectDims[2]
    heigth_item = rectDims[3]
    
    textpos = ( (width_screen/2)-(width_item/2), (heigth_screen/3)-(heigth_item/2))
    
    screen.blit(item_2, textpos)

    ########### SECOND SET OF TEXT #############

    font = pygame.font.SysFont("Arial", 16, False, True)
    
    text = Get_Current_Item(current_num)
    
    item_3 = text[2] ; item_3 = font.render(item_3, 1, (255, 255, 255))
    
    rectDims = pygame.Surface.get_rect(screen)
    width_screen = rectDims[2]
    heigth_screen = rectDims[3]
    
    rectDims = pygame.Surface.get_rect(item_3)
    width_item = rectDims[2]
    heigth_item = rectDims[3]
    
    textpos = ( (width_screen/2)-(width_item/2), (2*(heigth_screen)/3)-(heigth_item/2))
    
    screen.blit(item_3, textpos)

def Build_End_Screen():
    font = pygame.font.SysFont("Arial", 16, False, True)
    
    text = "That is the end of the presentation."
    text = font.render(text, 1, (255, 255, 255))
    
    rectDims = pygame.Surface.get_rect(screen)
    width_screen = rectDims[2]
    heigth_screen = rectDims[3]
    
    rectDims = pygame.Surface.get_rect(text)
    width_item = rectDims[2]
    heigth_item = rectDims[3]
    
    textpos = ( (width_screen/2)-(width_item/2), (heigth_screen/2)-(heigth_item/2) )
    
    screen.blit(text, textpos)

def Clear_Screen():
    screen.blit(background, (0,0))

def Main():
    pygame.init()

    ## varible declarations
    global screen
    global background
    global current_num
    current_num = 0
    first_space_press = True

    ## build the window
    pygame.display.set_caption('Powerpoint')
    screen = pygame.display.set_mode((600,400))
    pygame.mouse.set_visible(1)

    ## build the background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    screen.blit(background,(0,0))

    Clear_Screen()
    Build_Item_1()

    ## keep updating
    clock = pygame.time.Clock()
    while 1:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                return pygame.display.quit()
            
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return pygame.display.quit()
            
            elif event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed() == (1, 0, 0) \
                 or event.type == KEYDOWN and event.key == K_z:
                current_num += 1
                if current_num < ( len(main_displays) ):
                    Clear_Screen()
                    Build_Item_1()
                elif current_num < ( len(main_displays)+1 ):
                    Clear_Screen()
                    Build_End_Screen()
                else:
                    return pygame.display.quit()

            elif event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed() == (0, 0, 1) \
                 or event.type == KEYDOWN and event.key == K_x:
                if current_num > 0:
                    current_num -= 1
                Clear_Screen()
                Build_Item_1()
                
            elif event.type == KEYDOWN and event.key == K_SPACE:
                if current_num < len(main_displays):
                    if first_space_press == True:
                        Clear_Screen()
                        Build_Item_2()
                    
                        first_space_press = False
                        
                    elif first_space_press == False:
                        Clear_Screen()
                        Build_Item_1()
                        
                        first_space_press = True
                

        pygame.display.update()

if len(main_displays) == len(main_defs):
    Main()
