import requests

orcid = 'orcid:0000-0003-2588-4212'
query = 'http://api.crossref.org/works?filter=orcid:' + orcid

r = requests.get(query)
r = r.json()
results = r['message']['items']

for pu in results:
    print(pu['DOI'])