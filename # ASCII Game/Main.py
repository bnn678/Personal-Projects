map_height = 5
map_width = 10

# creates the map
the_map = []
for y in range(map_height):
    row = []    
    for x in range(map_width):
        row.append(' ')
    the_map.append(row)

def Print_Map(the_map = the_map):
    for item in the_map:
        row = str(item)

        row = row.replace("'","")
        row = row.replace(",","")
        
        print(row)

Print_Map()
