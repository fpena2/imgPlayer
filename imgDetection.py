import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy

def privateDataImg( privateString ):
  # Font path compartible with linux systems 
	font = ImageFont.truetype("/usr/share/fonts/truetype/ubuntu-font-family/UbuntuMono-R.ttf", 14, encoding="unic")
	fontWidth, fontHeight = font.getsize(privateString)

	privateImgField = Image.new("RGB", (fontWidth + 10, fontHeight + 10) , "white")

	writePrivateImgField = ImageDraw.Draw(privateImgField)
	writePrivateImgField.text((5,5) , privateString, "black", font )

	privateImgField.show()
	privateImgField.save("privateData.png", "PNG")
