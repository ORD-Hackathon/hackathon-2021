import os
from extractLocationFromText import ExtractLocationFromText
from getIdentifier import addWikiInfo
from writeHTML import writeToHTML
from importLocations import importLocation


def createEnglishTestResult(importedLocations):

    testFile = "en_swiss.txt"
    testData = os.path.join(testDataPath, testFile)
    text = open(testData, "r").read()
    foundLocations = parser.getLocationsEnglish(text)
    updatedLocations = addWikiInfo(foundLocations=foundLocations)
    # fileBaseName, ending = os.path.splitext(os.path.basename(testFile))
    # writeToHTML(text, updatedLocations, fileBaseName)
    importedLocations = importLocation(foundLocations=updatedLocations, importedLocations=importedLocations)
    print(importedLocations)

def createGermanTestResult(importedLocations):
    testFile = "de_swiss.txt"
    testData = os.path.join(testDataPath, testFile)
    text = open(testData, "r").read()
    foundLocations = parser.getLocationsGerman(text)
    updatedLocations = addWikiInfo(foundLocations=foundLocations)
    # fileBaseName, ending = os.path.splitext(os.path.basename(testFile))
    # writeToHTML(text, updatedLocations, fileBaseName)
    importedLocations = importLocation(foundLocations=updatedLocations, importedLocations=importedLocations)
    print(importedLocations)

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
    importedLocations = {}
    createEnglishTestResult(importedLocations)
    createGermanTestResult(importedLocations)

