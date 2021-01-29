from writeElement import writeToXMLForImport
import json
import codecs
import requests

def importDocument(textContent, name):
    url = "http://localhost:3333/v2/resources"
    payload = {}
    payload["@id"] = "http://rdfh.ch/0001/document_" + name
    payload["@type"] = "geo:Document"
    payload["knora-api:attachedToProject"] = {"@id": "http://rdfh.ch/projects/0001"}
    payload["geo:hasTextWithLocation"] = {
        "@type": "knora-api:TextValue",
        "knora-api:textValueAsXml": textContent,
        "knora-api:textValueHasMapping": { "@id": "http://rdfh.ch/standoff/mappings/StandardMapping"},
        "knora-api:creationDate": {
            "@type": "xsd:dateTimeStamp",
            "@value": "2020-01-21T12:58:54.502951Z"
        }
    }
    payload["rdfs:label"] = name
    payload["knora-api:creationDate"] = {
        "@type": "xsd:dateTimeStamp",
        "@value": "2020-01-21T12:58:54.502951Z"
    }
    payload["@context"] = {
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "knora-api": "http://api.knora.org/ontology/knora-api/v2#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "anything": "http://0.0.0.0:3333/ontology/0001/anything/v2#"
    }
    json_object = json.dumps(payload, indent=4)
    headers = {
        'authorization': "Basic cm9vdEBleGFtcGxlLmNvbTp0ZXN0",
        'cache-control': "no-cache",
        'postman-token': "19f719be-45ed-fa95-487d-e5510794e9b2"
    }
    response = requests.request("POST", url, data=json_object, headers=headers)
    if response.ok:
        print("Document "+ name + "is stored!")

def createDocumentResource(text, updatedLocations, name, outputFile):
    pureText = open(text, "r").read()
    writeToXMLForImport(pureText, updatedLocations, outputFile)
    # textContent = codecs.open(outputFile, 'r', encoding='utf8')
    # importDocument(textContent, name)