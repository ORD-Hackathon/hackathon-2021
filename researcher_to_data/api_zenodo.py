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
    records = get_records_page(name, 0)

    # get total nr of hits
    total_nr_of_hits = int(records.get("hits").get("total"))
    print("total_nr_of_hits: " + str(total_nr_of_hits))
    total_nr_of_pages = int(total_nr_of_hits/10)
    print("total_nr_of_pages: " + str(total_nr_of_pages))

    # extract ids
    list_of_ids = [item.get("conceptrecid") for item in records.get("hits").get("hits")]

    # if there is a link to the next (10 records) page, go and fetch it
    next_page_url = records.get("links").get("next")
    print("next:" + next_page_url)

    for page in range(1, total_nr_of_pages):
        records = get_records_page(name, page)
        list_of_ids_on_page = [item.get("conceptrecid") for item in records.get("hits").get("hits")]
        list_of_ids += list_of_ids_on_page

    # print the final list
    print(list_of_ids)


def get_records_page(name, page_nr):
    # hitting rate limits. need to back off a little.
    time.sleep(1)
    response = ""
    if page_nr == 0:
        response = r.get(
            'https://zenodo.org/api/records',
            params={'q': 'creators.name:' + name, 'access_token': ACCESS_TOKEN}
        )
    else:
        response = r.get(
            'https://zenodo.org/api/records',
            params={'q': 'creators.name:' + name, 'page': page_nr, 'size': 10, 'access_token': ACCESS_TOKEN}
        )
    # print("get_records_page - url: " + response.url)
    print("get_records_page - page_nr: " + str(page_nr))
    return response.json()


def get_data_for_orcid(orcid):
    return r.get(
        'https://zenodo.org/api/records',
        params={'q': 'creators.orcid:' + orcid, 'access_token': ACCESS_TOKEN}
    )


def get_data_for_doi(doi):
    response = r.get(
        'https://zenodo.org/api/records',
        params={'q': 'creators.orcid:' + orcid, 'access_token': ACCESS_TOKEN}
    )
    print(response.url)
    return response.json()
