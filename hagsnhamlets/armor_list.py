from item import item

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

 