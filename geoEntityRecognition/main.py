from createLocationResources import *
from createDocumentResources import createDocumentResource
import os
import time
importedLocations = {}

if __name__ == '__main__':
    testDataPath = "test_data/"

    testFile = "en_swiss.txt"
    testData = os.path.join(testDataPath, testFile)
    foundLocations, importedLocations = createLocationsInEnglishText(importedLocations, testData)
    createDocumentResource(testData, foundLocations, 'wiki_swiss_en', 'xmlEnglish.xml')
    print("Locations in English text imported")
    time.sleep(90)
    testFile = "de_swiss.txt"
    testData = os.path.join(testDataPath, testFile)
    foundLocations, importedLocations = createLocationsInGermanText(importedLocations, testData)
    createDocumentResource(testData, foundLocations, 'wiki_swiss_de', 'xmlDeutsch.xml')
    print("Locations in German text imported")

