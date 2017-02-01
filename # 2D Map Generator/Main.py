import random

threeXthree = ((2,2),
                [['|','~','|'],
                 ['|',' ','|'],
                 ['|','_','|']])

fiveXfive = ((3,3),
            [['|','~','~','~','|'],
             ['|',' ',' ',' ','|'],
             ['|',' ',' ',' ','|'],
             ['|',' ',' ',' ','|'],
             ['|','_','_','_','|']])

## CREATES A MAP OF WIDTH AND HEIGHT
def MakeEmptyMap( width, height ):
    new_map = []
    for i in range( height ):
        new_row = []
        
        for i in range( width ):
            new_row.append(' ')

        new_map.append( new_row )
    return new_map

## PRESENTS A FORMATTED DISPLAY OF THE MAP
def PrintMap( new_map ):
    for item in new_map:
        item = str( item )
        item = item.replace( ', ', '' )
        item = item.replace( "'", '' )
        print( item )

## ADDS THE GIVEN ROOM TO THE MAP
def AddRoom( new_map, map_x, map_y, center, room ):
    room_center = room[0]
    room = room[1]
    
    starting_point = ( center[0] - room_center[0], center[1] - room_center[1] )
    ending_point = ( center[0] + room_center[0] - 1, center[1] + room_center[1] - 1)

    ## IF THE ROOM IS TOO FAR LEFT
    while starting_point[0] < 0:
        starting_point = ( starting_point[0] + 1, starting_point[1] )
    ## IF THE ROOM IS TOO FAR UP
    while starting_point[1] < 0:
        starting_point = ( starting_point[0], starting_point[1] + 1 )
    ## IF THE ROOM IS TOO FAR RIGHT
    while ending_point[0] > map_x:
        ending_point = ( ending_point[0] - 1, ending_point[1] )
        starting_point = ( starting_point[0] - 1, starting_point[1] )
    ## IF THE ROOM IS TOO FAR DOWN
    while ending_point[1] > map_y:
        ending_point = ( ending_point[0], ending_point[1] - 1 )
        starting_point = ( starting_point[0], starting_point[1] - 1 )

    ## ACTUALLY INSERTING THE ROOM INTO THE MAP
    row_count = 0
    for row in room:
        column_count = 0
        
        for column in row:
            new_map[starting_point[1]+row_count][starting_point[0]+column_count] = room[row_count][column_count]
            column_count += 1

        row_count += 1

    return new_map



















def Main():
    map_x = 101
    map_y = 51
    room_types = {0:fiveXfive, 1:threeXthree }
    
    room_type = random.randint( 0, len(room_types)-1 )

    new_map = MakeEmptyMap( map_x, map_y )
    new_map = AddRoom( new_map, map_x, map_y, (0,0), fiveXfive )
    new_map = AddRoom( new_map, map_x, map_y, (0,51), fiveXfive )
    new_map = AddRoom( new_map, map_x, map_y, (101,51), fiveXfive )
    new_map = AddRoom( new_map, map_x, map_y, (101, 0), fiveXfive )
    new_map = AddRoom( new_map, map_x, map_y, (101, 25), threeXthree )
    ## POPULATE WITH ROOMS
    for x in range( 3 ):
        random_x = random.randint( 0, map_x )
        random_y = random.randint( 0, map_y )
        new_map = AddRoom( new_map, map_x, map_y, (random_x, random_y), threeXthree )
    

    PrintMap( new_map )
Main()
