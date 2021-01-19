import orcid


api = orcid.PublicAPI(institution_key, institution_secret, sandbox=True)
search_results = api.search_public('text:English')
# Get the summary
token = api.get_token(user_id, user_password, redirect_uri)
summary = api.read_record_public('0000-0001-1111-1111', 'activities',
                                 token)
summary = api.read_record_public('0000-0001-1111-1111', 'record',
                                 token)

