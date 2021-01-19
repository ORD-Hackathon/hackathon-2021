class GeoEntity:
    def __init__(self, text, label, startChar, endChar, lang, lon="", lat=""):
        self.label = label
        self.text = text
        self.startChar = startChar
        self.endChar = endChar
        self.language = lang
        self.geoNameID = ""
        self.wikiID = ""
        self.longitude = lon
        self.latitude = lat