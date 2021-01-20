import requests


def get_dois(orcid):
    import requests
    query = 'http://api.crossref.org/works?filter=orcid:' + orcid
    r = requests.get(query)
    r = r.json()
    results = r['message']['items']
    dois = []
    for pu in results:
        dois.append(pu['DOI'])
    return dois


dois = get_dois('0000-0003-2588-4212')
for doi in dois:
    print(doi)