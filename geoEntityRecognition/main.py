import os
from extractLocationFromText import ExtractLocationFromText
from getIdentifer import getWikiRecord
import time


if __name__ == '__main__':

    testDataPath = "test_data/"
    parser = ExtractLocationFromText()
    englishTestData = os.path.join(testDataPath, "en_magellan_voyage.txt")
    englishText = open(englishTestData, "r").read()
    foundLocations = parser.getLocationsEnglish(englishText)
    counter = 0
    for loc in foundLocations:
        loc.wikiID, loc.geonameID, loc.longitude, loc.latitude = getWikiRecord(loc.text, loc.language)
        if (counter>10):
            time.sleep(60)
            counter = 0
        else :
            counter += 1
        print(loc.__dict__)

