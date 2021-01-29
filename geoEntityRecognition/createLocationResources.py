from getIdentifier import addWikiInfo
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

def createLocationsInFrenchText(importedLocations, testData):
    text = open(testData, "r").read()
    foundLocations = parser.getLocationsFrench(text)
    updatedLocations = addWikiInfo(foundLocations=foundLocations)
    importedLocations = importLocation(foundLocations=updatedLocations, importedLocations=importedLocations)

    return updatedLocations, importedLocations


def createLocationsInItalianText(importedLocations, testData):
    text = open(testData, "r").read()
    foundLocations = parser.getLocationsItalian(text)
    updatedLocations = addWikiInfo(foundLocations=foundLocations)
    importedLocations = importLocation(foundLocations=updatedLocations, importedLocations=importedLocations)

    return updatedLocations, importedLocations