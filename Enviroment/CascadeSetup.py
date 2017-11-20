import subprocess

def createPositiveSamples(inputImg, inputNumb):
	# Command required by OpenCV to create positives samples 
	CV2SamplesCommand = "opencv_createsamples -img " + inputImg +" -bg negMap.txt -info positives/info.lst -pngoutput positives -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num " + inputNumb 
	subprocess.call(list[CV2SamplesCommand])

def createVector(inputNumb):
	# Creates Vector file needed to create a cascade file 
	CV2VectorCommand = "opencv_createsamples -info positives/info.lst -num " + inputNumb + " -w 20 -h 20 -vec positives.vec"
	subprocess.call(list[CV2VectorCommand])

def createCascade():
	# Creates Cascade file needed for object recognition 
	CV2CascadeCommand = "opencv_traincascade -data data -vec positives.vec -bg negMap.txt -numPos 1800 -numNeg 900 -numStages 10 -w 20 -h 20"
	subprocess.call(list[CV2CascadeCommand])
