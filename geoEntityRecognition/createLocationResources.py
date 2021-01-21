from getIdentifer import addWikiInfo
from writeElement import writeToHTML
from importLocations import importLocation
import os
from extractLocationFromText import ExtractLocationFromText

parser = ExtractLocationFromText()

def createLocationsInEnglishText(importedLocations, testData):

    text = open(testData, "r").read()
    foundLocations = parser.getLocationsEnglish(text)
    updatedLocations = addWikiInfo(foundLocations=foundLocations)
    importedLocations = importLocation(foundLocations=updatedLocations, importedLocations=importedLocations)

    return updatedLocations, importedLocations

def createLocationsInGermanText(importedLocations, testData):
    text = open(testData, "r").read()
    foundLocations = parser.getLocationsGerman(text)
    updatedLocations = addWikiInfo(foundLocations=foundLocations)
    importedLocations = importLocation(foundLocations=updatedLocations, importedLocations=importedLocations)

    return updatedLocations, importedLocations

def createLocationsInFrenchText(importedLocations):
    testFile = "fr_paris_a_Jerusalem.txt"
    testData = os.path.join(testDataPath, testFile)
    text = open(testData, "r").read()
    foundLocations = parser.getLocationsFrench(text)
    updatedLocations = addWikiInfo(foundLocations=foundLocations)
    importedLocations = importLocation(foundLocations=updatedLocations, importedLocations=importedLocations)

    return updatedLocations, importedLocations


def createLocationsInItalianText(importedLocations):
    testFile = "it_marcOPollo.txt"
    testData = os.path.join(testDataPath, testFile)
    text = open(testData, "r").read()
    foundLocations = parser.getLocationsItalian(text)
    updatedLocations = addWikiInfo(foundLocations=foundLocations)
    importedLocations = importLocation(foundLocations=updatedLocations, importedLocations=importedLocations)

    return updatedLocations, importedLocations