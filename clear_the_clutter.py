import os

#os.rename("Clutter/dfdd.txt","Clutter/TextFile.txt")

files = os.listdir("Clutter/")
i = 1
for file in files:
    if file.endswith(".jpg"):
        os.rename(f"Clutter/{file}",f"Clutter/{i}.jpg")
        i = i + 1
        print(file)