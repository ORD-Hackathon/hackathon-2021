import os
from extractLocationFromText import ExtractLocationFromText
from getIdentifer import getWikiRecord
import time
from writeHTML import writeToHTML


if __name__ == '__main__':

    testDataPath = "test_data/"
    parser = ExtractLocationFromText()
    testData = os.path.join(testDataPath, "fr_paris_a_Jerusalem.txt")
    text = open(testData, "r").read()
    foundLocations = parser.getLocationsFrench(text)
    counter = 0
    for loc in foundLocations:
        print(counter)
        loc.wikiID, loc.geonameID, loc.longitude, loc.latitude = getWikiRecord(loc.text, loc.language)
        if (counter==10):
            time.sleep(60)
            counter = 0
        else :
            counter += 1
        print(loc.__dict__)

    html_body = writeToHTML(text, foundLocations)
    html_content= """<html>
    <head></head>\n
    <body>\n<p>""" + html_body + """\n</p>\n</body>
    </html>"""

    f = open("fr_paris_a_Jerusalem.html", "w")
    f.write(html_content)
    f.close()
