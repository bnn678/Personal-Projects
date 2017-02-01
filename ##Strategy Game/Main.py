import time, sys, os
from pygame.locals import *

from DisplayFunctions import *
import MapInfo

space_length = MapInfo.space_length
screen_length = MapInfo.screen_length
    
########################################################################
########################################################################
########################################################################
def Main():
    BuildScreen()
    
    characterSelected = False
    buildingSelected = False
    turn =  1 ## 0 = red turn, 1 = blue turn
    
    selected = None
    old_moves = None

    ## keep updating
    clock = pygame.time.Clock()
    while 1:
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == QUIT: ## QUIT Section
                return pygame.display.quit()
            
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return pygame.display.quit()

            elif event.type == MOUSEBUTTONDOWN: ## Mouse click Section
                mouse_pos = pygame.mouse.get_pos()
                mouse_pos = GetGridPoint( mouse_pos )
                
                character_id = GetObjectAt( mouse_pos )
                
    ## Use Characters
                if characterSelected == True:
                    character_attacked = GetObjectAt( mouse_pos )
                    
                    ## Move
                    if mouse_pos in possible_moves and character_attacked == None:
                        Move( selected, mouse_pos )
                        turn = SwitchTurn( turn )
                        
                    ## Attack
                    elif character_attacked != None and mouse_pos in attack_moves and MapInfo.character_info[character_attacked][3] == 'fighter':
                        Attack( selected, character_attacked )
                        turn = SwitchTurn( turn )
                        character_id = None

                    ## No move
                    else:
                        print(' Not a valid move')

                    RemoveMoves( moves )
                    RemoveCharacterInfo()
                    characterSelected = False
                    buildingSelected = False
                    

    ## Build Characters
                elif buildingSelected == True:
                    grey_pos = GetGreyRectPos()
                    for count in range( len(grey_pos)):
                        pos = grey_pos[count]
                        if mouse_pos == pos:
                            build_pos = MapInfo.character_info[ selected ][0]
                            build_pos = [build_pos[0], build_pos[1] - 1]
                            character_name = MapInfo.SpawnerTextInfo[count]

                            if character_name != 'Cancel':
                                if turn == 0:
                                    character_name = 'Red_' + character_name
                                elif turn == 1:
                                    chateracter_name = 'Blue_' + character_name
                                    print(turn, character_name)
                                print( character_name )
                                BuildCharacter( build_pos, character_name )

                            buildingSelected = False
                            RemoveSpawnerInfo()
                            
    ## Select Characters
                elif character_id != None and characterSelected == False:
                    try:
                        RemoveSpawnerInfo()
                    except( IndexError ):
                        pass
                
                    object_type = MapInfo.character_info[character_id][3]
                    selected = character_id
                    character_color = MapInfo.character_info[character_id][4]

                    if character_color == turn:
                        ## Soldiers
                        
                        if object_type == 'fighter':
                            old_pos = MapInfo.character_info[character_id][0]
                            characterSelected = True
                            print(' Selected '+str( MapInfo.character_info[character_id][1] ))

                            ## Find and display possible moves
                            moves =  CanMove( character_id )
                            possible_moves = moves[0]
                            attack_moves = moves[1]
                            DisplayMoves( moves )
                            DisplayCharacterStats( character_id )

                        ## Buildings
                        elif object_type == 'building':
                            buildingSelected = True
                            DisplaySpawnerInfo()


            elif event.type == KEYDOWN: ## Key press section
                if event.key == K_LCTRL: ## Undo a move
                    try:
                        Move( selected, old_pos )
                    except( TypeError ):
                        print(' No move to undo.')

            UpdateScreen()
            pygame.display.flip()
Main()
