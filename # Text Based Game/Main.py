



#################################################################  GLOBAL CLASSES   ###################################################################################
## Stats for the citizen's city
class City():
    var_list = [
        'houses','tax','population','tax_income','barracks','troops','troop_percent','construct_force','construct_percent','goldmines',\
        'stonemines','lumbermills','total_mills','work_force',\
        'gold_income','stone_income','wood_income','goldmine_cost','stonemine_cost','lumbermill_cost'
                ]
    
    ## Constants:
    houses = 10
    population = 35

    ## Citizen categories:
        ## 1/5 of pop is troops to start
    troop_percent = 25
    troops = int( population/ (100/troop_percent) )

        ## 1/10 of pop is construction workers to start
    construct_percent = 12.5
    construct_force = int( population/ (100/construct_percent) )

        ## Everyone else is a worker
    work_force = population - troops - construct_force

    ## Buildings:
    barracks = 1
    goldmines = 2
    stonemines = 3
    lumbermills = 2
    total_mills = goldmines + stonemines + lumbermills

    ## Building costs:
        ## Building cost = [ gold, stone, wood ]
    house_cost = [1,2,3]
    barracks_cost = [1,2,3]
    goldmine_cost = [1,2,3]
    stomemine_cost = [1,2,3]
    lumbermill_cost = [1,2,3]

    ## Various rates:
    tax = 2
    gold_priority = 1
    stone_priority = 2
    wood_priority = 3
    
    ## Income rates:
    tax_income = houses * tax
        ## income = priority * ( total workers / total mills (which = workers for that mine))
    gold_income = int(  gold_priority * goldmines * work_force/total_mills  )
    stone_income = int(  stone_priority * stonemines * work_force/total_mills  )
    wood_income = int(  wood_priority * lumbermills * work_force/total_mills  )    
    
## Character's stats, can be modified
class Man():
    health = 100
    attack = 12
    strength = 2

## The orc enemy stats
class Orc():
    health = 50
    attack = 6
    strength = 3




##########################################################   GLOBAL FUNCTIONS   #######################################################################################
## Returns the desired task to run
def Get_Action():
    print ('You are now at the Command Post. What do you wish to do?')
    Type ('Will you go to the "War", build up your "cities", view the "tutorial", or "quit"?')
    
    task = str( input('') )
    valid_inputs = ['War','war','cities','Cities','tutorial','Tutorial','quit','Quit']
    
    task = Check(task, valid_inputs)
    
    return task

## Runs the desired task5
def Run_Action(task):
    if task == 'quit' or task == 'Quit':
        global Running
        Running = False
    elif task == 'war' or task == 'War':
        print ('Under refinement')
        #War()
    elif task == 'cities' or task == 'Cities':
        Cities()
    elif task == 'tutorial' or task == 'Tutorial':
        Tutorial()

## A very common snippet that makes sure given input is valid so that no loops are broken
    ## More concise than a try/except because it test multiple inputs at once
def Check(test, check_list):
    count = 0
    while test not in check_list and count != 8:
        if test == 'quit' or test == 'Quit':
            break
        count += 1
        print ('Unrecoginzed command. Enter a new command.')
        test = input ('')
    if count == 8:
        print ('Too many invalid commands. Returning you to the command tent.')
        Get_Action()
    if test == 'quit' or test == 'Quit':
        print ('')
        Get_Action()
    return test

## Finds the ending word for Type(text)
def Find_Last_Word(text, text_chars, page_length, current_count):
    original_count = current_count
    current_letter = text_chars[current_count]
    # on the off chance that the first letter is a 'space'
    if current_letter == ' ':
        current_letter = text_chars[current_count-1]
    current_word_list = []
    while current_letter != ' ':
        current_word_list.append(current_letter)
        current_count -= 1
        current_letter = text_chars[current_count]

    first_point = current_count
    current_word_list.remove(current_word_list[0])
    current_word_list.reverse()

    current_count = original_count
    current_letter = text_chars[current_count]
    while current_letter != ' ':
        current_word_list.append(current_letter)
        current_count += 1

        # if the current word is the last word then is used
        try:
            current_letter = text_chars[current_count]
        except:
            break

    current_word = ('')
    for x in current_word_list:
        current_word += str(x)

    last_word = current_word
    final_return = [last_word, first_point]

    return final_return

def Insert_Newline(text_chars, text_words_list, first_point, last_word):
    for current_word in text_words_list:
        if last_word == current_word:
            text_chars.insert( first_point , '\n')
            break
    return text_chars

## Prints words on screen but will measure the screen to make sure no words are broken up
def Type(text):
    page_length = 80 # number of chars that fit on a single line of text
        
    # for multi-line text
    if len(text) > page_length:
        text_words_list = text.split(' ')
        
        # makes a list of the text
        text_chars = []
        for x in text:
            text_chars.append(x)

        # finds valuble info
        first_start = page_length - 1
        final_return = Find_Last_Word(text, text_chars, page_length, first_start)
        last_word = final_return[0]
        first_point = final_return[1]
        
        # Puts the ending word on a new line
        text_chars = Insert_Newline(text_chars, text_words_list, first_point, last_word)
        
        new_start = first_point + page_length - 1 # the one is for the space before each new line
                
        try:
            final_return  = Find_Last_Word(text, text_chars, page_length, new_start)
            last_word = final_return[0]
            first_point = final_return[1]

            text_chars = Insert_Newline(text_chars, text_words_list, last_word, first_point)

            new_start += first_point
            
            try:
                final_return  = Find_Last_Word(text, text_chars, page_length, new_start)
                last_word = final_return[0]
                first_point = final_return[1]

                text_chars = Insert_Newline(text_chars, text_words_list, last_word, first_point)

            except:
                pass
                        
        except:
            pass
        
        # Makes the actual modified text
        text = ''
        for x in text_chars:
            text += str(x)

    print (text)



    
##################################################################   TUTORIAL   #######################################################################################
def Tutorial():
    print ('The first thing you need to understand is info about your city.')
    Type ('Each house you own can hold up to 10 people. To start, 1/5 of your population will be soldiers. Another 1/10 will be construction workers. The rest is divided up to the goldmines, stonemines, and lumbermills.')
    print ('')
    
    Type ('You can increase or decrease these ratios at any time by going to your city and prompting to change them, but beware, population is not based solely on the number of homes you own.')
    Type ('Your tax rates, gerenal wealthiness, supply of each material, troop percentage, the crowdidness of your town and various other things will affect immigration rates.')
    print ('')
    
    Type ('The next thing you need to understand is how to change these things. First, you start by getting to your command tent. Then, when prompted you type in the specific command you would like to change.')
    print ('')

    print ('Next, battle commands. To start, go to your battle front. ')


#########################################################################    BATTLE   #################################################################################
## Runs the battle sims
def War():
    print ('You currently have '+ str(Man.health) +' health remaining, and '+ str(City.troops) +' troops.)')
    print ('Would you like to battle an orc or fight a battle? (y)(n)')

    valid_responses = ['y','Y','n','N']
    fight = str( input(''))

    Check(fight, valid_responses)
    if fight == 'y' or fight == 'Y':
        print ('Which would you like to fight, large scale battle or a 1v1 match?')
    elif fight == 'n' or fight == 'N':
        print ('We will return to the commmand tent then.')




##########################################################################   CITY   ###################################################################################
## Runs the city info and sims
def Cities():
    Type ('Currently you have '+ str(City.houses) +' houses, a population of '+ str(City.population) +' citizens, '+str(City.construct_force) +' construction workers, '+ str( City.troops ) +' troops, and '+ str( City.work_force ) +' people in your work force.')
    print ('')
    
    print ('Would you like a list of all information about your city? (y)(n)')
    getInfo = input('')
    valid_inputs = ['y','Y','n','N']
    Check(getInfo, valid_inputs)
    city_buildings = ['house','barracks','goldmines','stonemines','lumbermills']
    city_rates = ['tax','gold_priority','stone_priority','wood_priority']
    
    if getInfo == 'y' or getInfo == 'Y':
        print ('Your buildings include '+ str( city_buildings ) +', and your rates include '+ str( city_rates ) +'.')
        print (City.var_list)
        
    Type ('You can type the name of any structure and construction will begin to add a new building. You must be able to pay for each construct though.')
    Type ("In addition to this, you can change your city's rates such as your tax, gold, stone, or wood income priority, military drafting rate, percent of construction workers, and others.")

    print ('Would you like to build any new buildings? (y)(n)')
    get_action = input ('')
    valid_inputs = ['y','Y','n','N']
    Check(get_action, valid_inputs)
    
    if get_action == 'y' or get_action == 'Y':
        print('What would you like to build?')
        get_action = input('')
        Check(get_action, city_buildings)

        for building in city_buildings:
            if get_action == building:
                building_cost = ( ''+ building +'_cost' )
                building_cost = locals()['City.'+ building_cost]
                

    ## city_varibles = ['houses','tax','barracks','goldmines','stonemines','lumbermills','troop_percent','construct_percent']
                
##    if get_action == 'houses':
##        gold = City.house_cost[0]
##        stone = City.house_cost[1]
##        wood = City.house_cost[2]
##        print ('A new house can be constructed for '+ gold +' gold, '+ stone +' stone, and '+ wood +' wood.')
##        print ('Are you sure you want to build a house?')
##        build = input('') 
##        if build == 'y' or build == 'Y':
##            City.houses += 1
##            City.gold -= gold
##            City.stone -= stone
##            City.wood -= wood
##            print ('You now have ')
##        
##    elif get_action == 'tax':
##        Type ('Your current tax is '+ str( City.tax ) + ' gold per a house. What would you like to change your tax to? Beware, too high a tax will encourage people to leave.')
##        new_tax = input('')
##        City.tax = new_tax
##    elif get_action == city_varibles[1]:
##        gold = City.barracks_cost[0]
##        stone = City.barracks_cost[1]
##        wood = City.barracks_cost[2]
##        print ('A new barracks can be contructed for ...')
##    elif get_action == 'goldmines':
##        gold = City.goldmine_cost[0]
##        stone = City.goldmine_cost[1]
##        wood = City.goldmine_cost[2]
##        print ('A new goldmine can be constructed for ...')
##    elif get_action == 'stonemines':
##        gold = City.stonemine_cost[0]
##        stone = City.stonemine_cost[1]
##        wood = City.stonemine_cost[2]
##        print ('A new stonemine can be constructed for ...')
##    elif get_action == 'lumbermill':
##        gold = City.lumbermill_cost[0]
##        stone = City.lumbermill_cost[1]
##        wood = City.lumbermill_cost[2]
##        print ('A new lumbermill can be constructed for ...')
##    elif get_action == 'troop_percent':
##        print ('Your current troop percent is '+ str( City.troop_percent ) +'% of your population.')
##    elif get_action == 'construct_percent':
##        print ('Your current construction percent is '+ str( City.construct_person ) +'% of your population.')
##
##    print ('Would you like to change anything else?')
    
        
####################################################################   MAIN   #########################################################################################
## Runs the main exe
def Main():
    name = input("What is your name: ")

    print ('Welcome to The War, '+ name +'.')

    while Running == True:
        task = Get_Action()
        print ('')
        
        Run_Action(task)
        print ('')

Running = True






    
