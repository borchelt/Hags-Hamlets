from weapon import weapon 

weapon_list = [

"Battle axe",
"bludgeon",
"club",
"flail",
"flanged mace",
"pick",
"mace",
"morning star",
"quarterstaff",
"war hammer",
"arming sword",
"dagger",
"estoc",
"falchion",
"katana",
"knife",
"longsword",
"rapier",
"sabre",
"shortsword",
"glaive",
"lance",
"halberd",
"axe",
"pike",
"war scythe",
"bow",
"longbow",
"recurve bow",
"crossbow",
"arbalest",
"repeating crossbow",
"sling",
"throwing knife",
"throwing spear",
"javelin",
"club",
"dagger",
"greatclub",
"handaxe",
"javelin",
"mace",
"sickle",
"dart",
"scimitar",
"rapier",
"trident",
"whip",
"maul",
"lance",

]


def variable_list(list):
        
    print("Variable List")

    variable_list = []
    for i in range(len(list)):
        variable_list.append(list[i])

    print(variable_list)


def weapon_writer(list):

    formatted_titles = []

    origin_list = list
    for i in range(len(list)):

        formatted = origin_list[i].replace(" ", "_")
        formatted_titles.append(formatted)
        formatted_titles[i] = formatted_titles[i].replace("-", "_")

    capitalized = []

    origin_list = list
    for i in range(len(list)):
        formatted = origin_list[i].capitalize()
        capitalized.append(formatted)


    for i in range(len(list)):
        list[i] = f"{formatted_titles[i]} = weapon(\"{capitalized[i]}\", 1, 1, \"Weapon\", \"A {capitalized[i]}\")"


    for i in range(len(list)):
        print(list[i])


variable_list(weapon_list)
print("")
print("")

weapon_writer(weapon_list)
