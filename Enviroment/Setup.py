"""Setup function, which calls individual modules in order"""
import enviromentSetup
import cascadeSetup

def Setup():
    # Sets up folders and negative images needed to create the cascade
    enviromentSetup.setupFolders()
    enviromentSetup.getAndResizeImages()
    enviromentSetup.createNegatives()

    # Parameters which are feed to the commands to generate the cascade
    inputImg = "pictureToDetect.png"
    inputNumb = 1900
    inputNumbPos = inputNumb - 100

    # Sends Commands to create cascade/XML file
    cascadeSetup.createPositiveSamples(inputImg, str(inputNumb))
    cascadeSetup.createVector(str(inputNumb))
    cascadeSetup.createCascade(inputNumbPos)
    cascadeSetup.createCascade(inputNumbPos)
    cascadeSetup.moveFolder()


Setup()
