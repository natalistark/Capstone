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
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}

GET 'api/v1.0/questions/'
- Fetches a dictionary with all questions, all categories, current category, and a count of all questions
- Request Arguments: None
- Returns: a dictionary with dictionary of questions, categories, current category, number of all available questions, success status
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "current_category": {}, 
  "num_questions": 23, 
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }
  ], 
  "success": true


DELETE 'api/v.1.0/questions/<int:question_id>'
- Deletes question with a specific question_id
- Request Arguments: question_id
- Returns a dictionary with success status and question_id of a deleted question

curl -X DELETE http://127.0.0.1:5000/questions/28
{
  "question_deleted": 37, 
  "success": true
}


POST 'api/v1.0/questions/'
- Posts a new question with question, answer, category and difficulty
- Request Arguments: None
- Returns dictionary with success status and question and question_id created

curl -d '{"question":"value1", "answer":"value2", "category":"1", "difficulty":"2"}' -H "Content-Type: application/json" -X POST http://localhost:5000/questions

{
  "question_created": "value1", 
  "success": true
  "question_id": 1
}

POST 'api/v1.0/questions/search'
- Posts a search for a phrase, case insensitive, partial match
- Request Arguments: None
- Returns a dictionary with current category, list of questions(a dictionary contains answer, category, difficulty, id, and question), count of questions

curl -X POST -H "Content-Type: application/json" -d'{"searchTerm":"taj"}' http://127.0.0.1:5000/questions/search

{
  "current_category": {}, 
  "questions": [
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ], 
  "total_questions": 1
}

GET 'api/v.1.0/categories/<int:category_id>/questions'
- Fetches a dictionary with questions for a specific category
- Request Arguments: category_id
- Returns a dictionary with questions for a specific category, current category_id, success status

curl http://127.0.0.1:5000/categories/3/questions
{
  "category_id": 3, 
  "questions": [
    {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ], 
  "success": true
}

POST 'api/v.1.0/quizzes'
- Fetches a random question for a specific category and difficulty, excluding questions that were already answered
- Request Arguments: None
- Returns a dictionary with a random question(a dictionary contains answer, category, difficulty, id, and question), status

{
      "question": {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
      "success": True
    }

```


## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
