
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

Installation of Python 3.6.9 or later is needed. Please install it using the official documentation of python such as this
https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python

#### PIP Dependencies

Please use terminal and cd into directory of the Podcast project and with the help of pip install install all the requirements from requirements.txt

```
pip install -r requirements.txt
```

This will install all of the required packages.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Running the server

To run the server, execute:
```
python3 app.py
```
We can now also open the application via Heroku using the URL:
https://warranty-tracker.herokuapp.com

The live application can only be used to generate tokens via Auth0, the endpoints have to be tested using curl or Postman 
using the token since I did not build a frontend for the application.

## DATA MODELING:
#### models.py
The schema for the database and helper methods to simplify API behavior are in models.py:
- There are three tables created: Product, User, and Items_for_Sale
- The Product table is used by the role 'user' to add new products and their warranty dates, and also retrieve these products.
- The Product table has a foreign key on the User table for user_id.
- The Items_for_Sale table is used by the role 'seller' to add new items to sell, and to retrieve these items.
- The Items_for_Sale table has a foreign key on the User table for user_id as well.
- The User table keeps track of the users who want to post or retrieve their products or items by storing their name, email, and products/item.
Each table has an insert, update, delete, and format helper functions.

## USER ROLES:

## API ARCHITECTURE AND TESTING
### Endpoint Library

@app.errorhandler decorators were used to format error responses as JSON objects. Custom @requires_auth decorator were used for Authorization based
on roles of the user. Two roles are assigned to this API: 'user' and 'seller'. The 'user' role is assigned by default when someone creates an account
from the login page, while the 'seller' role is already pre-assigned to certain users.

A token needs to be passed to each endpoint. 
The following only works for /products endpoints:
The token can be retrived by following these steps:
1. Go to https: https://warranty-tracker.herokuapp.com
2. Click on Login and enter any credentials into the Auth0 login page. The role is automatically assigned by Auth0. 
   Alternatively, sample account that has already been created can be used:
   Email: test_user_role@gmail.com
   Password: test1234!

#### GET '/products'
Returns a list of all available products belonging to the user, total number of products, and a success value.
Sample curl: 
curl -i -H "Content-Type: application/json" -H "Authorization: Bearer {INSERT_TOKEN_HERE}" http://localhost:5000/products 
Sample response output:
{
  "products": [
    {
      "date_purchased": "Thu, 12 May 2016 00:00:00 GMT",
      "id": 2,
      "name": "Printer",
      "user_id": 2,
      "warranty_end_date": "Tue, 12 May 2020 00:00:00 GMT"
    },
    {
      "date_purchased": "Thu, 12 May 2016 00:00:00 GMT",
      "id": 3,
      "name": "Printer",
      "user_id": 2,
      "warranty_end_date": "Tue, 12 May 2020 00:00:00 GMT"
    }
  ],
  "success": true,
  "total_products": 2
}

#### POST '/products'
Returns a list of all products belonging to user, along with new product posted, a success value, and total number of products.
Sample curl: 
curl http://localhost:5000/products -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {INSERT_TOKEN_HERE}" -d '{"name":"Printer", "date_purchased": "2016-05-12", "warranty_end_date": "2020-05-12"}'
Sample response output:
{
  "products": [
    {
      "date_purchased": "Thu, 12 May 2016 00:00:00 GMT",
      "id": 2,
      "name": "Printer",
      "user_id": 2,
      "warranty_end_date": "Tue, 12 May 2020 00:00:00 GMT"
    }
  ],
  "success": true,
  "total_products": 1
}

#### PATCH '/products/{product_id}'
Returns a list of all products belonging to user, along with updated product, a success value, and total number of products.
Sample curl:
curl http://localhost:5000/products/1 -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {INSERT_TOKEN_HERE}" -d '{"name":"Canon Printer", "date_purchased": "2016-05-12", "warranty_end_date": "2020-05-12"}'
{
  "products": [
    {
      "date_purchased": "Thu, 12 May 2016 00:00:00 GMT",
      "id": 2,
      "name": "Canon Printer",
      "user_id": 2,
      "warranty_end_date": "Tue, 12 May 2020 00:00:00 GMT"
    }
  ],
  "success": true,
  "total_products": 1
}

#### DELETE '/products/{product_id}'
Returns a list of all products after deleting the requested product, a success value, and total number of products.
curl http://localhost:5000/products/1 -X DELETE -H "Content-Type: application/json" -H "Authorization: Bearer {INSERT_TOKEN_HERE}" 
{
  "products": [],
  "success": true,
  "total_products": 0
}

To get the tokens for /items endpoints, we need the payload to contain the seller role permissions.
For this, we can once again go to the hosted heroku URL:
1. Go to https: https://warranty-tracker.herokuapp.com
2. Click on Login and enter the following credentials into Auth0, which has been designated with seller role:
   Email: test_seller_role@gmail.com
   Password: test1234!
 
#### GET '/items'
Returns a list of all items belonging to the user, total number of items, and a success value.
Sample curl: 
curl -i -H "Content-Type: application/json" -H "Authorization: Bearer {INSERT_TOKEN_HERE}" http://localhost:5000/items 
Sample response output:
{
  "items": [
    {
      "id": 2,
      "image_link": "getprinter.com",
      "item_description": "Brand new and good quality",
      "name": "Printer",
      "user_id": 3,
      "warranty_period": 4
    }
  ],
  "success": true,
  "total_items": 1
}

#### POST '/items'
Returns a list of all products belonging to user, along with new product posted, a success value, and total number of items.
Sample curl: 
curl http://localhost:5000/products -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {INSERT_TOKEN_HERE}" -d '{"name":"Printer", "warranty_period": 4, "item_description": "Brand new and good quality", "image_link": "getprinter.com"}'
Sample response output:
{
  "items": [
    {
      "id": 2,
      "image_link": "getprinter.com",
      "item_description": "Brand new and good quality",
      "name": "Printer",
      "user_id": 3,
      "warranty_period": 4
    }
  ],
  "success": true,
  "total_items": 1
}

#### DELETE '/items/1'
Returns a list of all items after deleting the requested item, a success value, and total number of items.
curl http://localhost:5000/items/1 -X DELETE -H "Content-Type: application/json" -H "Authorization: Bearer {INSERT_TOKEN_HERE}" 
{
  "products": [],
  "success": true,
  "total_products": 0
}

## Testing
There are 19 unittests in test_app.py. To run this file use:
```
dropdb warranty_test
createdb warranty_test
python test_app.py
```
The tests include one test for expected success and error behavior for each endpoint, and tests demonstrating role-based access control, 
where all endpoints are tested with and without the correct authorization.
Further, the file 'warranty-tracker-test-endpoints.postman_collection.json' contains postman tests containing tokens for specific roles.
To run this file, follow the steps:
1. Go to postman application.
2. Load the collection --> Import -> directory/warranty-tracker-test-endpoints.postman_collection.json
3. Click on the runner, select the collection and run all the tests.

## THIRD-PARTY AUTHENTICATION
#### auth.py
Auth0 is set up and running. The following configurations are in a .env file which is exported by the app:
- The Auth0 Domain Name
- The JWT code signing secret
- The Auth0 Client ID
The JWT token contains the permissions for the 'user' and 'seller' roles.

## DEPLOYMENT
The app is hosted live on heroku at the URL: 
https://warranty-tracker.herokuapp.com

However, there is no frontend for this app yet, and it can only be presently used to authenticate using Auth0 by entering
credentials and retrieving a fresh token to use with curl or postman.


=====

Capstone Project

This is a webservice that shows podcasts, their episodes and artists that create podcasts. Content creator and podcast superviser have writes to CRUD operations.

Content creator(role: Content_Creator) can:
1. get information about artists
Permissions: get:artists
2. get information about podcasts
Permissions: get:podcasts
3. post information about artists
Permissions: post:artists
4. post information about podcasts
Permissions: post:podcasts


Podcast supervisor(role: Podcast_Superviser) can:
1. get information about artists
get:artists
2. get information about podcasts
Permissions: get:podcasts
3. post information about artists
Permissions: post:artists
4. post information about podcasts
Permissions: post:podcasts
5. change information about artists
Permissions: patch:artists
6. delete information about artists
Permissions: delete:artists




Endpoints
GET '/api/v1.0/podcasts'
GET 'api/v1.0/artists/'
DELETE 'api/v.1.0/podcasts/<int:podcast_id>'
POST 'api/v1.0/podcasts/'

GET '/api/v1.0/podcasts'
- Fetches a dictionary of podcasts in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: dict

GET '/api/v1.0/artists'
- Fetches a dictionary of artists 
- Request Arguments: None
- Returns: dict

DELETE 'api/v.1.0/podcasts/<int:podcast_id>'
- Deletes podcast with a specific podcast_id
- Request Arguments: podcast_id
- Returns a dictionary with success status and podcast_id of a deleted podcast


POST 'api/v1.0/artists/'
- Posts a new artists
- Request Arguments: None
- Returns dictionary with success status and artist created

