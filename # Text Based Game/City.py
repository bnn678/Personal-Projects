## Stats for the citizen's city
class City():
    var_list = ['houses','tax','population','tax_income','barracks','troops','troop_percent','construct_force','construct_percent','goldmines',\
                'stonemines','lumbermills','total_mills','work_force',\
                'gold_income','stone_income','wood_income','goldmine_cost','stonemine_cost','lumbermill_cost']
    
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
