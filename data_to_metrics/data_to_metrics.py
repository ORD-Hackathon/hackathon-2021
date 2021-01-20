
## @Ivan: What format should the dataset be in? Can't always use DOI as unique identifier, as some daataset recrods won't have DOIs.

# The data should be a dictionary in the following form:
# {
#   identifier: string (doi or link)
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
    if data.get("access_open") and data.get("license_cc_by"):
        score = 100
        if not data.get("accrual_method"):
            score -= 3

        if not data.get("accrual_policy"):
            score -= 1

        if not data.get("available"):
            score -= 1

        if not data.get("date"):
            score -= 2

        if not data.get("date_accepted"):
            score -= 1

        if not data.get("date_copyrighted"):
            score -= 1

        if not data.get("date_submitted"):
            score -= 1

        if not data.get("description"):
            score -= 3

        if not data.get("format_proprietary_or_not_available"):
            score -= 3

        if not data.get("has_versions"):
            score -= 2

        if not data.get("identifier_available"):
            score -= 5

        if not data.get("language_available"):
            score -= 2

        if not data.get("provenance_rights"):
            score -= 5

        if not data.get("rights_holder_available"):
            score -= 2

        if not data.get("subject"):
            score -= 2

        if not data.get("title_available"):
            score -= 5

        if not data.get("type_available"):
            score -= 2

        return score
    else:
        return 0


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
        identifiers.append(data.get("identifier"))
        openness_scores.append(dataset_to_score(data))
        usage_stats.append(dataset_to_usage_stats(data))
        
        unique_views = []
        for record in range(0,len(usage_stats)):
            unique_views.append(usage_stats[record]['unique_views'])
        avg_unique_views = sum(unique_views)/len(unique_views)
        
        downloads = []
        for record in range(0,len(usage_stats)):
            downloads.append(usage_stats[record]['downloads'])
        avg_downloads = sum(downloads)/len(downloads)
        



    result = {
        "ids": identifiers,
        "openness_score": sum(openness_scores)/max(1,len(openness_scores)),
        "usage_stats": usage_stats,
        "avg_unique_views":avg_unique_views,
        "avg_downloads":avg_downloads
    }


    return result