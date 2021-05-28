import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Artist, Podcast, Episode
from config import DevelopmentConfig
import os

SUCCESS_STATUS_CODE = 200
NOT_FOUND_ERROR_CODE = 404
NOT_ALLOWED_ERROR_CODE = 405
NOR_PROCESSABLE_ERROR_CODE = 422
UNAUTHORIZED_ERROR_CODE = 401
FORBIDDEN_ERROR_CODE = 403
CATEGORY_ID = '1'
DATABASE_URL = 'postgresql://student:qwerty@localhost:5432/capstone'
#tokens 
CONTENT_CREATOR_TOKEN_TEST='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjIxTHF5WXZZdFdGOFJEaERWYnQ5MCJ9.eyJpc3MiOiJodHRwczovL2RldjIxLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGFmZDJhNjg3ODAxYjAwNjgyYmQwNjQiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTYyMjIzNDYwMCwiZXhwIjoxNjIyMzIxMDAwLCJhenAiOiJHT0dTUm9SQXpVdERKTnVQWUl0UUU2YkNFdXdYbEt6dyIsImd0eSI6InBhc3N3b3JkIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFydGlzdHMiLCJnZXQ6cG9kY2FzdHMiLCJwb3N0OmFydGlzdHMiLCJwb3N0OnBvZGNhc3RzIl19.nkH_X4Dr_UxPZz9Jw4mMhDbUEnKESfqAfVkq82DwK8yJcPb4rPM_k52c2x9Rt7XrWRsfhmZTM7A7OcatjoBmscJb6xuBntATG8noZxLuMZ2bL_fhExrjjzJ_SaN8yJWA9CJQ-FMIYlzDrfHzLmuhyd7mmBLhvPbyjy1X-QVcccnEbnlXOhpPCq1Uiv-5BLnK1_dhl6EUOIQwpQxbX1DzE8brSz3HAsG0f4YHRqnye5RCmbyVkeAKvFgd-f26n9KEmXzEPe06P7lRmcRlv8UZfbQqtdy2NbmARdJTguQc-L_z7_Jm5yQPiVyc1Mdaf0To651jC0ScIsKrcDXdLMV8fQ'
PODCAST_SUPERVISOR_TOKEN_TEST='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjIxTHF5WXZZdFdGOFJEaERWYnQ5MCJ9.eyJpc3MiOiJodHRwczovL2RldjIxLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGFmZDJkYmQxYzc1MzAwNzA4ZGNjN2IiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTYyMjIzNDYyNiwiZXhwIjoxNjIyMzIxMDI2LCJhenAiOiJHT0dTUm9SQXpVdERKTnVQWUl0UUU2YkNFdXdYbEt6dyIsImd0eSI6InBhc3N3b3JkIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFydGlzdHMiLCJkZWxldGU6cG9kY2FzdHMiLCJnZXQ6YXJ0aXN0cyIsImdldDpwb2RjYXN0cyIsInBhdGNoOmFydGlzdHMiLCJwb3N0OmFydGlzdHMiLCJwb3N0OnBvZGNhc3RzIl19.k2dN4e2GB-eQJWiFSp4zFVwf8wnqAKgFLiqKCi_cgjPKwuHg09tp88Rh4X4s_Hv5ziRNrg-NkLabo3aLDQ3JKxciEbIMal0d9tqiljXg7M_7siCOOMxSiY7tZDblBZMZf7XLuu3jMTXWTNbSGmmdT0A8ZNDSI6UxLPHvHRyuyDes2PK1VWXhx0Uesx18UKVFBRMMDutRq209RtXYptvXWhQcaA5-ebi14e5gl05uPyGO9NooNQF5cFn9XIbcoFjDomN-KMTpJGAG1cE-gxWiLZlfqsjGjChQBR8e3E_6tgMmOn5OmX8H2MWcUri8mYKb4qR5Z1jGrulWKh0ktQk80w'


class CapstoneTestCase(unittest.TestCase):
    """This class represents the capstone test case"""
    artist_id = ''
    artist_id_2 = ''

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        
        setup_db(self.app, DATABASE_URL)      

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_artist = {
        'name': 'Zelda',
        'city': 'Rome',
        'country': 'Italy',
        'image_link': 'https://homepages.cae.wisc.edu/~ece533/images/zelda.png'
        }

        self.bad_artist = {
        'name': '',
        'city': 'Rome',
        'country': 'Italy',
        'image_link': 'https://homepages.cae.wisc.edu/~ece533/images/zelda.png'
        }
        
        self.new_podcast = {
        'name': 'Test podcast',
        'city': 'London',
        'country': 'UK',
        'image_link': 'https://homepages.cae.wisc.edu/~ece533/images/tulips.png',
        'genre': 'Talk show'
        }

        self.new_podcast = {
        "searchTerm":"taj"
        }
        
        self.headers_con={'Authorization':'Bearer ' + CONTENT_CREATOR_TOKEN_TEST}
        self.headers_sup={'Authorization':'Bearer ' + PODCAST_SUPERVISOR_TOKEN_TEST}
    
    def tearDown(self):
        """Executed after reach test"""
        with self.app.app_context():
          self.db.drop_all()
        pass

    def test_a_post_artist_by_content_creator(self):
        result = self.client().post(
            '/artists',
            json=self.new_artist,
            headers=self.headers_con
        )
        test_data = json.loads(result.data)
        self.assertEqual(result.status_code, SUCCESS_STATUS_CODE)
        self.assertEqual(test_data['success'], True)
        self.assertTrue(test_data['artist_id'])
        if (test_data['artist_id']):
            self.__class__.artist_id_2 = str(test_data['artist_id'])
     
    #test deleting artists
    def test_w_delete_the_artist_by_content_creator_error(self):
        result = self.client().delete(
            '/artists/'+  self.__class__.artist_id_2,
            headers=self.headers_con)
        test_data = json.loads(result.data)
        self.assertEqual(result.status_code, FORBIDDEN_ERROR_CODE)
        self.assertEqual(test_data['success'], False)
    
    #test all artists
    def test_get_artists(self):
        result = self.client().get(
            '/artists',
            headers=self.headers_con
        )
        test_data = json.loads(result.data)
        self.assertEqual(result.status_code, SUCCESS_STATUS_CODE)
        self.assertEqual(test_data['success'], True)
    
    def test_401_error_get_artists(self):
        result = self.client().get(
            '/artists')   
        test_data = json.loads(result.data)
        self.assertEqual(result.status_code, UNAUTHORIZED_ERROR_CODE)
        self.assertEqual(test_data['success'], False)
        self.assertEqual(test_data['message'], 'Unauthorized')

    #test all podcasts
    def test_get_podcasts(self):
        result = self.client().get(
            '/podcasts',
            headers=self.headers_con
        )
        test_data = json.loads(result.data)
        self.assertEqual(result.status_code, SUCCESS_STATUS_CODE)
        self.assertEqual(test_data['success'], True)
    
    def test_404_error_get_podcasts(self):
        result = self.client().get(
            '/podcasts/9000',
            headers=self.headers_con
        )
        test_data = json.loads(result.data)
        self.assertEqual(result.status_code, NOT_FOUND_ERROR_CODE)
        self.assertEqual(test_data['success'], False)
        self.assertEqual(test_data['message'], 'Not found')

    #test creating an artist
    def test_422_error_deleting_artist(self):
        result = self.client().delete('/artists/9000', headers=self.headers_sup)
        test_data = json.loads(result.data)
        self.assertEqual(result.status_code, NOR_PROCESSABLE_ERROR_CODE)
        self.assertEqual(test_data['success'], False)
        self.assertEqual(test_data['message'], 'The entity is unprocessable')


    def test_w_delete_the_artist_by_podcast_supervisor(self):
        result = self.client().delete(
            '/artists/'+  self.__class__.artist_id,
            headers=self.headers_sup)
        test_data = json.loads(result.data)
        self.assertEqual(result.status_code, SUCCESS_STATUS_CODE)
        self.assertEqual(test_data['success'], True)


    def test_a_post_artist_by_podcast_supervisor(self):
        result = self.client().post(
            '/artists',
            json=self.new_artist,
            headers=self.headers_sup
        )
        test_data = json.loads(result.data)
        self.assertEqual(result.status_code, SUCCESS_STATUS_CODE)
        self.assertEqual(test_data['success'], True)
        self.assertTrue(test_data['artist_id'])

        if (test_data['artist_id']):
            self.__class__.artist_id = str(test_data['artist_id'])

    def test_422_error_creating_artist(self):
        result = self.client().post(
            '/artists', json=self.bad_artist,
            headers=self.headers_con
        )
        test_data = json.loads(result.data)
        self.assertEqual(result.status_code, NOR_PROCESSABLE_ERROR_CODE)
        self.assertEqual(test_data['success'], False)
        self.assertEqual(test_data['message'], 'The entity is unprocessable')

  #test patching artists
    def test_patch_artist_podcast_superviser(self):
        result = self.client().patch(
            f'/artists/' +  self.__class__.artist_id,
            json={'name':'new name', 'city':'Salt Lake City', 'country':'USA', 'image_link': 'test_image_link'},
            headers=self.headers_sup
        )
        test_data = json.loads(result.data)
        self.assertEqual(result.status_code, SUCCESS_STATUS_CODE)
        self.assertEqual(test_data['success'], True)
        self.assertTrue(test_data['artist_id'])
    
    def test_patching_artist_error_bad_patch(self):
        result = self.client().patch(
            '/artists/' +  self.__class__.artist_id, json=self.bad_artist,
            headers=self.headers_sup
        )
        test_data = json.loads(result.data)
        self.assertEqual(result.status_code, NOR_PROCESSABLE_ERROR_CODE)
        self.assertEqual(test_data['success'], False)
        self.assertEqual(test_data['message'], 'The entity is unprocessable') 

    def test_patching_artist_error_content_creator(self):
        result = self.client().patch(
            '/artists/' +  self.__class__.artist_id, json=self.bad_artist,
            headers=self.headers_con
        )
        test_data = json.loads(result.data)
        self.assertEqual(result.status_code, FORBIDDEN_ERROR_CODE)
        self.assertEqual(test_data['success'], False)
        self.assertEqual(test_data['message'], 'permission role is missing')   
    
# Make the tests executable
if __name__ == "__main__":
    unittest.main()
