#!/bin/bash
export DATABASE_URL='postgresql://postgres@localhost:5432/capstone'
export AUTH0_DOMAIN='dev21.eu.auth0.com'
export ALGORITHMS=['RS256']
export API_AUDIENCE='capstone'

#tokens 
export CONTENT_CREATOR_TOKEN='token_value_1'
export PODCAST_SUPERVISOR_TOKEN='token_value_2'
