import numpy as np
import pandas as pd
import requests as r
import time

ACCESS_TOKEN = "RRlabvBJSg4yFCVwILXvtTdEYoMBpQ3fw6CuGmjWNUIwXX6tmDREvQcktRLe"

# find datasets for user based on name or orcid
# get dataset properties for calculating the openness score
# get usage metrics for found datasets


def get_data_for_name(name):
    """Returns score and metrics data points for all found records, where the name is the creator."""

    # get first 10 records
    records = get_records_page_by_name(name, 0)

    # get total nr of hits
    total_nr_of_hits = int(records.get("hits").get("total"))
    total_nr_of_pages = int(total_nr_of_hits/10)
    print("total_nr_of_hits: " + str(total_nr_of_hits) + ' (' + str(total_nr_of_pages) + ' pages)')

    list_of_datasets = []

    for hit in records.get("hits").get("hits"):
        list_of_datasets.append(extract_data_from_hit(hit))

    for page in range(1, total_nr_of_pages):
        records = get_records_page_by_name(name, page)
        for hit in records.get("hits").get("hits"):
            list_of_datasets.append(extract_data_from_hit(hit))

    return list_of_datasets


def get_records_page_by_name(name, page_nr):
    # hitting rate limits. need to back off a little.
    time.sleep(0.5)
    response = ""
    if page_nr == 0:
        response = r.get(
            'https://zenodo.org/api/records',
            params={'q': 'creators.name:' + name, 'access_token': ACCESS_TOKEN}
        )
    else:
        pass
        response = r.get(
            'https://zenodo.org/api/records',
            params={'q': 'creators.name:' + name, 'page': page_nr, 'size': 10, 'access_token': ACCESS_TOKEN}
        )
    # print("get_records_page - url: " + response.url)
    # print("get_records_page - page_nr: " + str(page_nr))
    return response.json()


def extract_data_from_hit(hit):
    """Extracts the data from the Zenodo record."""

    try:
        access_right_value = hit.get("metadata").get("access_right")
        if access_right_value == 'open':
            access_open = True
        else:
            access_open = False
    except AttributeError:
        access_open = False

    license_cc_by = False
    try:
        license_id = hit.get("metadata").get("license").get("id")
    except AttributeError:
        license_id = ""

    if "CC-BY" in license_id:
        license_cc_by = True

    try:
        description_value = hit.get("metadata").get("description")
        if len(description_value) > 0:
            description = True
        else:
            description = False
    except AttributeError:
        description = False

    data = {
        "identifier": hit.get("metadata").get("doi"),
        "access_open": access_open,
        "license_cc_by": license_cc_by,
        "description": description,
    }

    stats = hit.get("stats")
    data.update(stats)

    return data


def get_data_for_orcid(orcid):
    # get first 10 records
    records = get_records_page_by_orcid(orcid, 0)

    # get total nr of hits
    total_nr_of_hits = int(records.get("hits").get("total"))
    total_nr_of_pages = int(total_nr_of_hits / 10)
    print("total_nr_of_hits: " + str(total_nr_of_hits) + ' (' + str(total_nr_of_pages) + ' pages)')

    list_of_datasets = []

    for hit in records.get("hits").get("hits"):
        list_of_datasets.append(extract_data_from_hit(hit))

    for page in range(1, total_nr_of_pages):
        records = get_records_page_by_orcid(orcid, page)
        for hit in records.get("hits").get("hits"):
            list_of_datasets.append(extract_data_from_hit(hit))

    return list_of_datasets


def get_records_page_by_orcid(orcid, page_nr):
    # hitting rate limits. need to back off a little.
    time.sleep(0.5)
    response = ""
    if page_nr == 0:
        response = r.get(
            'https://zenodo.org/api/records',
            params={'q': 'creators.orcid:' + orcid, 'access_token': ACCESS_TOKEN}
        )
    else:
        pass
        response = r.get(
            'https://zenodo.org/api/records',
            params={'q': 'creators.orcid:' + orcid, 'page': page_nr, 'size': 10, 'access_token': ACCESS_TOKEN}
        )
    # print("get_records_page - url: " + response.url)
    # print("get_records_page - page_nr: " + str(page_nr))
    return response.json()


def get_data_for_doi(doi):
    response = r.get(
        'https://zenodo.org/api/records',
        params={'q': 'doi:' + doi, 'access_token': ACCESS_TOKEN}
    )
    print(response.url)
    return response.json()
