import dblp

authors = dblp.search('noam chomsky')
# authors = dblp.searchORCID("0000-0001-7580-4351")

for au in authors:
    print (au.name)
    print (len(au.publications))
    for pu in au.publications:
        print(pu.title, pu.year, pu.ee) # ee: electornic edition

