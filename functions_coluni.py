from PIL import Image
import os
import shutil


"""
Rename files and Image Crop function.

"""

#rename files
def renamePages(path = os.getcwd()):
    i=1
    for files in os.listdir(path):
        shutil.move(path+files,path+str(i)+".png")
        i+=1
#crop img
def cropfiles(path = os.getcwd()):
    for file in os.listdir(path):
        filePath=path+file
        with Image.open(filePath) as img:
            left =0
            top=240
            right=0.72*img.size[1]
            botton=1.33*img.size[0]
            img =img.crop((left,top,right,botton))
            img.save(filePath,"PNG")
            
renamePages("img/dia1/")
renamePages("img/dia2/")
cropfiles("img/dia1/")
cropfiles("img/dia2/")
