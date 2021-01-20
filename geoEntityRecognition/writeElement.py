import os
from lxml import etree as et
import codecs


def writeToHTML(text, foundLocations, outputFile):
    htmlFile = os.path.join('results', outputFile+'.html')
    root = et.Element("html")
    head = et.SubElement(root, "head")
    body = et.SubElement(root, "body")
    title = et.SubElement(body, "h1")
    title.text = outputFile

    first_index = 0
    html_body = "<p>"
    for loc in foundLocations:
        html_body += text[first_index:loc.startChar]
        if loc.wikiID:
            html_body += '<a href="' + loc.wikiID + '">' + loc.text + "</a>"
        else :
            html_body += '<span style="color: #ff0000">' + loc.text + '</span>'

        first_index = loc.endChar

    lastLocation = foundLocations[-1].endChar
    html_body += text[lastLocation:] + "</p>"
    body.append(et.fromstring(html_body))
    # Writing the HTML to disk
    with open(htmlFile, "wb") as f:
        f.write(et.tostring(root, pretty_print=True))

def writeToXMLForImport(text, foundLocations):
    root = et.Element('text')
    paragraph = et.SubElement(root, 'p')
    paragraph.text = ""
    first_index = 0
    for loc in foundLocations:
        paragraph.text += text[first_index:loc.startChar]
        if loc.geoNameID:
            paragraph.text += '<a class=salsah-link href="http://rdfh.ch/0001/' + loc.geoNameID + '">' + loc.text + "</a>"

        first_index = loc.endChar

    lastLocation = foundLocations[-1].endChar
    paragraph.text += text[lastLocation:]
    # file = codecs.open('xmlEnglish.xml', 'w', 'utf-8')
    # file.write()
    # file.write(et.tostring(root, pretty_print=True, encoding='unicode'))
    # file.close()
    return '<?xml version="1.0" encoding="UTF-8"?>\n' + et.tostring(root, pretty_print=True)