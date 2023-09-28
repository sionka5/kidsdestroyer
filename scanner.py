import os
import shutil


path = "C:/"
# we shall store all the file names in this list
dirnames = []
dirlist = []



def scanforgames():
    how_many_files = 0
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            how_many_files = how_many_files + 1
            print(dir)
            if (dir == "Epic Games" or dir == "Steam" or dir == "Riot Games"):
                dirlist.append(os.path.join(root, dir))
                dirnames.append(os.path.join(dir))

    print(f"Games dirs: {dirnames}, files scanned: {how_many_files}")
    

def remove():
    print("Deleting...")
    for item in dirlist:
            for position, item in enumerate(dirlist):
                shutil.rmtree(dirlist[position])

   

