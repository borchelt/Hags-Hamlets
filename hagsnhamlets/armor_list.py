from item import armor, item

import random
#ARMOR 



chainmail = item("Chainmail", "Chainmail")
lamellar = item("Lamellar", "Lamellar")
leather = item("Leather", "Leather")
plate = item("Plate", "Plate")
ringmail = item("Ringmail", "Ringmail")
scale = item("Scale", "Scale")
obsidian = item("Obsidian", "Obsidian")
glass = item("Glass", "Glass")
robes = item("Robes", "Robes")
helmet = item("Helmet", "Helmet")
coif = item("Coif", "Coif")
hood = item("Hood", "Hood")
mantle = item("Mantle", "Mantle")
breastplate = item("Breastplate", "Breastplate")
greaves = item("Greaves", "Greaves")
bracers = item("Bracers", "Bracers")
boots = item("Boots", "Boots")
cuirass = item("Cuirass", "Cuirass")

armor_listProto = ['chainmail', 'lamellar', 'leather', 'plate', 'ringmail', 'scale', 'obsidian', 'glass']
armor_listProto2 = ['robes', 'helmet', 'coif', 'hood', 'mantle', 'breastplate', 'greaves', 'bracers', 'boots', 'cuirass']
armor_list = []

for i in range(len(armor_listProto)):
    for y in range(len(armor_listProto2)):
        armor_list.append(item(f"{armor_listProto[i]} {armor_listProto2[y]}",f"{armor_listProto[i]} {armor_listProto2[y]}" ))

for i in range(len(armor_list)):
    print(f"{i}. {armor_list[i].name}")


new_armor_list = []

def armorsmith(item):
    print("running armorsmith")
    rand_stat = random.randint(0, 5)
    new_armor = armor(item.name, rand_stat, rand_stat,f"a {item.name}")
    return new_armor

for i in range(len(armor_list)):
    new_armor_list.append(armorsmith(armor_list[i]))

armor_list = new_armor_list

# for i in range(len(armor_list)):
#     print(f"{i}. {armor_list[i].name}")

 