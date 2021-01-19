import numpy as np
import pandas as pd
import requests as r

ACCESS_TOKEN = "RRlabvBJSg4yFCVwILXvtTdEYoMBpQ3fw6CuGmjWNUIwXX6tmDREvQcktRLe"

# find datasets for user based on name or orcid
# get dataset properties for calculating the openness score
# get usage metrics for found datasets


def get_record_dois_for_name(name):
    """Returns all found dois for records, where the name is the creator."""
    records = r.get(
        'https://zenodo.org/api/records',
        params={'q': 'creators.name:' + name, 'access_token': ACCESS_TOKEN}
    ).json()

    concepts = records.get("hits").get("hits")
    print("nr of concepts found: " + str(len(concepts)))

    li = [item.get("conceptrecid") for item in records.get("hits").get("hits")]

    if records.get("links").get("next") is not None:
        li += [item.get("conceptrecid") for item in records.get("hits").get("hits")]

    print(li)

def get_record_dois_for_next_page(page):
    pass


def get_data_for_orcid(orcid):
    return r.get(
        'https://zenodo.org/api/records',
        params={'q': 'creators.orcid:' + orcid, 'access_token': ACCESS_TOKEN}
    )


def get_data_for_doi(doi):
    return r.get(
        'https://zenodo.org/api/records',
        params={'q': 'creators.orcid:' + orcid, 'access_token': ACCESS_TOKEN}
    )
