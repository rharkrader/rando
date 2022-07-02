import os
import zipfile
import shutil

dir_to_check = "D:/OneDrive/RPGs"
out_file_path = "./dupe_list.txt"

file_list = list()
for root, dirs, files in os.walk(dir_to_check):
    for direc in dirs:
        if direc == "__MACOSX":
            print("Current dir: ", os.path.join(root, direc))
            shutil.rmtree(os.path.join(root, direc), ignore_errors=True)
    for file in files:
        file_path = os.path.join(root, file)
        file_size = os.path.getsize(file_path)
        if file.endswith(".zip"):
            print("Zipfile Path:", root)
            print("Zipfile: ", file)
            with zipfile.ZipFile(file_path, "r") as zip_ref:
                zip_ref.extractall(root)
        if file != "desktop.ini" and file != ".DS_Store":
            file_list.append([file_path.encode("UTF-8"), file_size])
        else:
            print("removing :", file_path)
            os.remove(file_path)

sorted_list = sorted(file_list, key=lambda i: i[1])
print("Final list:", len(sorted_list), " :", sorted_list)

dupe_list = list()
previous = sorted_list[0]
for sorted_file in sorted_list[1:]:
    if sorted_file[1] == previous[1]:
        dupe_list.append(previous)
        dupe_list.append(sorted_file)
    previous = sorted_file
print("Dupe list:", len(dupe_list), " :", dupe_list)

out_file = open(out_file_path, "w")
index = 1
for dupe in dupe_list:
    out_file.write(str(dupe[0]))
    out_file.write("|")
    out_file.write(str(dupe[1]))
    out_file.write("\n")
    if index % 2 == 0:
        out_file.write("\n")
    index += 1
out_file.close()
