import os
from extractLocationFromText import ExtractLocationFromText
from getIdentifer import getWikiRecord
from lxml import etree as et

def loc_with_link(loc):
    return f'<a href="{loc.wikiID}">{loc.text}</a>' if loc.wikiID else f'<span style="color: #ff0000">{loc.text}</span>'


if __name__ == '__main__':

    testDataPath = "test_data/"
    parser = ExtractLocationFromText()
    englishTestData = os.path.join(testDataPath, "en_magellan_voyage.txt")
    englishText = open(englishTestData, "r").read()
    foundLocations = parser.getLocationsEnglish(englishText)
    print("****")
    print("type: ", type(foundLocations))
    for loc in foundLocations:
        loc.wikiID, loc.geonameID, loc.longitude, loc.lattitude = getWikiRecord(loc.text, loc.language)
        englishText = englishText.replace(f" {loc.text}", " " + loc_with_link(loc))
    
    # Adding paragraph tags for each line.
    englishText = ["<p>" + x + "</p>" for x in englishText.split("\n")]

    # Creating HTML file
    root = et.Element("html")
    head = et.SubElement(root, "head")
    body = et.SubElement(root, "body")
    title = et.SubElement(body, "h1")
    title.text = "The Tales of Magellan"

    # Adding a new paragraph for each line in englishText
    for line in englishText:
        elem = et.fromstring(line)
        body.append(elem)

    # Writing the HTML to disk
    with open("demo.html", "wb") as f:
        f.write(et.tostring(root, pretty_print=True))
    