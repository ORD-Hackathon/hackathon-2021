import os
from extractLocationFromText import ExtractLocationFromText
from getIdentifer import getWikiRecord


if __name__ == '__main__':

    testDataPath = "test_data/"
    parser = ExtractLocationFromText()
    englishTestData = os.path.join(testDataPath, "en_magellan_voyage.txt")
    englishText = open(englishTestData, "r").read()
    foundLocations = parser.getLocationsEnglish(englishText)
    for loc in foundLocations:
        loc.wikiID, loc.geonameID, loc.longitude, loc.latitude = getWikiRecord(loc.text, loc.language)
        print(loc.__dict__)

