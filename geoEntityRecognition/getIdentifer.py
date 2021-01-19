from qwikidata.sparql  import return_sparql_query_results
import warnings
import time

def getPostition(coordinate):
    longitude, latitude = coordinate.split(" ")
    return longitude.strip('Point('), latitude.strip(')')

def getWikiRecord(name, lang):

    sparql_statement = """
    select ?wikiItem ?geonameID ?coordinate
    where {""" +\
    '?wikiItem rdfs:label "' + name + '"@' + lang + "; " +\
    """wdt:P1566 ?geonameID;\n
    wdt:P625 ?coordinate
    }
    """

    # print(sparql_statement)

    res = return_sparql_query_results(sparql_statement)
    results = res["results"]["bindings"]
    wikiId = ""
    geonameID = ""
    longitude = ""
    lattitude = ""
    if (len(results)==0) :
        warnings.warn("No records found for location " + name + " in language " + lang + ".")
    else :
        record = results[0]
        # if(len(results)>1):
        #     warnings.warn("Multiple records found for location " + name + "in language" + lang + ". Top one is chosen.")
        wikiId = record['wikiItem']['value']
        geonameID = record['geonameID']['value']
        coordinate = record['coordinate']['value']
        longitude, lattitude = getPostition(coordinate)

    return wikiId, geonameID, longitude, lattitude


def addWikiInfo(foundLocations):
    counter = 0
    for loc in foundLocations:
        print(counter)
        loc.wikiID, loc.geoNameID, loc.longitude, loc.latitude = getWikiRecord(loc.text, loc.language)
        if (counter == 10):
            time.sleep(120)
            counter = 0
        else:
            counter += 1
        print(loc.__dict__)
    return foundLocations

if __name__ == '__main__':
    print(getWikiRecord("Berlin", "de"))