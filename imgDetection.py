import cv2
from PIL import ImageFont, ImageDraw, Image

""" Converts user provided string to an images that will be used to find the
sensitive data from a target file.
"""
def privateDataImg(privateString):
        # Selects font for the user provided string (Using Ubuntu's font path)
    font = ImageFont.truetype(
        "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf", 14, encoding="unic")

    # Dimentions of the font
    fontWidth, fontHeight = font.getsize(privateString)

    # Creates the background of the picture for the user string
    privateImgField = Image.new(
        "RGB", (fontWidth + 10, fontHeight + 10), "white")
    # Draws the string onto the created white rectangle
    writePrivateImgField = ImageDraw.Draw(privateImgField)
    writePrivateImgField.text((5, 5), privateString, "black", font)
    # Saves the final file
    privateImgField.save("privateData.png", "PNG")


"""Perfoms template matching function """
def imgTemplateMatch(templetaImageName, imageToScanName):
        # Loads the string image and target images in gray scale
    imageScan = cv2.imread(imageToScanName, 0)
    templateImage = cv2.imread(templetaImageName, 0)

    # Stores the dimentions of the template
    templateWidth, templateHight = templateImage.shape[::-1]

    # Use template matching function with method TM_CCOEFF_NORMED
    result = cv2.matchTemplate(imageScan, templateImage, cv2.TM_CCOEFF_NORMED)

    # Calculate the rectangle dimentions around the detected area
    minumum, maximum, minLocation, maxLocation = cv2.minMaxLoc(result)
    lowCornerFormula = (
        maxLocation[0] + templateWidth, maxLocation[1] + templateHight)

    copyimageScan = imageScan.copy()
    # Draws rectangle
    cv2.rectangle(copyimageScan, maxLocation, lowCornerFormula, 255, -1)
    cv2.imwrite("output.png", copyimageScan)
    # cv2.imshow('image',copyimageScan)
    # cv2.waitKey(0)


""" Utilizes machine learing (cascade file) file to detect objects.  Faces cascade will be
used by default. """
def objectDetection(filename):
    faceCascade = cv2.CascadeClassifier(
        "./resources/haarcascade_frontalface_alt.xml")
    img = cv2.imread(filename)
    tempGrayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Utilizes detectMultiScale to find the objects
    faces = faceCascade.detectMultiScale(tempGrayImg, 1.3, 5)

    # Calculates the rectangle based on two points
    for (xDir, yDir, width, height) in faces:
        cv2.rectangle(img, (xDir, yDir), (xDir + width,
                                          yDir + height), (255, 0, 0), -1)

    cv2.imwrite("finalOutput.png", img)
    # cv2.imshow("Faces", img)
    # cv2.waitKey(0)


def RUN(userInput, filename):
    privateDataImg(userInput)
    imgTemplateMatch("privateData.png", filename)
    objectDetection("output.png")
