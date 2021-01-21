from geoEntity import GeoEntity
from lxml import etree as et
import re
from getIdentifier import addWikiInfo

def parse_locations_from_tei(filepath):
    # Reads the file
    root = et.parse(filepath).getroot()
    # et.dump(root)

    # String snippet for specify TEI tags in XML
    tei_string = re.search("{.*}", root.tag)
    tei_string = tei_string.group() if tei_string else ""

    # Extracts list of matches for <place> tag.
    places = list(root.iterfind(f".//{tei_string}place"))

    foundLocations = []
    for place in places:
        # Find the place of the name (GeoEntity.text property)
        placeName = place.find(f"{tei_string}placeName")
        placeName = placeName.text if placeName is not None else ''

        # # Optionally adds region and country if that information is available
        # regionName = place.find(f".//{tei_string}region")
        # countryName = place.find(f".//{tei_string}country")
        # placeName = f"{placeName.text if placeName is not None else ''}{', ' + regionName.text if regionName is not None else ''}{', ' + countryName.text if countryName is not None else ''}"
        
        # Leaving GPE as the defulat label type for now
        label = "GPE"

        # Coordinates are stored as space-separated string of the form <geo>lat long</geo>
        placeCoords = place.find(f".//{tei_string}geo").text.split() if place.find(f".//{tei_string}geo") is not None else ""
        lat = placeCoords[0] if placeCoords else None
        lon = placeCoords[1] if placeCoords else None

        # Creating and appending new GeoEntity for each location found
        entity = GeoEntity(text=placeName, label=label, lang="en", lat=lat, lon=lon)
        foundLocations.append(entity)

        # foundLocations = addWikiInfo(foundLocations)
    
    return foundLocations

if __name__ == "__main__":
    foundLocations = parse_locations_from_tei('test_data/cities_example.xml')
    for loc in foundLocations:
        print(f"{vars(loc)}\n")

