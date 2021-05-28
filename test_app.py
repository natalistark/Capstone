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
CATEGORY_ID = '1'
DATABASE_URL = 'postgresql://student:qwerty@localhost:5432/capstone'
#tokens 
CONTENT_CREATOR_TOKEN_TEST='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjIxTHF5WXZZdFdGOFJEaERWYnQ5MCJ9.eyJpc3MiOiJodHRwczovL2RldjIxLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGFmZDJhNjg3ODAxYjAwNjgyYmQwNjQiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTYyMjIwMjIwNSwiZXhwIjoxNjIyMjg4NjA1LCJhenAiOiJHT0dTUm9SQXpVdERKTnVQWUl0UUU2YkNFdXdYbEt6dyIsImd0eSI6InBhc3N3b3JkIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFydGlzdHMiLCJnZXQ6cG9kY2FzdHMiLCJwb3N0OmFydGlzdHMiLCJwb3N0OnBvZGNhc3RzIl19.Gz38pSqRYwd-AS4dtSb0vHeLuVFr3tJthEy4D3o_EM41Zp5zVWjkkEdWJlQt5OjnnbT7dP-iO_InojF6RtTfaUTCjD5Vz0tTf-Tpo8x9HjazjMIHkPzh8qUBtU5uBfSOP_njCVZKnUCNVLmmF4gJQytp3t5IXnXCx9jXzM9B_NsIPOiamerx8GfIfEUTA6CmBwaaXdwKenJ5UbNn6MjiRoav2WuPK_64rMkFFeqvwCXntarHSllJF0yaqB984SfBViCm9v8gRR_vr0fGONDsJbCoPo5Ecus7_XhKIxEHI7TTENjHA50QApU8URVr7jawTfjKbROdZYTDuhSQjB5szg'
PODCAST_SUPERVISOR_TOKEN_TEST='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjIxTHF5WXZZdFdGOFJEaERWYnQ5MCJ9.eyJpc3MiOiJodHRwczovL2RldjIxLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGFmZDJkYmQxYzc1MzAwNzA4ZGNjN2IiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTYyMjIwMjQ1MiwiZXhwIjoxNjIyMjg4ODUyLCJhenAiOiJHT0dTUm9SQXpVdERKTnVQWUl0UUU2YkNFdXdYbEt6dyIsImd0eSI6InBhc3N3b3JkIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFydGlzdHMiLCJnZXQ6YXJ0aXN0cyIsImdldDpwb2RjYXN0cyIsInBhdGNoOmFydGlzdHMiLCJwb3N0OmFydGlzdHMiLCJwb3N0OnBvZGNhc3RzIl19.iacehLPMg4GlWW78nURrvMHkLLePWH0LIzJhe00iGYjCBkYenkO9jM1DNCE1G4llRSrYsrOF35lMfYNuA4q2SnS3t2i4hf3QGOnh5Aaxkst0w0XyeB8I1f5YDOjsal9eaLzfCgmX8zro2JMxCsdqpYRo40DcwhxB4QP2tu_ju3siuRcW16x6QW3bQXCjJQFe1jswrdUZuiHNgR6CfRwaitkQhXB6-12oQG7fmYG53CgkxHdZ0pNMbdyTPnn3phQaoY-kI-pxTYnaiEeKEBxryNHkcmVnRW31j8LVkTI889ZS_sEnjfP0M6QWMHL5bf1ERPYmHtwhXa4vwYGEmiRv_g'


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
        print('sucessfully created new artist 555555554')
        print(test_data['artist_id'])
        if (test_data['artist_id']):
            self.__class__.artist_id_2 = str(test_data['artist_id'])
     
    #test deleting artists
    def test_w_delete_the_artist_by_content_creator_error(self):
        result = self.client().delete(
            '/artists/'+  self.__class__.artist_id_2,
            headers=self.headers_con)
        print(self.__class__.artist_id_2)
        print('insidedelart')
        test_data = json.loads(result.data)
        self.assertEqual(result.status_code, NOT_ALLOWED_ERROR_CODE)
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
            '/artists/' + self.__class__.artist_id_2, headers=self.headers_sup)
        test_data = json.loads(result.data)
        self.assertEqual(result.status_code, SUCCESS_STATUS_CODE)
        self.assertEqual(test_data['success'], True)
        self.assertTrue(test_data['artist_id'])
        del_art = Artist.query.filter(Artist.id ==  self.__class__.artist_id_2).first()
        self.assertEqual(del_art, None)


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
    def test_patch_artist(self):
        result = self.client().patch(
            f'/artists/' +  self.__class__.artist_id,
            json={'name':'new name', 'city':'Salt Lake City', 'country':'USA', 'image_link': 'test_image_link'},
            headers=self.headers_con
        )
        test_data = json.loads(result.data)
        self.assertEqual(result.status_code, SUCCESS_STATUS_CODE)
        self.assertEqual(test_data['success'], True)
        self.assertTrue(test_data['artist_id'])
    
    def test_patching_artist_error(self):
        result = self.client().patch(
            '/artists/' +  self.__class__.artist_id, json=self.bad_artist,
            headers=self.headers_con
        )
        test_data = json.loads(result.data)
        self.assertEqual(result.status_code, NOR_PROCESSABLE_ERROR_CODE)
        self.assertEqual(test_data['success'], False)
        self.assertEqual(test_data['message'], 'The entity is unprocessable')   
    
# Make the tests executable
if __name__ == "__main__":
    unittest.main()
