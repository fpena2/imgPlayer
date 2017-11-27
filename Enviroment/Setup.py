"""Setup function, which calls individual modules in order"""
import enviromentSetup
import cascadeSetup
import time


def Setup(): 
	# Sets up folders needed 
	enviromentSetup.setupFolders()
	enviromentSetup.getAndResizeImages()
	enviromentSetup.createNegatives()
	time.sleep(2)

	#Parameters 
	inputImg = "pictureToDetect.png"
	inputNumb = 1900

	# Sends Commands to create cascade XML file 
	cascadeSetup.createPositiveSamples(inputImg, str(inputNumb))
	time.sleep(5)
	cascadeSetup.createVector(str(inputNumb))
	time.sleep(5)
	cascadeSetup.createCascade(inputNumb)


Setup()
