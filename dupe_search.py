import os

dir_to_check = "F:/Documents/rpgs"
out_file_path = "./dupe_list.txt"

file_list = list()
for root, dirs, files in os.walk(dir_to_check):
    for file in files:
        file_path = os.path.join(root, file).encode("utf-8")
        file_size = os.path.getsize(file_path)
        if file != "desktop.ini":
            file_list.append([file_path, file_size])

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
for dupe in dupe_list:
    out_file.write(str(dupe[0]))
    out_file.write("|")
    out_file.write(str(dupe[1]))
    out_file.write("\n")
out_file.close()
