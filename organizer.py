import os
import shutil

folder = "files"

for file in os.listdir(folder):
    if file.endswith(".jpg") or file.endswith(".png"):
        shutil.move(folder + "/" + file, folder + "/Images/" + file)
    elif file.endswith(".pdf"):
        shutil.move(folder + "/" + file, folder + "/Documents/" + file)
