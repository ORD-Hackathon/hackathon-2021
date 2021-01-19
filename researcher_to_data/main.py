import numpy as np
import pandas as pd
import requests as r

import api_zenodo
import data_to_metrics

ACCESS_TOKEN = "RRlabvBJSg4yFCVwILXvtTdEYoMBpQ3fw6CuGmjWNUIwXX6tmDREvQcktRLe"


def get_data_for_name(name):
    records = api_zenodo.get_record_doi_for_name(name)
    # print(records.json())


def get_data_for_orcid(orcid):
    records = api_zenodo.get_data_for_orcid(orcid)
    print(records.json())


def get_metrics_for_data(data):
    data_to_metrics


def main():
    get_data_for_name("Leitgeb, Rainer")
    # get_data_for_orcid("0000-0002-0131-4111")


if __name__ == "__main__":
    main()
