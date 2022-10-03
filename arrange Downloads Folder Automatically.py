#! python3
# Incerc sa copiez fisierele cu o anumita extensie in alt folder

import os
import shutil

a = input("""Introduce the name of the Downloads folder, taken with copy - paste from the upper bar
-for ex. C:\Programfiles\Dragos-:\n""")
b = input('Introduce the new address for the copied files:\n')
b1 = b + '\\PDF'
b2 = b + '\\JPG'
b3 = b + '\\STL'
b4 = b + '\\ZCODE'
b5 = b + '\\DWG'
b6 = b + '\\ZIP'
b7 = b + '\\3dModel'
try:
    os.makedirs(b1)
    os.makedirs(b2)
    os.makedirs(b3)
    os.makedirs(b4)
    os.makedirs(b5)
    os.makedirs(b6)
    os.makedirs(b7)
except:
    pass

for folder, subfolders, files in os.walk(a):
    print('Folder is ' + folder)
    for subfolder in subfolders:
        pass
        # print('subfolderul lui ' + folder +' este: ' + subfolder)
    for fisier in files:
        # print('Fisierul dinauntru folderului: ' + folder +' este: '+ fisier)
        d = os.path.join(folder, fisier)  # megaimportant
        # print(d)
        try:
            if '.pdf'.lower() in fisier.lower():
                shutil.move(d, b1)
            if '.jpg'.lower() in fisier.lower():
                shutil.move(d, b2)
            if '.stl'.lower() in fisier.lower():
                shutil.move(d, b3)
            if '.zcode'.lower() in fisier.lower():
                shutil.move(d, b4)
            if '.dwg'.lower() in fisier.lower():
                shutil.move(d, b5)
            if '.zip'.lower() in fisier.lower():
                shutil.move(d, b6)
            if '.3dm'.lower() in fisier.lower():
                shutil.move(d, b7)
        except:
            continue
