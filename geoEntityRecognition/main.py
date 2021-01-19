import os
from extractLocationFromText import ExtractLocationFromText
from getIdentifer import addWikiInfo
from writeHTML import writeToHTML



def createEnglishTestResult():

    testFile = "en_magellan_voyage.txt"
    testData = os.path.join(testDataPath, testFile)
    text = open(testData, "r").read()
    foundLocations = parser.getLocationsEnglish(text)
    updatedLocations = addWikiInfo(foundLocations=foundLocations)
    fileBaseName, ending = os.path.splitext(os.path.basename(testFile))
    writeToHTML(text, updatedLocations, fileBaseName)

def createGermanTestResult():
    testFile = "de_mozartItalienReise.txt"
    testData = os.path.join(testDataPath, testFile)
    text = open(testData, "r").read()
    foundLocations = parser.getLocationsGerman(text)
    updatedLocations = addWikiInfo(foundLocations=foundLocations)
    fileBaseName, ending = os.path.splitext(os.path.basename(testFile))
    writeToHTML(text, updatedLocations, fileBaseName)

def createFrenchTestResult():
    testFile = "fr_paris_a_Jerusalem.txt"
    testData = os.path.join(testDataPath, testFile)
    text = open(testData, "r").read()
    foundLocations = parser.getLocationsFrench(text)
    updatedLocations = addWikiInfo(foundLocations=foundLocations)
    fileBaseName, ending = os.path.splitext(os.path.basename(testFile))
    writeToHTML(text, updatedLocations, fileBaseName)


def createItalianTestResult():
    testFile = "it_marcOPollo.txt"
    testData = os.path.join(testDataPath, testFile)
    text = open(testData, "r").read()
    foundLocations = parser.getLocationsItalian(text)
    updatedLocations = addWikiInfo(foundLocations=foundLocations)
    fileBaseName, ending = os.path.splitext(os.path.basename(testFile))
    writeToHTML(text, updatedLocations, fileBaseName)

if __name__ == '__main__':

    testDataPath = "test_data/"
    parser = ExtractLocationFromText()
    createGermanTestResult()

