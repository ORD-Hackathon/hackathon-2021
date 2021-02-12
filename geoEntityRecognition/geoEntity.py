class GeoEntity:
    def __init__(self, text, label, startChar=None, endChar=None, lang="en", lon=None, lat=None):
        self.label = label # e.g., GPE for geo-political entities
        self.text = text # name of the location
        self.startChar = startChar
        self.endChar = endChar
        self.language = lang
        self.geoNameID = ""
        self.wikiID = ""
        self.longitude = lon
        self.latitude = lat