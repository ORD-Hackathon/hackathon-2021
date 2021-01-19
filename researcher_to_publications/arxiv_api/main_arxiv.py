import urllib.request as libreq

author = 'norm'
with libreq.urlopen('http://export.arxiv.org/api/query?search_query=au:' + author) as url:
    r = url.read()
print(r)

# import arxiv
#
# # Keyword queries
# arxiv.query(query="quantum", max_results=100)
#
# # Multi-field queries
# arxiv.query(query="au:balents_leon AND cat:cond-mat.str-el")
#
# # Get single record by ID
# arxiv.query(id_list=["1707.08567"])
#
# # Get multiple records by ID
# arxiv.query(id_list=["1707.08567", "1707.08567"])
#
# # Get an interator over query results
# result = arxiv.query(
#     query="quantum",
#     max_chunk_results=10,
#     max_results=100,
#     iterative=True
# )
#
# for paper in result():
#     print(paper)