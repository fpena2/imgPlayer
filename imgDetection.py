import cv2
from PIL import ImageFont, ImageDraw, Image


def privateDataImg(privateString):
    font = ImageFont.truetype(
        "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf", 14, encoding="unic")

    fontWidth, fontHeight = font.getsize(privateString)

    privateImgField = Image.new(
        "RGB", (fontWidth + 10, fontHeight + 10), "white")

    writePrivateImgField = ImageDraw.Draw(privateImgField)
    writePrivateImgField.text((5, 5), privateString, "black", font)

    privateImgField.save("privateData.png", "PNG")


def imgTemplateMatch(templetaImageName, imageToScanName):
    # Images will be loading in gray scale
    imageScan = cv2.imread(imageToScanName, 0)

    templateImage = cv2.imread(templetaImageName, 0)
    templateWidth, templateHight = templateImage.shape[::-1]

    # Use template matching function with method TM_CCOEFF_NORMED
    result = cv2.matchTemplate(imageScan, templateImage, cv2.TM_CCOEFF_NORMED)
    minumum, maximum, minLocation, maxLocation = cv2.minMaxLoc(result)

    lowCornerFormula = (
        maxLocation[0] + templateWidth, maxLocation[1] + templateHight)

    copyimageScan = imageScan.copy()
    cv2.rectangle(copyimageScan, maxLocation, lowCornerFormula, 255, -1)
    cv2.imwrite("output.png", copyimageScan)
    # cv2.imshow('image',copyimageScan)
    # cv2.waitKey(0)


def objectDetection(filename):
	faceCascade = cv2.CascadeClassifier("./resources/haarcascade_frontalface_alt.xml")
	img = cv2.imread(filename)
	tempGrayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(tempGrayImg, 1.3, 5)
	for (xDir, yDir, width, height) in faces:
		cv2.rectangle(img, (xDir, yDir), (xDir + width, yDir + height), (255, 0, 0), -1)

	cv2.imwrite("finalOutput.png", img)
	# cv2.imshow("Faces", img)
	# cv2.waitKey(0)

def RUN(userInput, filename):
    privateDataImg(userInput)
    imgTemplateMatch("privateData.png", filename)
    objectDetection("output.png")
