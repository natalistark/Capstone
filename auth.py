import json
from flask import Flask, request, jsonify, _request_ctx_stack
from functools import wraps
from jose import jwt
from urllib.request import urlopen
import sys
from config import DevelopmentConfig
import os

AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN')
ALGORITHMS = os.environ.get('ALGORITHMS')
API_AUDIENCE = os.environ.get('API_AUDIENCE')

app = Flask(__name__)

## AuthError Exception
class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

## Errors handling
@app.errorhandler(AuthError)
def auth_error(AuthError):
    return jsonify({
        "success": False,
        "error": AuthError.status_code,
        "message": AuthError.error["description"]
    }), AuthError.status_code

## Auth Header
def get_token_auth_header():
    #if 'Authorization' key is missing from request headers then abort with 403 error
    if 'Authorization' not in request.headers:
        print('No Authorization key')
        print(request.headers)
        raise AuthError({'code':'Authorization key is missing from request headers',
        'description':'Unauthorized'}, 401)

    header = request.headers.get('Authorization', None)
    #if auth header is missing then abort with 403 error
    try:
        header != None
    except Exception as error:
        print(sys.exc_info())
        print(error)
        raise AuthError({'code':'auth header is missing', 'description':'auth header is missing'}, 401)
    header_divided = header.split(' ')
    #if auth header does not consist of 2 parts, then abort with 403 error
    try:
        len(header_divided) == 2
    except Exception as error:
        print(sys.exc_info())
        print(error)
        raise AuthError({'code':'auth header does not consist of 2 parts', 'description':'auth header does not consist of 2 parts'}, 403)
    #if first auth header is not bearer, then abort with 403 error
    try:
        header_divided[0].lower() == 'bearer'
    except Exception as error:
        print(sys.exc_info())
        print(error)
        raise AuthError({'code':'first auth header is not bearer', 'description':'first auth header is not bearer'}, 403)
    token = header_divided[1]
    #if token is missing, then abort with 403 error
    try:
        len(token) > 0
    except Exception as error:
        print(sys.exc_info())
        print(error)
        raise AuthError({'code':'token is missing', 'description':'token is missing'}, 403)
    return token

def check_permissions(permission, payload):
    # if permissions are missing from payload, then abort with 400 error
    try:
        'permissions' in payload
    except Exception as error:
        print(sys.exc_info())
        print(error)
        raise AuthError({'code':'permissions are missing from payload', 'description':'permissions are missing from payload'}, 403)
 
    # if the permission role is missing from permissions payload, 
    # then abort with 403 not found error
    try:
        permission in payload['permissions']
    except Exception as error:
        print(sys.exc_info()) 
        print(error)
        raise AuthError({'code':'permission role is missing', 'description':'permission role is missing'}, 403)

def verify_decode_jwt(token):
    dict_rsa = {}
    payload_decoded = {}
    # get and load public key 
    json_url = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    json_loaded = json.loads(json_url.read())
    # get unvarified header
    header_unver = jwt.get_unverified_header(token)
    try:
        # check if key kid exists in unverified header
        if 'kid' in header_unver:
            for dict in json_loaded['keys']:
                # check if key values are equal, create dictionary with rsa key
                if dict['kid'] == header_unver['kid']:
                    if dict['kty']:
                        dict_rsa['kty'] = dict['kty']
                    if dict['kid']:
                        dict_rsa['kid'] = dict['kid']
                    if dict['use']:
                        dict_rsa['use'] = dict['use']
                    if dict['n']:
                        dict_rsa['n'] = dict['n']
                    if dict['e']:
                        dict_rsa['e'] = dict['e']
                    print(dict_rsa)
    # check if token is valid. throw an error if key kid does not exist or rsa key is malformed
    except Exception as error:
        print(sys.exc_info())
        print(error)
        raise AuthError({'code':'the token is invalid',
         'description':'key kid does not exist or rsa key is malformed'}, 403)
        #raise auth_error()
    try:
        payload_decoded = jwt.decode(token, dict_rsa, algorithms=ALGORITHMS, audience=API_AUDIENCE, 
        issuer='https://' + AUTH0_DOMAIN + '/')
    #check if claims are valid
    except jwt.JWTClaimsError as error:
        print(sys.exc_info())
        print(error)
        raise AuthError({'code':'claims are not valid', 'description':'claims are not valid'}, 403)
    #check if token is not expired
    except jwt.ExpiredSignatureError as error:
        print(sys.exc_info())
        print(error)
        raise AuthError({'code':'token is expired', 'description':'token is expired'}, 403)
    except Exception as error:
        print(sys.exc_info())
        print(error)
        raise AuthError({'code':'payload is not decoded', 'description':'payload is not decoded'}, 403)

    return payload_decoded

def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            #check if token is valid, if not abort (in function)
            token = get_token_auth_header()
            #verify and decode token, if not abort(in function)
            payload = verify_decode_jwt(token)
            #check if permission is valid, if not abort (in function)
            check_permissions(permission, payload)
            return f(payload, *args, **kwargs)

        return wrapper
    return requires_auth_decorator

