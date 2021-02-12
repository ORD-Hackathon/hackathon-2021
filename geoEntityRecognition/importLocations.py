import requests
import json

ontoName = "geo"

def createNewResourceForLocation(loc, importedLocations):
    url = "http://localhost:3333/v2/resources"
    payload = {}
    payload["@id"] = "http://rdfh.ch/0001/" + loc.geoNameID
    payload["@type"] = ontoName + ":Location"
    payload["knora-api:attachedToProject"] = {"@id": "http://rdfh.ch/projects/0001"}
    payload[ontoName + ":hasName"] = {
        "@type": "knora-api:TextValue",
        "knora-api:valueAsString": loc.text,
        "knora-api:valueHasLanguage": loc.language,
        "knora-api:creationDate": {
            "@type": "xsd:dateTimeStamp",
            "@value": "2020-01-21T12:58:54.502951Z"
        }
    }
    payload[ontoName + ":hasGeoNameID"] = {
        "@type": "knora-api:GeonameValue",
        "knora-api:geonameValueAsGeonameCode": loc.geoNameID,
        "knora-api:creationDate": {
            "@type": "xsd:dateTimeStamp",
            "@value": "2020-01-21T12:58:54.502951Z"
        }

    }
    payload[ontoName + ":hasWikiLink"] = {"@type": "knora-api:UriValue",
                                          "knora-api:uriValueAsUri": {"@type": "xsd:anyURI", "@value": loc.wikiID},
                                          "knora-api:creationDate": {
                                              "@type": "xsd:dateTimeStamp",
                                              "@value": "2020-01-21T12:58:54.502951Z"
                                          }
                                          }
    payload["rdfs:label"] = loc.text
    payload["knora-api:creationDate"] = {
        "@type": "xsd:dateTimeStamp",
        "@value": "2020-01-21T12:58:54.502951Z"
    }
    payload["@context"] = {
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "knora-api": "http://api.knora.org/ontology/knora-api/v2#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "geo": "http://0.0.0.0:3333/ontology/0001/geo/v2#"
    }
    json_object = json.dumps(payload, indent=4)
    headers = {
        'authorization': "Basic cm9vdEBleGFtcGxlLmNvbTp0ZXN0",
        'cache-control': "no-cache",
        'postman-token': "19f719be-45ed-fa95-487d-e5510794e9b2"
    }
    response = requests.request("POST", url, data=json_object, headers=headers)
    if response.ok:
        importedLocations[loc.geoNameID] = [loc.language]
        print("Location" + loc.text + "stored!")
    else :
        print (response.content)
    return importedLocations

def createNewNameValue(loc, importedLocations):
    url = "http://localhost:3333/v2/values"
    payload = {}
    payload["@id"] = "http://rdfh.ch/0001/" + loc.geoNameID
    payload["@type"] = ontoName + ":Location"
    payload[ontoName + ":hasName"] = {
        "@type": "knora-api:TextValue",
        "knora-api:valueAsString": loc.text,
        "knora-api:valueHasLanguage": loc.language,
        "knora-api:creationDate": {
            "@type": "xsd:dateTimeStamp",
            "@value": "2020-01-21T12:58:54.502951Z"
        }
    }
    payload["@context"] = {
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "knora-api": "http://api.knora.org/ontology/knora-api/v2#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "geo": "http://0.0.0.0:3333/ontology/0001/geo/v2#"
    }


    json_object = json.dumps(payload, indent=4)
    headers = {
        'authorization': "Basic cm9vdEBleGFtcGxlLmNvbTp0ZXN0",
        'cache-control': "no-cache",
        'postman-token': "19f719be-45ed-fa95-487d-e5510794e9b2"
    }
    response = requests.request("POST", url, data=json_object, headers=headers)
    if response.ok:
        importedLocations[loc.geoNameID].append(loc.language)
        print("Location" + loc.text + "stored!")
    return importedLocations

def importLocation(foundLocations, importedLocations):

    for loc in foundLocations:

        if loc.geoNameID:
            if loc.geoNameID not in importedLocations.keys():
                createNewResourceForLocation(loc, importedLocations)
            else :
                if loc.language not in importedLocations[loc.geoNameID]:
                    createNewNameValue(loc, importedLocations)
    return importedLocations

