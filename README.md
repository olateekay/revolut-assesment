# revolut-assesment
The scope of this project is to create the following:

1. Design and code a simple "Hello World" application that exposes the following HTTP-based APIs:
 Description: Request: Response:
Saves/updates the given user’s name and date of birth in the database.
PUT /hello/<username> { “dateOfBirth”: “YYYY-MM-DD” } 204 No Content
Note:
<username> must contain only letters. YYYY-MM-DD must be a date before the today date.
Description: Returns hello birthday message for the given user Request: Get /hello/<username>
Response: 200 OK
Response Examples:
A. If username’s birthday is in N days:
{ “message”: “Hello, <username>! Your birthday is in N day(s)”
}
B. If username’s birthday is today:
{ “message”: “Hello, <username>! Happy birthday!” }
Note: Use storage/database of your choice.
2. Produce a system diagram of your solution deployed to either AWS or GCP (it's not
required to support both cloud platforms).
3. Write configuration scripts for building and no-downtime production deployment of this application, keeping in mind aspects that an SRE would have to consider.

 Implicit requirements:
1. The code produced by you is expected to be of high quality.
2. The solution must have tests, runnable locally, and deployable to the cloud.
3. Use common sense.
Please put your work on github or bitbucket.



# Task Resolution


## Prerequisites
This guide assumes you already have the following installed locally

Postgres https://www.2ndquadrant.com/en/blog/pginstaller-install-postgresql/

Minikube cluster  https://minikube.sigs.k8s.io/docs/start/

Helm https://helm.sh/docs/helm/helm_install/

Make https://www.gnu.org/software/make/



## Version Used

Python 3.9.5

Helm 3.5.0

GNU Make 3.81

After installing postgres, create the database `users` , then create the columns, `id`, `username`, and `birthdate`. If not you will get this error ;

`Error while connecting to PostgreSQL relation "users" does not exist`

**Application uses postgresql and need following environment values:**

export DB_USER=supply your postgresdb user

export DB_PASSWORD=supply your postgresdb password

export DB_HOST=localhost

export DB_NAME=users
## Python Setup

- Set up your python virtualenv

- Install the following python modules

  `pip install -r requirements.txt`

 - Run the app by executing

   `python3 revolut_api/app.py`

   Test the GET and PUT methods on postman

   ![alt text](put.png)

   ![alt text](get.png)
  
- Run the tests by executing
  
  *NB*  you might need to run this 

  `export PYTHONPATH=$(pwd) for running tests`

   Then this, 

   `python tests/tests.py`


   ![pytests](pytests.png)

   **Tests includes for steps**
 - put unittest user with birtdate on 31-12-{now.year-1}
 - gets unittest user and checks response message
 - updates unittest user's birtdate to today
 - gets unittest user and checks response message


 - To dockerise the app, change directory to `revolut_api` and run the below command , we are using the first command so that our image can be accesible locally by minikube

`docker build -t revolutapi:v1`

 






