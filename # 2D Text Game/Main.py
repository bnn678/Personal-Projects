#################################################################################################################
#################################################################################################################
##    Made by: Brandon Shaver
#################################################################################################################
#################################################################################################################

import random
import sys



#################################################################################################################
##    Global Varible Declarations
#################################################################################################################
map_x = 15
map_y = 20

map_stage = 'move'



#################################################################################################################
##    Classes
#################################################################################################################
class Hero():
    def __init__( self ):
        self.type = 'hero'
        self.max_health = 25
        self.health = self.max_health
        self.attack = 6
        self.accuracy = 75 # he hits 75% of the time

        self.has_sword = False
        self.health_potions = 0
        self.gold = 10
        self.is_running = False

        self.wolves_killed = 0
        self.orcs_killed = 0
        self.dragons_killed = 0
        self.kill_count = self.wolves_killed + self.orcs_killed + self.dragons_killed
        
        self.sprite = 'H'
        self.pos = [0,0]

class Wolf():
    degrees = ['starved ','scarred ','winter ','forest ','dire ']
    def __init__( self ):
        self.type = 'enemy'
        self.race = 'wolf'
        self.degree = random.choice(Wolf.degrees)
        self.degree_level = Wolf.degrees.index(self.degree) + 1
        self.name = self.degree + self.race

        self.health = random.randint(3,6) * self.degree_level
        self.attack = random.randint(1,3) * self.degree_level
        self.accuracy = random.randint(25,60) * self.degree_level

        self.reward = random.randint(5,15)

        self.sprite = 'W'
        self.pos = [random.randint(0,map_x),random.randint(0,map_y)]

class Orc():
    degrees = ['starved ','scarred ','bloodthirsty ','warlord ']
    def __init__( self ):
        self.type = 'enemy'
        self.race = 'orc'
        self.degree = random.choice(Orc.degrees)
        self.degree_level = Orc.degrees.index(self.degree) + 1
        self.name = self.degree + self.race
        
        self.health = random.randint(3,18) * self.degree_level
        self.attack = random.randint(1,16) * self.degree_level
        self.accuracy = random.randint(25,60) * self.degree_level

        self.reward = random.randint(5,45)

        self.sprite = 'O'
        self.pos = [random.randint(0,map_x),random.randint(0,map_y)]

class Dragon():
    degrees = ['starved ','scarred ','bloodthirsty ','reverend ','elder ','ancient ','final ']
    def __init__( self ):
        self.type = 'enemy'
        self.race = 'dragon'
        self.degree = random.choice(Dragon.degrees)
        self.degree_level = Dragon.degrees.index(self.degree) + 1
        self.name = self.degree + self.race
        
        self.health = random.randint(75,100) * self.degree_level
        self.attack = random.randint(10,15) * self.degree_level
        self.accuracy = random.randint(50,75) * self.degree_level

        self.reward = random.randint( 500,1000 )

        self.sprite = 'D'
        self.pos = [random.randint(0,map_x),random.randint(0,map_y)]

class Store():
    possible_inventory = ['health_potion','excalibur','golden_apple']
    
    def __init__( self ):
        possible_inventory = Store.possible_inventory
        
        self.cost_for_sleep = random.randint(5,10)
        self.cost_for_excalibur = 100
        self.cost_for_health_potion = 15
        self.cost_for_golden_apple = 60
        self.cost_for_everything = self.cost_for_excalibur + self.cost_for_health_potion + self.cost_for_golden_apple

        self.inventory = []
        self.inventory_items = random.randint(1,len(possible_inventory))
        for num in range( self.inventory_items ):
            new_inventory_item = random.choice(possible_inventory)
            if new_inventory_item not in self.inventory:
                self.inventory.append( new_inventory_item )

        self.type = 'store'
        
        self.pos = [random.randint(0,map_x),random.randint(0,map_y)]
        self.sprite = 'S'



#################################################################################################################
##    Functions
#################################################################################################################
def Display_Map():
    new_map = [ ['_' for n in range( map_x+1 )] for a in range( map_y+1 ) ]
    for item in map_objects:
        new_map[item.pos[1]][item.pos[0]] = item.sprite
            
    for item in new_map:
        line = str( item )
        line = line.replace("'","")
        line = line.replace(",","")
        line = line.strip('[')
        line = line.strip(']')
        print( line )

    print('')

def Get_Map_Action():
    global valid_input
    
    action = input('Enter your command: ')
    if action == 'help':
        return 'help'
    elif action == 'move':
        direction = input('What direction(U,D,L,R): ')
        if direction == 'U':
            if hero.pos[1] - 1 < 0:
                hero.pos[1] = map_y
                return 'out_of_range'
            else:
                hero.pos[1] -= 1
        elif direction == 'D':
            if hero.pos[1] + 1 > map_y:
                hero.pos[1] = 0
                return 'out_of_range'
            else:
                hero.pos[1] += 1
        elif direction == 'L':
            if hero.pos[0] - 1 < 0:
                hero.pos[0] = map_x
                return 'out_of_range'
            else:
                hero.pos[0] -= 1
        elif direction == 'R':
            if hero.pos[0] + 1 > map_x:
                hero.pos[0] = 0
                return 'out_of_range'
            else:
                hero.pos[0] += 1
        else:
            valid_input = False
    elif action == 'w':
        if hero.pos[1] - 1 < 0:
            return 'at_edge'
        else:
            hero.pos[1] -= 1
            hero.is_running = False
    elif action == 'a':
        if hero.pos[0] - 1 < 0:
            return 'at_edge'
        else:
            hero.pos[0] -= 1
            hero.is_running = False
    elif action == 's':
        if hero.pos[1] + 1 > map_y:
            return 'at_edge'
        else:
            hero.pos[1] += 1
            hero.is_running = False
    elif action == 'd':
        if hero.pos[0] + 1 > map_x:
            return 'at_edge'
        else:
            hero.pos[0] += 1
            hero.is_running = False

    elif action == 'show health':
        return 'health'
    elif action == 'show attack':
        return 'attack'
    elif action == 'show gold':
        return 'gold'
    elif action == 'show stats' or action == 'show my stats':
        return 'stats'
    elif action == 'show wolf kills':
        return 'wolf'
    elif action == 'show orc kills':
        return 'orc'
    elif action == 'show dragon kills':
        return 'dragon'
    elif action == 'show kills':
        return 'kills'

    ## Debugging Codes:
    elif action == '``':
        hero.gold = 1000
        hero.max_health = 1000
        hero.health = 1000
        hero.attack = 1000

        hero.accuracy = 100
        hero.health_potions = 10
        hero.has_sword = True

    elif action == 'make_da_superstore':
        da_shop = Store()
        da_shop.__init__()
        da_shop.inventory = da_shop.possible_inventory
        da_shop.pos = hero.pos[:]
        map_objects.append( da_shop )

    elif action == 'quit' or action == 'exit':
        sys.exit()
    else:
        return 'invalid'

def Check_Hero_Collision():
    global map_stage
    global collision
    
    hero_pos = hero.pos
    map_objects.reverse()
    
    if hero.is_running == False and map_stage == 'move':
        for item in map_objects:
            if hero != item:
                if hero.pos == item.pos:
                    if item.type == 'store':
                        print("You have found an inn.")
                        map_stage = 'shop'
                        
                    elif item.type == 'enemy':
                        Clear_Screen()
                        if item.health <= 0:
                            print('You have found a dead '+item.name+'.')
                        else:
                            print('You have encountered a '+item.name+'!')
                            map_stage = 'attack'
                            
                    else:
                        print("Something is not working correctly.")
                        
                    collision = item
    map_objects.reverse()
    return None

def Clear_Screen():
    [print('') for x in range(30)]

def Get_Encounter_Action():
    encounter_move = input('What would you like to do(examine,attack,use potion,run): ')
    if encounter_move == 'examine':
        if collision.health > 0:
            print('The '+ collision.race +' has '+ str(collision.health) +' health and '+ str(collision.attack) +' attack power.')
        else:
            print('You stand atop a dead '+ collision.race +'.')
    elif encounter_move == 'attack':
        if collision.health > 0:
            Attack()
        else:
            print('The '+ collision.race +' is already dead.')
    elif encounter_move == 'use potion':
        potion_type = input('What kind of potion(health potion): ')
        if potion_type == 'health potion' and hero.health_potions > 0:
            print("Your hero's health has been restored. You now have "+str(hero.health)+" health.")
            hero.health = hero.max_health
            hero.health_potions -= 1
        elif potion_type == 'health potion' and hero.health_potions == 0:
            print("You do not have any of these potions.")
    elif encounter_move == 'run':
        global map_stage
        map_stage = 'move'
        hero.is_running = True

        Clear_Screen()
        Display_Map()

def Attack():
    print("You attempt to attack the "+ collision.race +".")
    hit_success = random.randint(0,100)
    if hero.accuracy >= hit_success:
        collision.health -= hero.attack
        if collision.health > 0:
            print("Your attack succeeded. The "+ collision.race +" now has "+ str(collision.health) +" health.")
        elif collision.health <= 0:
            hero.gold += collision.reward
            print("Your attack succeeded.")
            print("You have killed the "+ collision.race +". You gained "+ str(collision.reward) +" gold "+
                  "and now have a total of "+ str(hero.gold) +" gold.")
            collision.sprite = 'x'

            if collision.race == 'orc':
                hero.orcs_killed += 1
                orc = Orc()
                orc.__init__()
                map_objects.append(orc)
            elif collision.race == 'wolf':
                hero.wolves_killed += 1
                wolf = Wolf()
                wolf.__init__()
                map_objects.append(wolf)
            elif collision.race == 'dragon':
                hero.dragons_killed += 1
                dragon = Dragon()
                dragon.__init__()
                map_objects.append(dragon)

            hero.max_health += 1
            hero.attack += 1
            
    elif hero.accuracy < hit_success:
        print("Your attack missed.")

    if collision.health > 0:
        hit_success = random.randint(0,100)
        if collision.accuracy >= hit_success:
            hero.health -= collision.attack
            if hero.health > 0:
                print('The '+ collision.race +' has counter attacked and dealt '+ str(collision.attack) +' damage. '+
                      'You now have '+ str(hero.health) +' health left.')
            elif hero.health <= 0:
                print('The '+ collision.race +' has counter attacked.')
                print('Your hero has been killed.')
                sys.exit()
        elif collision.accuracy < hit_success:
            pass

def Shop():
    action = input("What would you like to do here(buy,sell,sleep/rest,leave):")
    if action == 'help':
        print('Here you can buy, sell, sleep, or leave.')
        
    elif action == 'buy':
        print('This store has '+ str(collision.inventory) +' for sale.')
        print("What would you like to buy?")
        item = input()
        if item in collision.inventory:
            if item == 'excalibur':
                print('This item costs '+ str(collision.cost_for_excalibur) +' gold, and will boost your attack damage by 100')
                if hero.has_sword == True:
                    print('You already own this sword.')
                elif hero.gold >= collision.cost_for_excalibur:
                    answer = input('Would you like to buy this(yes,no): ')
                    if answer == 'yes':
                        hero.attack += 100
                        hero.gold -= collision.cost_for_excalibur
                        
            elif item == 'health_potion':
                print("This item costs "+ str(collision.cost_for_health_potion) +" gold, and will restore your hero's health.")
                answer = input('Would you like to buy this(yes, no): ')
                if answer == 'yes':
                    hero.health_potions += 1
                    hero.gold -= collision.cost_for_health_potion
                
            elif item == 'golden_apple':
                print("This item costs "+ str(collision.cost_for_golden_apple) +" gold, and will raise your hero's max health by 40.")
                answer = input('Would you like to buy this(yes, no): ')
                if answer == 'yes':
                    hero.max_health += 40
                    hero.health = hero.max_health
                    hero.gold -= collision.cost_for_golden_apple
                    
        elif item == 'nothing':
            print("It would be a shame to come all the way here and not buy something.")

        elif item == 'everything':
            if hero.gold >= collision.cost_for_everything:
                hero.has_sword = True
                hero.attack += 100
                hero.health_potions += 1
                hero.health += 40
            pass
            
        else:
            print('This store does not sell that.')
        
    elif action == 'sell':
        print("What would you like to sell?")
        item = input()
        
    elif action == 'sleep' or action == 'rest':
        if hero.gold >= collision.cost_for_sleep:
            print('It will cost '+ str(collision.cost_for_sleep) +' gold to sleep here. '+
                  'You currently have '+ str(hero.gold) +'. Are you sure you want to sleep here?')
            answer = input()
            if answer == 'yes':
                hero.gold -= collision.cost_for_sleep
                hero.health = hero.max_health
                print("Your hero's health has been restored!")
        else:
            print("Sorry but you don't have enough gold.")
            
    elif action == 'leave':
        global map_stage
        map_stage = 'move'

def Move_Map_Characters():
    for character in map_objects:
        if character.type == 'enemy':
            if character.health > 0:
                x_change = random.randint(-1,1)
                y_change = random.randint(-1,1)
                x_or_y = random.randint(0,1)

                if x_or_y == 0:
                    character.pos[0] += x_change
                else:
                    character.pos[1] += y_change

                if character.pos[0] < 0 or character.pos[0] > map_x:
                    character.pos[0] -= x_change
                if character.pos[1] < 0 or character.pos[1] > map_y:
                    character.pos[1] -= y_change

def Check_Map_Objects_Collision():
    global current_positions
    global character
    current_positions = {}
    for character in map_objects:
        the_pos = tuple(character.pos)
        if character.type != 'hero':
            if the_pos not in current_positions:
                    current_positions[the_pos] = character
            else:
                other_char = current_positions[the_pos]
                if character.type == 'store':
                    print("A store has been destroyed!")
                    map_objects.remove(character)
                elif other_char.type == 'store':
                    print("A store has been destroyed!")
                    map_objects.remove(other_char)
                elif character.type == 'enemy' and other_char.type == 'enemy':
                    if character.health > 0 and other_char.health > 0:
                        print("There has been a skirmish between a "+character.race+" and a "+other_char.race+"!")
                        if character.health > other_char.health:
                            print("The "+character.race+" won the skirmish.")
                            other_char.health = 0
                            other_char.sprite = 'x'
                        else:
                            print("The "+other_char.race+" won the skirmish.")
                            character.health = 0
                            character.sprite = 'x'



#################################################################################################################
##    Initial Character Creation
#################################################################################################################
hero = Hero()
hero.__init__()

def CreateMapCharacters():
    global map_objects
    map_objects = [hero]

    for x in range( random.randint(2,5) ):
        wolf = Wolf()
        wolf.__init__()
        map_objects.append(wolf)

    for x in range( random.randint(2,4) ):
        orc = Orc()
        orc.__init__()
        map_objects.append(orc)

    store = Store()
    store.__init__()
    map_objects.append(store)

    dragon = Dragon()
    dragon.__init__()
    map_objects.append(dragon)

CreateMapCharacters()

#################################################################################################################
##    Main
#################################################################################################################
def Main():
    global map_stage
    global valid_input

    print('')
    print('-----------------------------------------------------------------------')
    print('You are the hero(H) and there are many things to be found on the map.')
    print('You will start of in the top left corner. Your goal is to kill a dragon(D).')
    print('To move, use W,A,S,D or type "move".')
    print('Try typing "help" for a complete list of commands.')
    print('Press "enter" to enter a command.')
    print('-----------------------------------------------------------------------')
    print('')
    print('Press "enter" to begin.')
    print('')

    begin = input()
    Clear_Screen()
    Display_Map()

    build_store_chance = 5
    
    while True:
        build_store = random.randint(1,100)
        
        if map_stage == 'move':
            action = Get_Map_Action()
            if build_store <= build_store_chance:
                store = Store()
                store.__init__()
                map_objects.append(store)
                
            if action == 'out_of_range':
                CreateMapCharacters()
            Clear_Screen()
            Display_Map()
            Check_Hero_Collision()
                        
            if action == 'invalid':
                print('That was not a valid input.')     
            elif action == 'health':
                print('Your hero currently has '+ str(hero.health) +' health.')
            elif action == 'attack':
                print("Your hero currently has "+ str(hero.attack) +" attack damage.")
            elif action == 'gold':
                print("Your hero currently has "+ str(hero.gold) +" gold.")
            elif action == 'stats':
                print('Your hero has '+str(hero.health)+' health, '+str(hero.attack)+' attack, '+str(hero.potions)+'.')
            elif action == 'wolf':
                print('Your hero has slain '+str(hero.wolves_killed)+' wolves.')
            elif action == 'orc':
                print('Your hero has slain '+str(hero.orcs_killed)+' orcs.')
            elif action == 'dragon':
                print('Your hero has slain '+str(hero.dragons_killed)+' dragons.')
            elif action == 'kills':
                print('Your hero has slain '+str(hero.wolves_killed)+' wolves, '+str(hero.orcs_killed)+' orcs, '
                      +str(hero.dragons_killed)+' dragons, and '+str(hero.kill_count)+' beasts in total.')
            elif action == 'help':
                print('Possible actions are: ')
                print('   move, w, a, s, d, show health, show attack, show gold,')
                print('   show wolf kills, show orc kills, show dragon kills, show kills')
                print('')
                print('To enter these commands, type them and then press "enter".')
                print('')
            elif action == 'at_edge':
                print("You are at the edge of this map. In order to move into the next area, "+
                      "you must use the 'move' command.")

            Move_Map_Characters()
            Check_Map_Objects_Collision()
            Check_Hero_Collision()
            
        elif map_stage == 'attack':
            Get_Encounter_Action()
        elif map_stage == 'shop':
            Shop()
        print('')
Main()

