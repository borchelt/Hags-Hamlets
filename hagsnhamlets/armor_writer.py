from item import item

armor_list = [

"chainmail",
"lamellar",
"leather",
"plate",
"ringmail",
"scale",
"obsidian",
"glass",
"robes",
"helmet",
"coif",
"hood",
"mantle",
"breastplate",
"greaves",
"bracers",
"boots",
"cuirass",

]


def variable_list(list):
        
    print("Variable List")

    variable_list = []
    for i in range(len(list)):
        variable_list.append(list[i])

    print(variable_list)


def item_writer(list):

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
        list[i] = f"{formatted_titles[i]} = item(\"{capitalized[i]}\", \"{capitalized[i]}\")"

    for i in range(len(list)):
        print(list[i])


variable_list(armor_list)
print("")
print("")

item_writer(armor_list)