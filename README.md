

1. Clone the repo
git clone https://github.com/<your-username>/late-show-api-challenge.git
cd late-show-api-challenge
2. Install dependencies

pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary
pipenv shell
3. Set up your PostgreSQL database
Make sure PostgreSQL is installed and running, then create your DB:

sql
CREATE DATABASE late_show_db;
4. Configure your database URL
In server/config.py, set your connection string:

SQLALCHEMY_DATABASE_URI = "postgresql://<your_user>:<your_password>@localhost:5432/late_show_db"
5. Run the migrations and seed data
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
python server/seed.py
 Authentication Flow
This API uses JWT (JSON Web Tokens) to handle authentication.

Register: POST /register

Login: POST /login → returns a token

Use the token in the Authorization header for protected routes:

Authorization: Bearer <your_token_here>
Protected routes include:

POST /appearances

DELETE /episodes/<id>

 Available Endpoints

register	POST		Register a new user
nces
/episodes/<id>	DELETE		Delete an episode and its appearances
/	List all guests
/appearances	POST		Create a guest appearance on an episode

Register a user



POST /register
Content-Type: application/json

{
  "username": "sam",
  "password": "mypassword"
}

Edit
POST /login
Content-Type: application/json

{
  "username": "sam",
  "password": "mypassword"
}
Response:

{
  "access_token": "your.jwt.token"
}
🎬
[
  {
    "id": 1,
    "date": "2025-06-01",
    "number": 12
  },
  ...
]
 Postman Testing
To test your API easily:

Open Postman

Import the file: challenge-4-lateshow.postman_collection.json

Start by registering and logging in

Use the JWT token in protected routes (paste it in the Authorization tab as Bearer <token>)

 Submission Checklist
 MVC folder structure followed

 PostgreSQL used (no SQLite)

 Models created with proper relationships & validation

 Auth (JWT) works with protected routes

All routes tested in Postman

 Seed file included and working

 Clean, complete README.md

 GitHub repo pushed and submitted

