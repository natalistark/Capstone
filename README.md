# Full Stack Podcast Tracker App API Backend

## About
The Podcast Tracker App is the app that shows podcasts, their episodes and artists that create these podcasts. 
Content creator and podcast superviser have rights to CRUD operations. They can send POST request to create a podcast stating name of the podcast, city and country where it was recorded, link to the image assosiated with podcast, and genre with which best can be described the podcast. To the podcasts are connected episodes of podcast with on one to many relationship(regarding relative databases), meaning one episode belongs to one podcast but podcast has many episodes. With sending POST request content creator and podcast superviser can also create Artist that took part in creating an episode stating his name, city, country, their photo or image. There is one to many relationship between artist and episodes, one artist has many episodes and episode can have one main artist. Episode contains its name, release date and podcast id and artist id.

The rights of content creator and podcast superviser differ and are described in USER ROLES section of this README.

All the description of Endpoints are included in section of this Readme that is called "Endpoint Library"

As frontend is still under development all the endpoints have to be checked programmatically that is using terminal and curl or use a standalone website such as Postman
## Getting Started

### Installing Dependencies

#### Python 3.6.9 or later

Installation of Python 3.6.9 or later is needed. Please install it using the official documentation of Python such as this
https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python

#### PIP Dependencies

Please use terminal and cd into directory of the Podcast project and with the help of pip install install all the requirements from requirements.txt

```
pip install -r requirements.txt
```

With pip install all necessary dependencies are installed.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a easy to use backend Python framework.

- [SQLAlchemy](https://www.sqlalchemy.org/) is Python frameworks dedicated to managing databases.


## Running the server

In order to run the app you have to use terminal and type the following:
```
FLASK_APP=app.py FLASK_DEBUG=TRUE flask run
```
Live version of the app is hosted on Heroku. Unfortunately frontend is under development and all endpoints have to checked and tested via curl or third party websites such as postman.co
https://capstonedev211.herokuapp.com/

## DATA MODELING:
#### models.py
- The model of the app is saved in models.py. There are 3 tables artists, podcasts and episodes. 
- Artist consists of id, name, city, country, image_link.
- Artist's id is a foreign key in Episode table
- Episode table constist of two foreign key artist's key and podcast's key. Episode holds id, name, and release date
- Podcast consists of id, name, city, country, image_link.
- Podcast consists of multiple episodes, one artist can create an episode.

Every table has helper function to assist with CRUD functionality

## USER ROLES:
- There are two roles
- Content creator can create and view episode, podcasts and artists
- Podcast superviser create and view episode, podcasts and artists. As well podcast superviser
can patch and delete all entries from all tables

## API ARCHITECTURE AND TESTING
### Endpoint Library

In the app I used @app.errorhandler decorators and @requires_auth decorators 

In order to acces all enpoints, you have to use authentication, tokens are provided below

Test user with role content creator
Email: lili@mail.com
Password: fdhdj&&GHdr43SFG@


Token: 
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjIxTHF5WXZZdFdGOFJEaERWYnQ5MCJ9.eyJpc3MiOiJodHRwczovL2RldjIxLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGFmZDJhNjg3ODAxYjAwNjgyYmQwNjQiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTYyMjIzNDYwMCwiZXhwIjoxNjIyMzIxMDAwLCJhenAiOiJHT0dTUm9SQXpVdERKTnVQWUl0UUU2YkNFdXdYbEt6dyIsImd0eSI6InBhc3N3b3JkIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFydGlzdHMiLCJnZXQ6cG9kY2FzdHMiLCJwb3N0OmFydGlzdHMiLCJwb3N0OnBvZGNhc3RzIl19.nkH_X4Dr_UxPZz9Jw4mMhDbUEnKESfqAfVkq82DwK8yJcPb4rPM_k52c2x9Rt7XrWRsfhmZTM7A7OcatjoBmscJb6xuBntATG8noZxLuMZ2bL_fhExrjjzJ_SaN8yJWA9CJQ-FMIYlzDrfHzLmuhyd7mmBLhvPbyjy1X-QVcccnEbnlXOhpPCq1Uiv-5BLnK1_dhl6EUOIQwpQxbX1DzE8brSz3HAsG0f4YHRqnye5RCmbyVkeAKvFgd-f26n9KEmXzEPe06P7lRmcRlv8UZfbQqtdy2NbmARdJTguQc-L_z7_Jm5yQPiVyc1Mdaf0To651jC0ScIsKrcDXdLMV8fQ



Test user with role podcast supervisor
Email: bob@mail.com
Password: fdhdj&&GHdr431SFG@

Token
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjIxTHF5WXZZdFdGOFJEaERWYnQ5MCJ9.eyJpc3MiOiJodHRwczovL2RldjIxLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGFmZDJkYmQxYzc1MzAwNzA4ZGNjN2IiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTYyMjIzNDYyNiwiZXhwIjoxNjIyMzIxMDI2LCJhenAiOiJHT0dTUm9SQXpVdERKTnVQWUl0UUU2YkNFdXdYbEt6dyIsImd0eSI6InBhc3N3b3JkIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFydGlzdHMiLCJkZWxldGU6cG9kY2FzdHMiLCJnZXQ6YXJ0aXN0cyIsImdldDpwb2RjYXN0cyIsInBhdGNoOmFydGlzdHMiLCJwb3N0OmFydGlzdHMiLCJwb3N0OnBvZGNhc3RzIl19.k2dN4e2GB-eQJWiFSp4zFVwf8wnqAKgFLiqKCi_cgjPKwuHg09tp88Rh4X4s_Hv5ziRNrg-NkLabo3aLDQ3JKxciEbIMal0d9tqiljXg7M_7siCOOMxSiY7tZDblBZMZf7XLuu3jMTXWTNbSGmmdT0A8ZNDSI6UxLPHvHRyuyDes2PK1VWXhx0Uesx18UKVFBRMMDutRq209RtXYptvXWhQcaA5-ebi14e5gl05uPyGO9NooNQF5cFn9XIbcoFjDomN-KMTpJGAG1cE-gxWiLZlfqsjGjChQBR8e3E_6tgMmOn5OmX8H2MWcUri8mYKb4qR5Z1jGrulWKh0ktQk80w


If tokens are expired please use curl in terminal in order to issue new token. 

curl --request POST   --url 'https://dev21.eu.auth0.com/oauth/token'   --header 'content-type: application/json'   --data '{"grant_type": "password","username":"lili@mail.com","password": "fdhdj&&GHdr43SFG@","audience": "capstone","scope": "SCOPE","client_id": "GOGSRoRAzUtDJNuPYItQE6bCEuwXlKzw","client_secret": "2GjKaCvf9qfbMKVW9HEoR9EU_-c-3000esDYu50R7FyeaeKLeTO3e5hKjsmGc9Ft"}'

curl --request POST   --url 'https://dev21.eu.auth0.com/oauth/token'   --header 'content-type: application/json'   --data '{"grant_type": "password","username":"bob@mail.com","password": "fdhdj&&GHdr431SFG@","audience": "capstone","scope": "SCOPE","client_id": "GOGSRoRAzUtDJNuPYItQE6bCEuwXlKzw","client_secret": "2GjKaCvf9qfbMKVW9HEoR9EU_-c-3000esDYu50R7FyeaeKLeTO3e5hKjsmGc9Ft"}'

#### GET '/podcasts'
Returns a list of all podcasts 

Example curl: 
curl https://capstonedev211.herokuapp.com/podcasts -X GET -H "Content-Type: application/json" -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjIxTHF5WXZZdFdGOFJEaERWYnQ5MCJ9.eyJpc3MiOiJodHRwczovL2RldjIxLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGFmZDJhNjg3ODAxYjAwNjgyYmQwNjQiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTYyMjE0NDk1MSwiZXhwIjoxNjIyMjMxMzUxLCJhenAiOiJHT0dTUm9SQXpVdERKTnVQWUl0UUU2YkNFdXdYbEt6dyIsImd0eSI6InBhc3N3b3JkIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFydGlzdHMiLCJnZXQ6cG9kY2FzdHMiLCJwb3N0OmFydGlzdHMiLCJwb3N0OnBvZGNhc3RzIl19.loohE4jCaSv6beWsXjIyIz1MWu5h_wCLZDw9BoRM5fpPL5IgmMLvrl2oUL1N_urUxhUWMq_H7gfdaG1xA5mkU2FJ2b9ZSAZ-nx7bS31DAG4O8jPWyTUmeAfVFWJzYzMZz8mqvgUF1GK67lgREcxLGk-DHk14sIjLSd5apVdy5boDSUxBsG9bFpeXhda19_85CvLz17Wf5jmHMrBXflIBUhTsguzQ8ic4cfIBfym3KPBl9mfMhEb7zm7WwaBfdGKI0EjkeCUAhy0y8NOFIasqSi9_rBNSkU89HmD12d7eYnEClEgMyxzL19CmIBqw2cr5gH1kAuFhiKsQoir7YdbRiw"

Example response:
{"podcasts":[{"city":"New York","country":"USA","genre":"Talk Show","id":1,"image_link":"testimagelink","name":"new podcast"}]

#### GET '/artists'
Returns a list of all artists
Takes no arguments

Example curl: 
curl https://capstonedev211.herokuapp.com/artists -X GET -H "Content-Type: application/json" -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjIxTHF5WXZZdFdGOFJEaERWYnQ5MCJ9.eyJpc3MiOiJodHRwczovL2RldjIxLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGFmZDJhNjg3ODAxYjAwNjgyYmQwNjQiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTYyMjE0NDk1MSwiZXhwIjoxNjIyMjMxMzUxLCJhenAiOiJHT0dTUm9SQXpVdERKTnVQWUl0UUU2YkNFdXdYbEt6dyIsImd0eSI6InBhc3N3b3JkIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFydGlzdHMiLCJnZXQ6cG9kY2FzdHMiLCJwb3N0OmFydGlzdHMiLCJwb3N0OnBvZGNhc3RzIl19.loohE4jCaSv6beWsXjIyIz1MWu5h_wCLZDw9BoRM5fpPL5IgmMLvrl2oUL1N_urUxhUWMq_H7gfdaG1xA5mkU2FJ2b9ZSAZ-nx7bS31DAG4O8jPWyTUmeAfVFWJzYzMZz8mqvgUF1GK67lgREcxLGk-DHk14sIjLSd5apVdy5boDSUxBsG9bFpeXhda19_85CvLz17Wf5jmHMrBXflIBUhTsguzQ8ic4cfIBfym3KPBl9mfMhEb7zm7WwaBfdGKI0EjkeCUAhy0y8NOFIasqSi9_rBNSkU89HmD12d7eYnEClEgMyxzL19CmIBqw2cr5gH1kAuFhiKsQoir7YdbRiw"

Example response:
{"artists":[{"city":"Chicago","country":"UK","id":1,"image_link":"https://homepages.cae.wisc.edu/~ece533/images/cat.png","name":"Heidy Red"},{"city":"London","country":"UK","id":2,"image_link":"testimagelink","name":"Lili Allen"},{"city":"Paris","country":"France","id":6,"image_link":"https://homepages.cae.wisc.edu/~ece533/images/cat.png","name":"Nick Green"}],"success":true}

#### POST '/artists'
Creates an artist
Takes arguments: name, city, country, image_link
Returns artist id and success status

Example curl: 
curl https://capstonedev211.herokuapp.com/artists -X POST -H "Content-Type: application/json" -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjIxTHF5WXZZdFdGOFJEaERWYnQ5MCJ9.eyJpc3MiOiJodHRwczovL2RldjIxLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGFmZDJhNjg3ODAxYjAwNjgyYmQwNjQiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTYyMjE0NDk1MSwiZXhwIjoxNjIyMjMxMzUxLCJhenAiOiJHT0dTUm9SQXpVdERKTnVQWUl0UUU2YkNFdXdYbEt6dyIsImd0eSI6InBhc3N3b3JkIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFydGlzdHMiLCJnZXQ6cG9kY2FzdHMiLCJwb3N0OmFydGlzdHMiLCJwb3N0OnBvZGNhc3RzIl19.loohE4jCaSv6beWsXjIyIz1MWu5h_wCLZDw9BoRM5fpPL5IgmMLvrl2oUL1N_urUxhUWMq_H7gfdaG1xA5mkU2FJ2b9ZSAZ-nx7bS31DAG4O8jPWyTUmeAfVFWJzYzMZz8mqvgUF1GK67lgREcxLGk-DHk14sIjLSd5apVdy5boDSUxBsG9bFpeXhda19_85CvLz17Wf5jmHMrBXflIBUhTsguzQ8ic4cfIBfym3KPBl9mfMhEb7zm7WwaBfdGKI0EjkeCUAhy0y8NOFIasqSi9_rBNSkU89HmD12d7eYnEClEgMyxzL19CmIBqw2cr5gH1kAuFhiKsQoir7YdbRiw" -d '{"name":"Nick Green", "city": "Paris", "country": "France", "image_link": "https://homepages.cae.wisc.edu/~ece533/images/cat.png"}'

Example response:
{"artist_id":"1","success":true}


#### POST '/podcasts'
Creates a podcast
Takes arguments: name, city, country, image_link, genre
Returns podcast id and success status 

Example curl: 
curl https://capstonedev211.herokuapp.com/podcasts -X POST -H "Content-Type: application/json" -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjIxTHF5WXZZdFdGOFJEaERWYnQ5MCJ9.eyJpc3MiOiJodHRwczovL2RldjIxLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGFmZDJhNjg3ODAxYjAwNjgyYmQwNjQiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTYyMjE0NDk1MSwiZXhwIjoxNjIyMjMxMzUxLCJhenAiOiJHT0dTUm9SQXpVdERKTnVQWUl0UUU2YkNFdXdYbEt6dyIsImd0eSI6InBhc3N3b3JkIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFydGlzdHMiLCJnZXQ6cG9kY2FzdHMiLCJwb3N0OmFydGlzdHMiLCJwb3N0OnBvZGNhc3RzIl19.loohE4jCaSv6beWsXjIyIz1MWu5h_wCLZDw9BoRM5fpPL5IgmMLvrl2oUL1N_urUxhUWMq_H7gfdaG1xA5mkU2FJ2b9ZSAZ-nx7bS31DAG4O8jPWyTUmeAfVFWJzYzMZz8mqvgUF1GK67lgREcxLGk-DHk14sIjLSd5apVdy5boDSUxBsG9bFpeXhda19_85CvLz17Wf5jmHMrBXflIBUhTsguzQ8ic4cfIBfym3KPBl9mfMhEb7zm7WwaBfdGKI0EjkeCUAhy0y8NOFIasqSi9_rBNSkU89HmD12d7eYnEClEgMyxzL19CmIBqw2cr5gH1kAuFhiKsQoir7YdbRiw" -d '{"name":"Life in Paris", "city": "Paris", "country": "France", "image_link": "https://homepages.cae.wisc.edu/~ece533/images/tulips.png", "genre": "Talk Show"}'

Example response:
{"podcast_id":"2","success":true}


#### PATCH '/artists'
Changes an artist entry
Takes arguments: name, city, country, image_link
Returns artist id and success status

Example curl: 
curl https://capstonedev211.herokuapp.com/artists/1 -X PATCH -H "Content-Type: application/json" -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjIxTHF5WXZZdFdGOFJEaERWYnQ5MCJ9.eyJpc3MiOiJodHRwczovL2RldjIxLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGFmZDJhNjg3ODAxYjAwNjgyYmQwNjQiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTYyMjE0NDk1MSwiZXhwIjoxNjIyMjMxMzUxLCJhenAiOiJHT0dTUm9SQXpVdERKTnVQWUl0UUU2YkNFdXdYbEt6dyIsImd0eSI6InBhc3N3b3JkIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFydGlzdHMiLCJnZXQ6cG9kY2FzdHMiLCJwb3N0OmFydGlzdHMiLCJwb3N0OnBvZGNhc3RzIl19.loohE4jCaSv6beWsXjIyIz1MWu5h_wCLZDw9BoRM5fpPL5IgmMLvrl2oUL1N_urUxhUWMq_H7gfdaG1xA5mkU2FJ2b9ZSAZ-nx7bS31DAG4O8jPWyTUmeAfVFWJzYzMZz8mqvgUF1GK67lgREcxLGk-DHk14sIjLSd5apVdy5boDSUxBsG9bFpeXhda19_85CvLz17Wf5jmHMrBXflIBUhTsguzQ8ic4cfIBfym3KPBl9mfMhEb7zm7WwaBfdGKI0EjkeCUAhy0y8NOFIasqSi9_rBNSkU89HmD12d7eYnEClEgMyxzL19CmIBqw2cr5gH1kAuFhiKsQoir7YdbRiw" -d '{"name":"Heidy Red", "city": "Chicago", "country": "USA", "image_link": "https://homepages.cae.wisc.edu/~ece533/images/cat.png"}'

Example response:
{"artist_id":"1","success":true}

#### DELETE '/artists/<artist_id>'
Deletes an artist entry
Takes no arguments
Returns artist's id that was deleted and success status

Example curl: 
curl https://capstonedev211.herokuapp.com/artists/1 -X DELETE -H "Content-Type: application/json" -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjIxTHF5WXZZdFdGOFJEaERWYnQ5MCJ9.eyJpc3MiOiJodHRwczovL2RldjIxLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGFmZDJhNjg3ODAxYjAwNjgyYmQwNjQiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTYyMjE0NDk1MSwiZXhwIjoxNjIyMjMxMzUxLCJhenAiOiJHT0dTUm9SQXpVdERKTnVQWUl0UUU2YkNFdXdYbEt6dyIsImd0eSI6InBhc3N3b3JkIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFydGlzdHMiLCJnZXQ6cG9kY2FzdHMiLCJwb3N0OmFydGlzdHMiLCJwb3N0OnBvZGNhc3RzIl19.loohE4jCaSv6beWsXjIyIz1MWu5h_wCLZDw9BoRM5fpPL5IgmMLvrl2oUL1N_urUxhUWMq_H7gfdaG1xA5mkU2FJ2b9ZSAZ-nx7bS31DAG4O8jPWyTUmeAfVFWJzYzMZz8mqvgUF1GK67lgREcxLGk-DHk14sIjLSd5apVdy5boDSUxBsG9bFpeXhda19_85CvLz17Wf5jmHMrBXflIBUhTsguzQ8ic4cfIBfym3KPBl9mfMhEb7zm7WwaBfdGKI0EjkeCUAhy0y8NOFIasqSi9_rBNSkU89HmD12d7eYnEClEgMyxzL19CmIBqw2cr5gH1kAuFhiKsQoir7YdbRiw" 

Example response:
{"artist_id":1,"success":true}

## Testing
13 unittests in test_app.py cover all app's endpoints. To launch unittests, please type the following in terminal
```
python -m unittest test_app.py
```

## THIRD-PARTY AUTHENTICATION
#### auth.py
Authentication is provided by third-party service auth0.com
The JWT token is given by auth0 and gives authorization for content creator and podcast supervisor according to their roles.

## DEPLOYMENT
Podcast app is deployed on Heroku
https://capstonedev211.herokuapp.com
No frontend is available, so curl is needed to test all the endpoints


