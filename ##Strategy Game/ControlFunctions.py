import MapInfo

########################################################################
##    A function to find the point in the grid where the mouse was clicked
########################################################################
def GetGridPoint( mouse_pos ):
    x = mouse_pos[0]
    x_found = 0
    for x_point in range( MapInfo.grid_spaces ):
        x_min = ( x_point * MapInfo.space_length )
        x_max = ( (x_point+1) * (MapInfo.space_length) )
        if x >= x_min and x < x_max:
            break 
    x_found = x_point

    y = mouse_pos[1]
    y_found = 0
    for y_point in range( MapInfo.grid_spaces ):
        y_min = ( y_point * MapInfo.space_length )
        y_max = ( (y_point+1) * (MapInfo.space_length) )
        if y >= y_min and y < y_max:
            break
    y_found = y_point

    print( '' )
    print( 'Mouse clicked at: (' + str(x_found) +','+ str(y_found)+')' )
    return[ x_found, y_found ]


########################################################################
##    A function that converts a grid point to a pixel point
########################################################################
def ConvertGridPoint( pos ):
    new_pos = []
    for coord in pos:
        new_coord = coord * ( MapInfo.screen_length / MapInfo.grid_spaces ) ## Takes the grid coord and multiples it by the number of pixels in each grid space
        new_pos.append( new_coord )
    return new_pos


########################################################################
##    A function that checks whether or not a space is occupied and
##        returns name of image if it is occupied
##    pos should be grid point
##    occupied_points will be pixel points
########################################################################
def GetObjectAt( pos ):
    pos = ConvertGridPoint( pos )
    
    for count in range( len( MapInfo.character_info)):
        occupied_point = MapInfo.character_info[count][0]
        occupied_point = ConvertGridPoint( occupied_point )

        if occupied_point == pos:
            return( count )
    return( None )


########################################################################
##    Given id of character to move and new location to move to,
##        this function moves characters on the map
########################################################################
def Move( character_id, new_pos ):   
    MapInfo.character_info[character_id][0] = new_pos


########################################################################
##    Attacks the specified character
########################################################################
def Attack( character_id, character_attacked ):
    
    ## Health of the attacked character =  original health - attacking character attack damage
    MapInfo.character_info[character_attacked][2][0] -=  MapInfo.character_info[character_id][2][1]

    if MapInfo.character_info[character_attacked][2][0] > 0:
        print( ' Character number '+ str(character_attacked) +' now has '+ str( MapInfo.character_info[character_attacked][2][0] ) +' health left.')
        print( ' Character number '+ str(character_id) +' now has '+ str( MapInfo.character_info[character_id][2][0] ) +' health left.')
    elif MapInfo.character_info[character_attacked][2][0] <= 0:
        MapInfo.character_info.remove( MapInfo.character_info[character_attacked] )
        print( ' Killed enemy character.')


########################################################################
##    Finds all possible moves for a character to make
########################################################################
def CanMove( character_id ):
    character_info = MapInfo.character_info[character_id]
    possible_moves = []
    attack_moves = []

    character_pos = character_info[0]
    move_range = character_info[2][3] ## Character speed
    attack_range = character_info[2][4]

    x = character_pos[0]
    y = character_pos[1]

    top_limit = y - move_range
    left_limit = x - move_range

    for count in range( move_range*2+1 ): ## Change in y
        for otherNum in range( move_range*2+1 ): ## Change in x
            new_x = left_limit + otherNum
            new_y = top_limit + count

            if(abs( new_x - x ) + abs( new_y - y )) <= move_range:
                object_collision = GetObjectAt( [new_x, new_y] )
                if object_collision == None:
                    possible_moves.append( [new_x, new_y] )

    x = character_pos[0]
    y = character_pos[1]

    top_limit = y - attack_range
    left_limit = x - attack_range

    for count in range( attack_range*2+1 ): ## Change in y
        for otherNum in range( attack_range*2+1 ): ## Change in x
            new_x = left_limit + otherNum
            new_y = top_limit + count

            if(abs( new_x - x ) + abs( new_y - y )) <= attack_range:
                attack_moves.append( [new_x, new_y] )

    return( [possible_moves,attack_moves] )


########################################################################
##    Get a list of rects with grey colors
########################################################################
def GetGreyRectPos():
    grey_pos = []
    for rect in MapInfo.rect_info:
        x = rect[0]
        y = rect[1]
        color = rect[4]
        if color == MapInfo.grey:
            grey_pos.append( [x,y] )
    return grey_pos


########################################################################
##    Switch turn from one team to the other
########################################################################
def SwitchTurn(turn):
    if turn == 0:
        return 1
    if turn == 1:
        return 0

    
