import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Artist, Podcast, Episode
from config import DevConfig, DevelopmentConfig

SUCCESS_STATUS_CODE = 200
NOT_FOUND_ERROR_CODE = 404
NOT_ALLOWED_ERROR_CODE = 405
NOR_PROCESSABLE_ERROR_CODE = 422
CATEGORY_ID = '1'

class CapstoneTestCase(unittest.TestCase):
    """This class represents the capstone test case"""
    artist_id = ''
    artist_id_2 = ''

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        
        setup_db(self.app, os.environ.get('DATABASE_URL'))      

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_artist = {
        'name': 'Zelda',
        'city': 'London',
        'country': 'UK',
        'image_link': 'https://homepages.cae.wisc.edu/~ece533/images/zelda.png'
        }

        self.new_podcast = {
        'name': 'Test podcast',
        'city': 'London',
        'country': 'UK',
        'image_link': 'https://homepages.cae.wisc.edu/~ece533/images/tulips.png'
        },
        'genre': 'Talk show'
        }

        self.new_podcast = {
        "searchTerm":"taj"
        }
    
    def tearDown(self):
        """Executed after reach test"""
        with self.app.app_context():
          self.db.drop_all()
        pass

    #test all artists
    def test_get_artists(self):
        result = self.client().get(
            '/artists',
            headers={"Authorization": "Bearer " + DevelopmentConfig.CONTENT_CREATOR_TOKEN}
        )
        data = json.loads(result.data)
        result = self.client().get('/artists')
        test_data = json.loads(result.data)
        self.assertEqual(result.status_code, SUCCESS_STATUS_CODE)
        self.assertEqual(test_data['success'], True)
        self.assertTrue(len(test_data['artists']))
    
    def test_404_error_get_artists(self):
        result = self.client().get(
            '/artists/9000',
            headers={"Authorization": "Bearer " + DevelopmentConfig.CONTENT_CREATOR_TOKEN}
        )        
        test_data = json.loads(result.data)
        self.assertEqual(result.status_code, NOT_FOUND_ERROR_CODE)
        self.assertEqual(test_data['success'], False)
        self.assertEqual(test_data['message'], 'Not found')

    #test all podcasts
    def test_get_podcasts(self):
        result = self.client().get('/podcasts')
        result = self.client().get(
            '/podcasts',
            headers={"Authorization": "Bearer " + DevelopmentConfig.CONTENT_CREATOR_TOKEN}
        )
        test_data = json.loads(result.data)
        self.assertEqual(result.status_code, SUCCESS_STATUS_CODE)
        self.assertEqual(test_data['success'], True)
        self.assertTrue(len(test_data['questions']))
        self.assertTrue(len(test_data['podcasts']))
    
    def test_404_error_get_podcasts(self):
        result = self.client().get(
            '/podcasts/9000',
            headers={"Authorization": "Bearer " + DevelopmentConfig.CONTENT_CREATOR_TOKEN}
        )
        test_data = json.loads(result.data)
        self.assertEqual(result.status_code, NOT_FOUND_ERROR_CODE)
        self.assertEqual(test_data['success'], False)
        self.assertEqual(test_data['message'], 'Not found')
    
    #test creating an artist
    def test_a_post_artist_by_podcast_supervisor(self):
        result = self.client().post(
            '/artists',
            json=self.new_artist,
            headers={"Authorization": "Bearer " + DevelopmentConfig.PODCAST_SUPERVISOR_TOKEN}
        )
        test_data = json.loads(result.data)
        self.assertEqual(result.status_code, SUCCESS_STATUS_CODE)
        self.assertEqual(test_data['success'], True)
        self.assertTrue(test_data['artists'])

        if (test_data['artist_id']):
            self.__class__.artist_id = str(test_data['artist_id'])
    
    def test_a_post_artist_by_content_creator(self):
        result = self.client().post(
            '/artists',
            json=self.new_artist,
            headers={"Authorization": "Bearer " + DevelopmentConfig.CONTENT_CREATOR_TOKEN}
        )
        test_data = json.loads(result.data)
        self.assertEqual(result.status_code, SUCCESS_STATUS_CODE)
        self.assertEqual(test_data['success'], True)
        self.assertTrue(test_data['artists'])

        if (test_data['artist_id']):
            self.__class__.artist_id_2 = str(test_data['artist_id'])
      
    def test_422_error_creating_artist(self):
        result = self.client().post(
            '/artists',
            headers={"Authorization": "Bearer " + DevelopmentConfig.CONTENT_CREATOR_TOKEN}
        )
        test_data = json.loads(result.data)
        self.assertEqual(result.status_code, NOR_PROCESSABLE_ERROR_CODE)
        self.assertEqual(test_data['success'], False)
        self.assertEqual(test_data['message'], 'The entity is unprocessable')

  #test patching artists
    def test_patch_artist(self):
        result = self.client().patch(
            '/artists/' +  self.__class__.artist_id,
            json={'name':'new name'},
            headers={"Authorization": "Bearer " + DevelopmentConfig.PODCAST_SUPERVISOR_TOKEN}
        )
        test_data = json.loads(result.data)
        self.assertEqual(result.status_code, SUCCESS_STATUS_CODE)
        self.assertEqual(test_data['success'], True)
        self.assertTrue(test_data['artist_patched'])
    
    def test_422_error_patching_artist(self):
        result = self.client().patch(
            '/artists/' +  self.__class__.artist_id,
            headers={"Authorization": "Bearer " + DevelopmentConfig.PODCAST_SUPERVISOR_TOKEN}
        )
        test_data = json.loads(result.data)
        self.assertEqual(result.status_code, NOR_PROCESSABLE_ERROR_CODE)
        self.assertEqual(test_data['success'], False)
        self.assertEqual(test_data['message'], 'The entity is unprocessable')

    #test deleting artists
    def test_delete_the_artist_by_content_creator(self):
        result = self.client().delete('/artists/' +  self.__class__.artist_id)
        result = self.client().get(
            '/artists',
            headers={"Authorization": "Bearer " + DevelopmentConfig.CONTENT_CREATOR_TOKEN}
        )
        test_data = json.loads(result.data)
        self.assertEqual(result.status_code, SUCCESS_STATUS_CODE)
        self.assertEqual(test_data['success'], True)
        self.assertTrue(test_data['artist_deleted'])
        del_art = Artist.query.filter(Artist.id ==  self.__class__.artist_id).first()
        self.assertEqual(del_art, None)
    
    def test_422_error_deleting_artist(self):
        result = self.client().delete('/artist/9000')
        test_data = json.loads(result.data)
        self.assertEqual(result.status_code, NOR_PROCESSABLE_ERROR_CODE)
        self.assertEqual(test_data['success'], False)
        self.assertEqual(test_data['message'], 'The entity is unprocessable')

    def test_403_error_deleting_artist_by_podcast_supervisor(self):
        result = self.client().delete(
            '/artists', headers={"Authorization": "Bearer " + os.environ.get('PODCAST_SUPERVISOR_TOKEN')}
        )
        test_data = json.loads(result.data)
        self.assertEqual(result.status_code, SUCCESS_STATUS_CODE)
        self.assertEqual(test_data['success'], True)
        self.assertTrue(test_data['artist_deleted'])
        del_art = Artist.query.filter(Artist.id ==  self.__class__.artist_id).first()
        self.assertEqual(del_art, None)

    
# Make the tests executable
if __name__ == "__main__":
    unittest.main()
