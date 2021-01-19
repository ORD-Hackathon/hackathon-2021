from scholarly import scholarly

def get_publications_from_researcher(name):
    """From name of researhcer, returns list of publications (Doi?, Titles? TBD!!) of the first authorname matching"""
    
    list_of_publications =[]

    gen = scholarly.search_author(name)
   
    author = next(gen) ## let's just keep first match to avoid duplicates.
    
    author = scholarly.fill(author)
    #print (author['scholar_id'], author['name'], author['email_domain'])
    try:
        for pub in author['publications']:
            list_of_publications += pub['bib']['title']
            # pub['author_pub_id'] Or the DOI instead ???
    except:
        print("no publications found")

    return list_of_publications

# # Retrieve the author's data, fill-in, and print
# search_query = scholarly.search_author('Steven A Cholewiak')
# author = scholarly.fill(next(search_query))
# print(author)
#
# # Print the titles of the author's publications
# print([pub['bib']['title'] for pub in author['publications']])
#
# # Take a closer look at the first publication
# pub = scholarly.fill(author['publications'][0])
# print(pub)
#
# # Which papers cited that publication?
# print([citation['bib']['title'] for citation in scholarly.citedby(pub)])