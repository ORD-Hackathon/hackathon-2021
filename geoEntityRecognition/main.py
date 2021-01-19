import os
from extractLocationFromText import ExtractLocationFromText
from getIdentifer import getWikiRecord
import time
from writeHTML import writeToHTML

def createEnglishTestResult():

    testFile = "en_magellan_voyage.txt"

    testData = os.path.join(testDataPath, "en_magellan_voyage.txt")
    text = open(testData, "r").read()
    foundLocations = parser.getLocationsEnglish(text)
    counter = 0
    for loc in foundLocations:
        print(counter)
        loc.wikiID, loc.geonameID, loc.longitude, loc.latitude = getWikiRecord(loc.text, loc.language)
        if (counter==10):
            time.sleep(60)
            counter = 0
        else :
            counter += 1
        print(loc.__dict__)
    fileBaseName, ending = os.path.splitext(os.path.basename(testFile))
    writeToHTML(text, foundLocations, fileBaseName)


if __name__ == '__main__':

    testDataPath = "test_data/"
    parser = ExtractLocationFromText()
    createEnglishTestResult()

