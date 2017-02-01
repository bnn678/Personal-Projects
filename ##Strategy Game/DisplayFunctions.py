## dimensions for screen stuff
import pygame
from pygame.locals import *

from ControlFunctions import *
from AddToWorldFunctions import *

import MapInfo

pygame.font.init()

########################################################################
##    A function to initilize the screen to the given varible specifications
##        moved out of Main() for formatting
########################################################################
def BuildScreen():
    global screen
    global background
    global fontobject
    
    ## sets up screen dimesions to varible specifications
    screenDims = (MapInfo.screen_length, MapInfo.screen_length) ## must be the same, for the grid to be a true grid

    ## build the window
    pygame.display.set_caption('Strategy Game')
    screen = pygame.display.set_mode(screenDims)
    pygame.mouse.set_visible(1)
    fontobject = pygame.font.Font( None, 18 )

##    s = pygame.Surface((1000,750))  # the size of your rect
##    s.set_alpha(128)                # alpha level
##    s.fill((255,255,255))           # this fills the entire surface
##    screen.blit( s, (0,0) )    # (0,0) are the top-left coordinates


########################################################################
##    A function to define the background of the map
########################################################################
def DisplayBackground():
    global background
    ## build the background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill( MapInfo.grass_green )

    screen.blit( background, (0,0) )

    DrawGridLines()


########################################################################
##    Draws the Grid lines for the background
########################################################################
def DrawGridLines():
    ## loop that draws the grid
    for count in range( MapInfo.grid_spaces ):
        ## Vertical lines
        pygame.draw.line( screen, MapInfo.black, ( (count*MapInfo.space_length), 0), ( (count*MapInfo.space_length), MapInfo.screen_length ) )
        ## Horizontal lines
        pygame.draw.line( screen, MapInfo.black, ( 0,(count*MapInfo.space_length)), ( MapInfo.screen_length, (count*MapInfo.space_length) ) )


########################################################################
##    Redisplay the background to clear the screen then
##        display characters at current positions
########################################################################
def UpdateScreen():
    DisplayBackground()

    for rect in MapInfo.rect_info:
        x = (rect[0] * MapInfo.space_length) + 1
        y = (rect[1] * MapInfo.space_length) + 1
        length = rect[2]
        height = rect[3]
        color = rect[4]

        rect_dims = [x,y,length,height]
        
        rect = pygame.draw.rect( screen, color, rect_dims )

    for textbox in MapInfo.text_info:
        x = textbox[0] * MapInfo.space_length
        y = textbox[1] * MapInfo.space_length
        text = textbox[2]
        
        screen.blit( fontobject.render( text, 1, MapInfo.black ), [x,y] )

    for character in MapInfo.character_info:
        sprite_name = character[1]
        sprite = ( pygame.image.load( 'Sprites/'+(sprite_name) ).convert() )
        
        pos = character[0]
        pos = ConvertGridPoint( pos )

        screen.blit(sprite, pos)


########################################################################
##    Display a blue box on all possible moves
########################################################################
def DisplayMoves( moves ):
    possible_moves = moves[0]
    attack_moves = moves[1]
    
    for point in possible_moves:
        grid_x = point[0]
        grid_y = point[1]
        BuildRect( grid_x, grid_y, 1, 1, MapInfo.move_blue )

    for point in attack_moves:
        grid_x = point[0]
        grid_y = point[1]
        BuildRect( grid_x, grid_y, 1, 1, MapInfo.red )


########################################################################
##    Remove a box from all attack moves
########################################################################
def RemoveMoves( moves ):
    possible_moves = moves[0]
    attack_moves = moves[1]
    rect_info = MapInfo.rect_info

    try:
        for point in possible_moves:
            rect_info.remove( rect_info[ len(rect_info) - 1] )
        for point in attack_moves:        
            rect_info.remove( rect_info[ len( rect_info )-1 ] )
    except( IndexError ):
        pass


########################################################################
##    Display the info box for the spawner
########################################################################
def DisplaySpawnerInfo():
    textItems = MapInfo.SpawnerTextInfo
    x_pos = MapInfo.spawnerInfoDisplayPoint[0]
    y_pos = MapInfo.spawnerInfoDisplayPoint[1]
    text_pos_x = x_pos + 2
    text_pos_y = y_pos + 1
    space_between = 2

    x_dim = 8
    y_dim = 2*len(textItems) + 1
    
    BuildRect( x_pos, y_pos, x_dim, y_dim, MapInfo.dark_grey )

    for count in range( len(textItems) ):
        BuildTextbox( text_pos_x + .125, text_pos_y + (count*space_between) + .125, textItems[count] )
        BuildRect( text_pos_x - 1, text_pos_y + (count*space_between), 1, 1, MapInfo.grey )


########################################################################
##    Remove the info box for the spawner
########################################################################
def RemoveSpawnerInfo():
    text_info = MapInfo.text_info
    rect_info = MapInfo.rect_info
    
    rect_info.remove( rect_info[ len(rect_info) - 1 ] )
    for count in range( len(MapInfo.SpawnerTextInfo) ):
        rect_info.remove( rect_info[ len( rect_info ) -1 ] )
        text_info.remove( text_info[ len(text_info) - 1 ] )
        

########################################################################
##    Displays an info box for the character selected
########################################################################
def DisplayCharacterStats( character_id ):
    length = 7; height = 6;
    x = MapInfo.grid_spaces - length - 1; y = 1;
    BuildRect( MapInfo.grid_spaces - length -1, y, length, height, MapInfo.grey )

    x += 1; y += 1
    space_between = 1

    BuildTextbox( x, y, 'Character ID: '+ str( character_id ) )
    BuildTextbox( x, y + space_between, 'Health: '+ str( MapInfo.character_info[character_id][2][0] ) )
    BuildTextbox( x, y + 2 * space_between, 'Attack: '+ str( MapInfo.character_info[character_id][2][1] ) )
    BuildTextbox( x, y + 3 * space_between, 'Defense: '+ str( MapInfo.character_info[character_id][2][2] ) )


    
########################################################################
##    Remove the info box for the character
########################################################################
def RemoveCharacterInfo():
    text_info = MapInfo.text_info
    rect_info = MapInfo.rect_info
    
    rect_info.remove( rect_info[ len(rect_info) - 1 ] )
    
    for count in range( 4 ):
        text_info.remove( text_info[ len(text_info) - 1 ] )


        
