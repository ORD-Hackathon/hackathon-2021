from scholarly import scholarly

gen = scholarly.search_author('Steven A. Cholewiak')
for au in gen:
    au = scholarly.fill(au)
    print (au['scholar_id'], au['name'], au['email_domain'])
    try:
        for pub in au['publications']:
            print(pub['author_pub_id'], pub['bib']['title'])
    except:
        print("no publications found")
    print()

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