#this is the cascade file
#it allows the program to seek out certain demographics
import os

def createPositiveSamples(inputImg, inputNumb):
	# Command required by OpenCV to create positives samples 
	CV2SamplesCommand = "opencv_createsamples -img " + inputImg +" -bg negativesMap.txt -info positives/info.lst -pngoutput positives -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num " + inputNumb
	os.system(CV2SamplesCommand) 

def createVector(inputNumb):
	# Creates Vector file needed to create a cascade file 
	CV2VectorCommand = "opencv_createsamples -info positives/info.lst -num " + inputNumb + " -w 20 -h 20 -vec positives.vec"
	os.system(CV2VectorCommand)

def createCascade(inputNumb):
	# Creates Cascade file needed for object recognition 
	CV2CascadeCommand = "opencv_traincascade -data data -vec positives.vec -bg negativesMap.txt -numPos " + str(inputNumb) +" -numNeg " + str(inputNumb/2) +" -numStages 10 -w 20 -h 20"
	os.system(CV2CascadeCommand)
