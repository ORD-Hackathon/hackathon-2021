
## @Ivan: What format should the dataset be in? Can't always use DOI as unique identifier, as some daataset recrods won't have DOIs.

# The data should be a dictionary in the following form:
# {
#   identifier: string,
#   access_open: True/False,
#   license_cc_by: True/False,
#   accrual_method: True/False,
#   accrual_policy: True/False,
#   available: True/False,
#   date: True/False,
#   date_accepted: True/False,
#   date_copyrighted: True/False,
#   date_submitted: True/False,
#   description: True/False,
#   format_proprietary_or_not_available: Ture/False,
#   has_versions: True/False,
#   identifier_available: True/False,
#   language_available: True/False,
#   provenance_rights: True/False,
#   rights_holder_available: True/False,
#   subject: True/False,
#   title_available: True/False,
#   type_available: True/False,
#   downloads: 0.0,
#   unique_downloads: 0.0,
#   unique_views: 0.0,
#   version_downloads: 0.0,
#   version_unique_downloads: 0.0,
#   version_unique_views: 0.0,
#   version_views: 0.0,
#   version_volume: 0.0,
#   views: 0.0,
#   volume: 0.0
# }

def dataset_to_score(data):
    """Returns Openness Score for a single dataset record"""
    score = 0
    if data.get("access_open"):
        if data.get("license_cc_by"):
            score = 100
        else:
            score = 0
    else:
        score = 0

    if not data.get("accrual_method"):
        score -= 3

    if not data.get("accrual_policy"):
        score -= 1

    # TODO: add the rest

    return score


def dataset_to_usage_stats(data):
    """Returns Usage stats for a single dataset record"""
    stats = {
        "downloads": data.get("downloads"),
        "unique_views": data.get("unique_views"),
        "version_downloads": data.get("version_downloads"),
        "version_unique_downloads": data.get("version_unique_downloads"),
        "version_unique_views": data.get("version_unique_views"),
        "version_views": data.get("version_views"),
        "version_volume": data.get("version_volume"),
        "views": data.get("views"),
        "volume": data.get("volume"),
    }

    return stats


def datasets_to_scores(list_of_datasets):
    """Returns aggregated metrics for a list of datasets"""
    # Uses both funtions above

    identifiers = []
    openness_scores = []
    usage_stats = []

    for data in list_of_datasets:
        identifiers += data.get("identifier")
        openness_scores += dataset_to_score(data)
        usage_stats += dataset_to_usage_stats(data)

    result = {
        "ids": identifiers,
        "openness_scores": openness_scores,
        "usage_stats": usage_stats
    }

    return result
