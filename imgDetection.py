import cv2
import time
import numpy as np
from PIL import ImageFont, ImageDraw, Image


def privateDataImg( privateString ):
	font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf", 14, encoding="unic")
	fontWidth, fontHeight = font.getsize(privateString)

	privateImgField = Image.new("RGB", (fontWidth + 10, fontHeight + 10) , "white")

	writePrivateImgField = ImageDraw.Draw(privateImgField)
	writePrivateImgField.text((5,5) , privateString, "black", font )

	privateImgField.save("privateData.png", "PNG")


def imgTemplateMatch( templetaImageName, imageToScanName ):
	# Images will be loading in gray scale
	imageScan = cv2.imread(imageToScanName, 0)

	templateImage = cv2.imread(templetaImageName,0)
	templateWidth, templateHight = templateImage.shape[::-1]

	# Use template matching function with method TM_CCOEFF_NORMED
	result = cv2.matchTemplate(imageScan, templateImage, cv2.TM_CCOEFF_NORMED)
	minumum, maximum, minLocation, maxLocation = cv2.minMaxLoc(result)

	lowCornerFormula = (maxLocation[0] + templateWidth, maxLocation[1] + templateHight )

	copyimageScan = imageScan.copy()

	cv2.rectangle( copyimageScan , maxLocation, lowCornerFormula, 255, -1 )
	#copyimageScan.show()
	cv2.imshow('image',copyimageScan)
	cv2.waitKey(0)


def RUN():
	userInput = input("Enter private data to protect: ")
	privateDataImg(userInput)

	imgTemplateMatch("privateData.png", "resume1.png")


RUN()
