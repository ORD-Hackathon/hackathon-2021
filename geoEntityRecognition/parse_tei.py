from geoEntity import GeoEntity
from lxml import etree as et
import re

def parse_locations_from_tei(filepath):
    # Reads the file
    root = et.parse(filepath).getroot()

    # String snippet for specify TEI tags in XML
    tei_string = re.search("{.*}", root.tag)
    tei_string = tei_string.group() if tei_string else ""

    # Extracts list of matches for <place> tag.
    places = list(root.iterfind(f".//{tei_string}place"))

    foundLocations = []
    for place in places:
        # Find the place of the name (GeoEntity.text property)
        placeName = place.find(f".//{tei_string}placeName")

        # Optionally adds region and country if that information is available
        regionName = place.find(f".//{tei_string}region")
        countryName = place.find(f".//{tei_string}country")
        placeName = f"{placeName.text}{', ' + regionName.text if regionName is not None else ''}{', ' + countryName.text if countryName is not None else ''}"
        
        # Leaving GPE as the defulat label type for now
        label = "GPE"

        # Coordinates are stored as space-separated string of the form <geo>lat long</geo>
        placeCoords = place.find(f".//{tei_string}geo").text.split()

        # Creating and appending new GeoEntity for each location found
        entity = GeoEntity(text=placeName, label=label, lang="en", lat=placeCoords[0], lon=placeCoords[1])
        foundLocations.append(entity)
    
    return foundLocations

if __name__ == "__main__":
    foundLocations = parse_locations_from_tei('test_data/cities_example.xml')
    for loc in foundLocations:
        print(f"{vars(loc)}\n")

