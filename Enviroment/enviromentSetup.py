import cv2
import os
import shutil

"""Setup directories needed"""
def setupFolders():
    listOfFolders = ["data", "positives", "negatives", "images"]
    print("The folders data, positives, and negatives will be created in this directory")
    for folder in listOfFolders:
        if not os.path.exists(folder):
            os.makedirs(folder)
        else:
            print("Warning: One or more folders already exist in this directory.")
            userIn = input("The folder " + '"' + folder + '"' +
                           " will be overwritten.  Do you want to continue. (y/n)")
            if (userIn).lower() in ["y", "yes"]:
				# Used to remove folders even when they contain files
                shutil.rmtree(folder)
                os.makedirs(folder)
            else:
                exit()


"""Generates 1900 negative images from a source solder"""
def getAndResizeImages(path="images", imgNumber=1900):
    count = 0
    for imgFile in os.listdir(path):
        # reading images in gray scale
        img = cv2.imread(os.path.join(path, imgFile), 0)
        imgResize = cv2.resize(img, (100, 100)) # resize images to 100x100
        if not os.path.exists("negatives"):
            os.mkdir("negatives")
        cv2.imwrite("negatives/" + str(count) + ".jpg", imgResize)
        count += 1
        if count > imgNumber:
            break


"""Generates a negative images map, which is required by CV2 to generate samples"""
def createNegatives():
    for folder in os.listdir():
        if (folder == "negatives"):
            for img in os.listdir(folder):
                toWrite = folder + "/" + img + "\n"
                with open("negativesMap.txt", 'a') as handle:
                    handle.write(toWrite)

""" Moves the final casacde file from the data folder to the working directory """
def moveFolder():
    shutil.copy2("./data/cascade.xml", "./generatedCascade.xml")
