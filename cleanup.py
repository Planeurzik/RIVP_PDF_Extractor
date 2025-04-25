import os
with open("errors.txt",encoding="utf-8") as f:
    files_to_keep = f.readlines()
    files_to_keep = ["pdf/"+file.strip().split(".txt")[0]+".pdf" for file in files_to_keep if len(file) > 1]
    path = "pdf/"
    for file_name in os.listdir(path):
        # construct full file path
        file = path + file_name
        if os.path.isfile(file) and file not in files_to_keep:
            print('Deleting file:', file)
            os.remove(file)