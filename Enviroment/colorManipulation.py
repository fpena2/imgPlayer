from PIL import Image
import cv2

#this is a block of code that takes a colored picture
#converts it to grayscale for better face detection
def image_to_grayscale(picture):
  image = cv2.imread(picture)
  gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  return cv2.imshow(picture, gray_image) 

#test code--earlier attempts of me trying to code
#image_to_grayscale('testface.jpg')
#image = Image.open('testface.jpg')
#image.show()
#print(image)
