import os
def writeToHTML(text, foundLocations, outputFile):
    htmlFile = os.path.join('results', outputFile+'.html')
    first_index = 0
    html_body = ""
    for loc in foundLocations:
        html_body += text[first_index:loc.startChar]
        if loc.wikiID:
            html_body += '<a href="' + loc.wikiID + '">' + loc.text + "</a>"
        else :
            html_body += '<span style="color: #ff0000">' + loc.text + '</span>'

        first_index = loc.endChar

    lastLocation = foundLocations[-1].endChar
    html_body += text[lastLocation:]
    html_content = """<html>
        <head></head>\n
        <body>\n<p>""" + html_body + """\n</p>\n</body>
        </html>"""

    f = open(htmlFile, "w")
    f.write(html_content)
    f.close()