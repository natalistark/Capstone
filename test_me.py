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
CATEGORY_ID = '1'
DATABASE_URL = 'postgresql://student:qwerty@localhost:5432/capstone'
#tokens 
CONTENT_CREATOR_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjIxTHF5WXZZdFdGOFJEaERWYnQ5MCJ9.eyJpc3MiOiJodHRwczovL2RldjIxLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGFmZDJhNjg3ODAxYjAwNjgyYmQwNjQiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTYyMjE0NDk1MSwiZXhwIjoxNjIyMjMxMzUxLCJhenAiOiJHT0dTUm9SQXpVdERKTnVQWUl0UUU2YkNFdXdYbEt6dyIsImd0eSI6InBhc3N3b3JkIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFydGlzdHMiLCJnZXQ6cG9kY2FzdHMiLCJwb3N0OmFydGlzdHMiLCJwb3N0OnBvZGNhc3RzIl19.loohE4jCaSv6beWsXjIyIz1MWu5h_wCLZDw9BoRM5fpPL5IgmMLvrl2oUL1N_urUxhUWMq_H7gfdaG1xA5mkU2FJ2b9ZSAZ-nx7bS31DAG4O8jPWyTUmeAfVFWJzYzMZz8mqvgUF1GK67lgREcxLGk-DHk14sIjLSd5apVdy5boDSUxBsG9bFpeXhda19_85CvLz17Wf5jmHMrBXflIBUhTsguzQ8ic4cfIBfym3KPBl9mfMhEb7zm7WwaBfdGKI0EjkeCUAhy0y8NOFIasqSi9_rBNSkU89HmD12d7eYnEClEgMyxzL19CmIBqw2cr5gH1kAuFhiKsQoir7YdbRiw'
PODCAST_SUPERVISOR_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjIxTHF5WXZZdFdGOFJEaERWYnQ5MCJ9.eyJpc3MiOiJodHRwczovL2RldjIxLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGFmZDJkYmQxYzc1MzAwNzA4ZGNjN2IiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTYyMjE0NTE0OCwiZXhwIjoxNjIyMjMxNTQ4LCJhenAiOiJHT0dTUm9SQXpVdERKTnVQWUl0UUU2YkNFdXdYbEt6dyIsImd0eSI6InBhc3N3b3JkIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFydGlzdHMiLCJnZXQ6YXJ0aXN0cyIsImdldDpwb2RjYXN0cyIsInBhdGNoOmFydGlzdHMiLCJwb3N0OmFydGlzdHMiLCJwb3N0OnBvZGNhc3RzIl19.nrPGAhhKKappzJCr2cvOhQCWU3rO88057DFh1YIb9zq2nFmWAElADQWvtVcNQhxeNuLMhl7jMaLFAlcFmCR_lmBzXEehAE1OcQ7cT62Tkr62lIXJcRYqPABe2_y3ZgA8sqDMF3kOAO1oET17l1Lx7__uYrFjNFuoRMWkVb_ylxSKoKdulcov2wFapnokyyzvKnhoc-_mocGhgnXvibtTZYnsYIDj_WICSFxjY14JYOtFIm6csd11E96FeC5l36xS25zLvRngwHHd82faHrwfL-xFK3H4hvycNOr6ERClfTQ0qiTsNs-h25cmAvRJXTvDh3-OSEaab5imrjeeWeItQg'


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
    
    def tearDown(self):
        """Executed after reach test"""
        with self.app.app_context():
          self.db.drop_all()
        pass

    #test all artists
    def test_get_artists(self):
        result = self.client().get(
            '/artists',
            headers={"Authorization": "Bearer " + CONTENT_CREATOR_TOKEN}
        )
        result = self.client().get('/artists')
        test_data = json.loads(result.data)
        self.assertEqual(result.status_code, SUCCESS_STATUS_CODE)
        self.assertEqual(test_data['success'], True)
    
    def test_404_error_get_artists(self):
        result = self.client().get(
            '/artists/9000',
            headers={"Authorization": "Bearer " + CONTENT_CREATOR_TOKEN}
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
            headers={"Authorization": "Bearer " + CONTENT_CREATOR_TOKEN}
        )
        test_data = json.loads(result.data)
        self.assertEqual(result.status_code, SUCCESS_STATUS_CODE)
        self.assertEqual(test_data['success'], True)
        self.assertTrue(len(test_data['questions']))
        self.assertTrue(len(test_data['podcasts']))
    
    def test_404_error_get_podcasts(self):
        result = self.client().get(
            '/podcasts/9000',
            headers={"Authorization": "Bearer " + CONTENT_CREATOR_TOKEN}
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
            headers={"Authorization": "Bearer " + PODCAST_SUPERVISOR_TOKEN}
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
            headers={"Authorization": "Bearer " + CONTENT_CREATOR_TOKEN}
        )
        test_data = json.loads(result.data)
        self.assertEqual(result.status_code, SUCCESS_STATUS_CODE)
        self.assertEqual(test_data['success'], True)
        self.assertTrue(test_data['artists'])

        if (test_data['artist_id']):
            self.__class__.artist_id_2 = str(test_data['artist_id'])
      
    

    
# Make the tests executable
if __name__ == "__main__":
    unittest.main()
