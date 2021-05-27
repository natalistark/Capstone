import os
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from models import db, setup_db, Artist, Episode, Podcast
from auth import AuthError, requires_auth
import sys
from config import DevelopmentConfig
from flask.ext.sqlalchemy import SQLAlchemy



def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  #initializing db
  setup_db(app, 'postgresql://student:qwerty@localhost:5432/capstone')
  CORS(app)
  app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://student:qwerty@localhost:5432/capstone'
  app.config['SECRET_KEY'] = DevelopmentConfig.SECRET_KEY
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = DevelopmentConfig.SQLALCHEMY_TRACK_MODIFICATIONS

  return app

APP = create_app()

@APP.route('/artists', methods=['GET'])
@requires_auth('get:artists')
def artists():
    try:
        artists_list = []
        artists_all = Artist.query.order_by(Artist.title).all()
        # if no artists are found, then abort with not found error
        if artists_all is None:
            print("no artists found, have to abort with an error")
            abort(404)
        for art in artists_all:
            artists_list.append(art.artist_json())
        print(jsonify({'success':True, 'artists': artists_list}))
        # if no artistis are added to artists_list, then abort with not found error
        if artists_list is None:
            print("no artists found, have to abort with an error")
            abort(404)
        return jsonify({'success':True, 'artists': artists_list})
    except Exception as error:
        print("was not able to return a list of artists, have to abort with an error")
        print(error)
        print(sys.exc_info())
        abort(422)
        return jsonify({'success': False, 'error_description': 'error, failed with artists'})


@APP.route('/podcasts', methods=['GET'])
@requires_auth('get:podcasts')
def podcasts(jwt):
    try:
        podcasts_list = []
        podcasts_all = Podcast.query.order_by(Podcast.title).all()
        # if no podcasts are found, then abort with not found error
        if podcasts_all is None:
            abort(404)
        for pod in podcasts_all:
            podcasts_list.append(pod.podcast_json())
        # if no podcasts are added, then abort with not found error
        if podcasts_list is None:
            abort(404)
        return jsonify({'success':True, 'podcasts': podcasts_list})
    except Exception as error:
        print(error)
        print(sys.exc_info())
        raise AuthError({'code':'authorization denied', 'description':'authorization denied'}, 401)
        return jsonify({'success': False, 'error_description': print(error)})

@APP.route('/artists', methods=['POST'])
@requires_auth('post:artists')
def create_artist(jwt):
    try:
        print(request.get_json())
        name = request.get_json()['name']
        city = request.get_json()['city']
        country = request.get_json()['country']
        image_link = request.get_json()['image_link']
        artist_to_create = Artist(name, city, country, image_link)
        # if failed to create instance of artist, then abort with 422 error
        if artist_to_create is None: 
            abort(403)
        artist_created = artist_to_create.insert()
        # if failed to create dict of artist, then abort with 422 error
        if len(artist_created.artist_json()) == 0:
            abort(403) 
        return jsonify({'success':True, 'artists':artist_created.artist_json(),'artist_id':artist_created.id})
    except Exception as error:
        print(error)
        print(sys.exc_info())
        raise AuthError({'code':'authorization denied', 'description':'authorization denied'}, 403)
        return jsonify({'success': False, 'error_description': print(error)})

@APP.route('/podcasts', methods=['POST'])
@requires_auth('post:podcasts')
def create_podcast(jwt):
    try:
        print(request.get_json())
        name = request.get_json()['name']
        city = request.get_json()['city']
        country = request.get_json()['country']
        image_link = request.get_json()['image_link']
        genre = request.get_json()['genre']
        podcast_to_create = Podcast(name, city, country, image_link, genre)
        # if failed to create instance of podcast, then abort with 422 error
        if podcast_to_create is None: 
            abort(403)
        podcast_to_create.insert()
        # if failed to create  dict of podcast, then abort with 422 error
        if podcast_to_create.podcast_json is None:
            abort(403) 
        return jsonify({'success':True, 'podcasts':podcast_to_create.podcast_json()})
    except Exception as error:
        print(error)
        print(sys.exc_info())
        raise AuthError({'code':'authorization denied', 'description':'authorization denied'}, 403)
        return jsonify({'success': False, 'error_description': print(error)})

@APP.route('/artists/<int:id>', methods=['PATCH'])
@requires_auth('patch:artists')
def patch_artist(jwt, id):
    try:
        artist_to_patch = Artist.query.filter(Artist.id==id).first()
        # if no artists are found, then abort with not found error
        if artist_to_patch is None:
            abort(404)
        artist_to_patch.name = request.get_json().get('name')
        artist_to_patch.city = request.get_json().get('city')
        artist_to_patch.county = request.get_json().get('country')
        artist_to_patch.image_link = request.get_json().get('image_link')

        artist_to_patch.update()
        return jsonify({'success':True, 'artist_patched':artist_to_patch.artist_json})
    except Exception as error:
        print(error)
        print(sys.exc_info())
        raise AuthError({'code':'authorization denied', 'description':'authorization denied'}, 403)
        return jsonify({'success': False, 'error_description': print(error)})

@APP.route('/artists/<int:id>', methods=['DELETE'])
@requires_auth('delete:artists')
def delete_artist(jwt, id):
    try:
        artist_to_delete = Artist.query.filter(Artist.id==id).first()
        id_to_delete = artist_to_delete.id
        # if no artists are found, then abort with not found error
        if artist_to_delete is None:
            abort(404)
        artist_to_delete.delete()
        return jsonify({'success':True, 'artist_deleted':id_to_delete})
    except Exception as error:
        print(error)
        print(sys.exc_info())
        raise AuthError({'code':'authorization denied', 'description':'authorization denied'}, 403)
        return jsonify({'success': False, 'error_description': print(error)})

# Error Handling

@APP.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "Unprocessable"
    }), 422

@APP.errorhandler(404)
def not_found_error(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "Not found"
    }), 404

@APP.errorhandler(400)
def bad_request_error(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "Bad request"
    }), 400

@APP.errorhandler(403)
def bad_request_error(error):
    return jsonify({
        "success": False,
        "error": 403,
        "message": "Forbidden"
    }), 403

@APP.errorhandler(AuthError)
def auth_error(AuthError):
    return jsonify({
        "success": False,
        "error": AuthError.status_code,
        "message": AuthError.error["description"]
    }), AuthError.status_code

# Launch

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
