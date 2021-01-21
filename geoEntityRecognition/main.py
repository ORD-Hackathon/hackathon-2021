from createLocationResources import *
from createDocumentResources import createDocumentResource

importedLocations = {}

if __name__ == '__main__':
    testDataPath = "test_data/"

    testFile = "en_swiss.txt"
    testData = os.path.join(testDataPath, testFile)
    foundLocations, importedLocations = createLocationsInEnglishText(importedLocations, testData)
    testFile = "de_swiss.txt"
    testData = os.path.join(testDataPath, testFile)
    foundLocations, importedLocations = createLocationsInGermanText(importedLocations, testData)
    createDocumentResource(testData, foundLocations, 'wiki_swiss_de', 'xmlDeutsch.xml')


