import spacy
import os

locationLabels = ['GPE', 'LOC', 'FAC']


class GeoEntity:
    def __init__(self, text, label, startChar, endChar):
        self.label = label
        self.text = text
        self.startChar = startChar
        self.endChar = endChar


def extractLocations(entities):
    foundLocations = []
    geoEntities = list(filter(lambda ent: ent.label_ in locationLabels, entities))

    for ent in geoEntities:
        entity = GeoEntity(ent.text, ent.label_, ent.start_char, ent.end_char)
        foundLocations.append(entity.__dict__)

    return foundLocations


def getLocationsEnglish(text):
    # load pretrained english model
    englishModel = spacy.load("en_core_web_sm")

    # extrac geo entities
    doc = englishModel(text)
    return extractLocations(doc.ents)


def getLocationsGerman(text):
    # load pretrained german model
    germanhModel = spacy.load("de_core_news_sm")

    # extrac geo entities
    doc = germanhModel(text)
    return extractLocations(doc.ents)

if __name__ == '__main__':
    testDataPath = "test_data/"
    englishTestData = os.path.join(testDataPath, "en_magellan_voyage.txt")
    englishText = open(englishTestData, "r").read()
    print(getLocationsEnglish(englishText))

    germanTestData = os.path.join(testDataPath, "de_mozartItalienReise.txt")
    germanText = open(germanTestData, "r").read()
    print(getLocationsGerman(germanText))