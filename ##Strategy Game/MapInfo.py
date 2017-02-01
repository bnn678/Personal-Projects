## dimensions for screen stuff
##    ideally, grid boxes should be 16x16 pixels since png's are 16x16
screen_length = 800
grid_spaces = 50
space_length = screen_length / grid_spaces

## color RGB
white = [250,250,250]
black = [0,0,0]
grass_green = [0,204,0]
grey = [200,200,200]
dark_grey = [100,100,100]
red = [255, 0, 0]
move_blue = [100,100,255]

## Info for debugging
print('One grid space has dimensions: ['+str(space_length)+','+str(space_length)+'] pixels')
print('')

#######################################################################
##    This class should contain a list of the objects
##        on the map and their current locations
########################################################################

## Character info is set up in this format:
##    current_pos, sprite name, current_stats, object_type, team_color
##            team color: 0 = red turn, 1 = blue turn
character_info = []
## Rectangle info is set up in this format:
##    [ x_pos, y_pos, length, height, color
rect_info = []
## Textbox info is set up in this format:
##    [x_pos, y_pos, text]
text_info = []

## Character stats are set up in this format:
##    health, attack, defense, speed, attack_range
blue_archer_sprite_name = 'Archer_Blue.png'
red_archer_sprite_name = 'Archer_Red.png'
archer_stats = [10,3,2,3,2]
archer_type = 'fighter'

blue_soldier_sprite_name = 'Soldier_Blue.png'
red_soldier_sprite_name = 'Soldier_Red.png'
soldier_stats = [10,3,3,4,1]
soldier_type = 'fighter'

red_spawner_sprite_name = 'Spawner_Red.png'
blue_spawner_sprite_name = 'Spawner_Blue.png'
spawner_stats = [20, 0, 30, 0, 0]
spawner_type = 'building'

## Spawner Init
blue_spawner = [ (1,1), blue_spawner_sprite_name, spawner_stats[:], spawner_type, 1 ]
red_spawner = [ (grid_spaces-2,grid_spaces-2), red_spawner_sprite_name, spawner_stats[:], spawner_type, 0 ]
character_info.append( blue_spawner )
character_info.append( red_spawner )

## Archer Init
blue_archer = [ (10,0), blue_archer_sprite_name,  archer_stats[:], archer_type, 1 ]
red_archer = [ (grid_spaces-10,grid_spaces-1), red_archer_sprite_name, archer_stats[:], archer_type, 0 ]
character_info.append( blue_archer )
character_info.append( red_archer )

## Soldier Init
blue_soldier = [ (0,10), blue_soldier_sprite_name, soldier_stats[:], soldier_type, 1 ]
red_soldier = [ (grid_spaces-1, grid_spaces-10), red_soldier_sprite_name, soldier_stats[:], soldier_type, 0 ]
character_info.append( blue_soldier )
character_info.append( red_soldier )

## Other premade characters
blue_soldier = [ (grid_spaces/2, grid_spaces/2), blue_soldier_sprite_name, soldier_stats[:], soldier_type, 1 ]
character_info.append( blue_soldier )
red_soldier = [ (grid_spaces/2-1, grid_spaces/2), red_soldier_sprite_name, soldier_stats[:], soldier_type, 0 ]
character_info.append( red_soldier )
blue_soldier = [ (grid_spaces/2-2, grid_spaces/2), blue_soldier_sprite_name, soldier_stats[:], soldier_type, 1 ]
character_info.append( blue_soldier )

#######################################################################
##    other stuff
########################################################################
SpawnerTextInfo = ['Soldier', 'Archer', 'Cancel']
characters = {'Blue Soldier':blue_soldier, 'Blue Archer':blue_archer,
              'Red Soldier':red_soldier, 'Red Archer':red_archer }
spawnerId = 0
spawnerInfoDisplayPoint = (grid_spaces-10, 2 )









