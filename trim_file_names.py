import os

dir_to_check = "D:\\OneDrive\\RPGs"
out_file_path = "./rename_candidates.txt"
patterns_to_filter = ["TLG",
                      "Dungeon_Crawl_Classics_",
                      "dungeoncrawlclassics_issue",
                      "d20 - FGG - ",
                      "Delta_Green_",
                      "13thAge-",
                      "FTD_",
                      "Old_School_Essentials_",
                      "Old-School Essentials - ",
                      "OldSchoolEssentials-",
                      "Old-School_Essentials_-_",
                      "Through_Sunken_Lands_-_",
                      "DEGENESIS-",
                      "DCO_",
                      "DuskCityOutlaws-",
                      "EvilHat-",
                      "Coriolis-",
                      "844642-",
                      "BR OST _",
                      "Forbidden_Lands_",
                      "MYZ - ",
                      "MYZ_",
                      "T2K4_",
                      "Twilight 2000 OST ",
                      "Twilight 2000 - ",
                      "TOR_",
                      "DraculaDossier-",
                      "Esoterrorists-",
                      "KWAS-",
                      "TrailOfCthulhu-",
                      "Hero_Kids_-_",
                      "Liminal - ",
                      "Liminal-",
                      "lotr_",
                      "DLWW_",
                      "Hell_on_Earth_",
                      "The_Savage_World_of_Flash_Gordon_",
                      "SevenWorlds-",
                      "KEM_",
                      "Savage_Worlds_Adventure_Edition_",
                      "Esteren_",
                      "ShadowsOfEsteren-",
                      "Stars Without Number - ",
                      "StarsWithoutNumber-",
                      "ShadowOfDemonLord-",
                      "ShadowOfTheDemonLord-",
                      "Star Wars RPG (D6) - ",
                      "Star Wars WEG RPG (D6) - ",
                      "SWD6 - ",
                      "SWD20 - ",
                      "CastleOldskull-",
                      "Catalyst-",
                      "MongooseTraveller-2E-",
                      "UnknownArmies-"]

candidates = list()
for root, dirs, files in os.walk(dir_to_check):
    for file in files:
        file_path = os.path.join(root, file)
        for prefix in patterns_to_filter:
            if file.startswith(prefix):
                candidates.append([file_path.encode("UTF-8"), file_path.replace(prefix, "").encode("UTF-8")])
                os.rename(file_path, file_path.replace(prefix, ""))

print("Final list:", len(candidates), " :", candidates)

out_file = open(out_file_path, "w")
for candidate in candidates:
    out_file.write(str(candidate[0]))
    out_file.write("\n")
    out_file.write("New name:")
    out_file.write("\n")
    out_file.write(str(candidate[1]))
    out_file.write("\n\n")
out_file.close()
