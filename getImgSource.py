import os

def imgSouce(pathToScan="src"):
    fileTypes = [".png", ".jpg"]
    filesFound = []

    for img in os.listdir(pathToScan):
        newPath = os.path.join(pathToScan, img)
        if not os.path.isdir(newPath):
            for extension in fileTypes:
                if newPath.endswith(extension):
                    filesFound.append(img)

    return (filesFound)
