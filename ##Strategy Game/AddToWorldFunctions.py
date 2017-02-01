import MapInfo

########################################################################
##    Adds a rectangle to the world
########################################################################
def BuildRect( grid_x, grid_y, length, height, color ):
    x = ( grid_x )
    y = ( grid_y )
    length = ( length * MapInfo.space_length ) - 1
    height = ( height * MapInfo.space_length ) - 1
    
    MapInfo.rect_info.append( [x, y, length, height, color] )

def BuildTextbox( grid_x, grid_y, text ):
    MapInfo.text_info.append( [grid_x, grid_y, text] )

def BuildCharacter( build_pos, character_name ):
    newInfo = []
    for info in MapInfo.characters[character_name]:
        newInfo.append( info )
    newInfo[0] = build_pos
    MapInfo.character_info.append( newInfo )
