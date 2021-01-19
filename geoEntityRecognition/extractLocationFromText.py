import spacy
import os
from geoEntity import GeoEntity


class ExtractLocationFromText:
    def __init__(self):
        self.locationLabels = ['GPE', 'LOC', 'FAC']

    def extractLocationEntities(self, entities, lang):
        foundLocations = []
        geoEntities = list(filter(lambda ent: ent.label_ in self.locationLabels, entities))

        for ent in geoEntities:
            entity = GeoEntity(ent.text, ent.label_, ent.start_char, ent.end_char, lang)
            foundLocations.append(entity)

        return foundLocations

    def getLocationsEnglish(self, text):
        # load pretrained english model
        englishModel = spacy.load("en_core_web_sm")

        # extrac geo entities
        doc = englishModel(text)
        return self.extractLocationEntities(doc.ents, 'en')

    def getLocationsGerman(self, text):
        # load pretrained german model
        germanhModel = spacy.load("de_core_news_sm")

        # extrac geo entities
        doc = germanhModel(text)
        return self.extractLocationEntities(doc.ents, 'de')

    def getLocationsFrench(self, text):
        # load pretrained french model
        frenchhModel = spacy.load("fr_core_news_sm")

        # extrac geo entities
        doc = frenchhModel(text)
        return self.extractLocationEntities(doc.ents, 'fr')

    def getLocationsItalian(self, text):
        # load pretrained italian model
        italianModel = spacy.load("it_core_news_sm")

        # extrac geo entities
        doc = italianModel(text)
        return self.extractLocationEntities(doc.ents, 'it')


def pretty_print(locations):
    return '\n'.join([str(d) for d in locations])

if __name__ == '__main__':
    testDataPath = "test_data/"
    parser = ExtractLocationFromText()
    englishTestData = os.path.join(testDataPath, "en_magellan_voyage.txt")
    englishText = open(englishTestData, "r").read()
    foundLocations = parser.getLocationsEnglish(englishText)
    print(f"---English---\nLocations found: {len(foundLocations)}\nResults:\n{pretty_print(foundLocations)}\n\n")

    germanTestData = os.path.join(testDataPath, "de_mozartItalienReise.txt")
    germanText = open(germanTestData, "r").read()
    foundLocations = parser.getLocationsGerman(germanText)
    print(f"---German---\nLocations found: {len(foundLocations)}\nResults:\n{pretty_print(foundLocations)}\n\n")

    frenchTestData = os.path.join(testDataPath, "fr_paris_a_Jerusalem.txt")
    frenchText = open(frenchTestData, "r").read()
    foundLocations = parser.getLocationsFrench(frenchText)
    print(f"---French---\nLocations found: {len(foundLocations)}\nResults:\n{pretty_print(foundLocations)}\n\n")

    italianTestData = os.path.join(testDataPath, "it_marcOPollo.txt")
    italianText = open(italianTestData, "r").read()
    foundLocations = parser.getLocationsItalian(italianText)
    print(f"---Italian---\nLocations found: {len(foundLocations)}\nResults:\n{pretty_print(foundLocations)}\n\n")