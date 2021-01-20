import numpy as np
import pandas as pd
import requests as r

import api_zenodo
import data_to_metrics.data_to_metrics as dtm

ACCESS_TOKEN = "RRlabvBJSg4yFCVwILXvtTdEYoMBpQ3fw6CuGmjWNUIwXX6tmDREvQcktRLe"


def get_data_for_name(name):
    data = api_zenodo.get_data_for_name(name)
    return data


def get_data_for_orcid(orcid):
    data = api_zenodo.get_data_for_orcid(orcid)
    return data


def get_metrics_for_data(data):
    metrics = dtm.datasets_to_scores(data)
    return metrics


def main():
    data1 = get_data_for_name("Leitgeb AND Rainer")
    print(data1)
    metrics1 = get_metrics_for_data(data1)
    print(metrics1)

    data2 = get_data_for_orcid("0000-0002-0131-4111")
    print(data2)
    metrics2 = get_metrics_for_data(data2)
    print(metrics2)


if __name__ == "__main__":
    main()
