import flask
from flask import request, jsonify, make_response
from datetime import datetime
import re
import json
import os
import psycopg2


app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["DATE_FORMAT"] = "%Y-%m-%d"
DB_PORT=5432
if os.environ.get('DB_PORT'):
    DB_PORT=os.environ.get('DB_PORT')
     
app.config["CONNECTION_STRING"]="dbname='{}' user='{}' host='{}' password='{}' port='{}'".format(os.environ.get('DB_NAME'),os.environ.get('DB_USER'), os.environ.get('DB_HOST'),os.environ.get('DB_PASSWORD'), DB_PORT)  
def get_birthdate(username):
        try:
            connectionString=app.config["CONNECTION_STRING"]
            
            #Check if user is presented in DB
            connection = psycopg2.connect(connectionString)

            # Create a cursor to perform database operations
            cursor = connection.cursor()
            # Executing a SQL query
            cursor.execute("SELECT id, username,birthdate FROM users WHERE username='{}';".format(username))
            # Fetch result
            if cursor.rowcount>0:
                record = cursor.fetchone()
                return record[2]
            else:
                return None
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if 'connectnio' in locals():
                if (connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed")
def update_birthdate(username, birthdate):
    try:
        connectionString=app.config["CONNECTION_STRING"]
            
        #Check if user is presented in DB
        connection = psycopg2.connect(connectionString)

        # Create a cursor to perform database operations
        cursor = connection.cursor()
        # Executing a SQL query
        cursor.execute("UPDATE users SET birthdate = '{}' WHERE username  = '{}';".format(birthdate, username))
        # Fetch result
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if 'connectnio' in locals():
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
def add_birthdate(username, birthdate):
        try:
            connectionString=app.config["CONNECTION_STRING"]
            
            #Check if user is presented in DB
            connection = psycopg2.connect(connectionString)

            # Create a cursor to perform database operations
            cursor = connection.cursor()
            # Executing a SQL query
            cursor.execute("INSERT into users (username, birthdate) VALUES ('{}', '{}');".format(username,birthdate))
            # Fetch result
            connection.commit()
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if 'connectnio' in locals():
                if (connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed")

@app.route('/hello/<username>', methods=['GET'])
def get_hello(username):
    if username.isalpha():
        try:
            birthdate = get_birthdate(username)
            if(birthdate):
                    now = datetime.now()
                    formatted_birthday = datetime(now.year, birthdate.month, birthdate.day)
                    days_to_birthday=(formatted_birthday - now.today()).days+1
                    if(days_to_birthday>0):
                        return jsonify(
                            message="Hello, {}! Your birthday is in {} day(s)".format(username, days_to_birthday)
                        )
                    elif days_to_birthday == 0:
                        return jsonify(
                            message="Hello, {}! Happy birthday!".format(username)
                        )
                    else:
                        return jsonify(
                            message="Hello, {}! Your birthday has already passed".format(username)
                        )
            else:
                return ({"error": "username {} is not presented".format(username)}, 400)
        except (Exception) as error:
            print(error)
            return ({"error": "something went wrong"}, 400)
    else:
        return ({"error": "username must contain only letters"}, 400)

@app.route('/hello/<username>', methods=['PUT'])
def put_hello(username):
    if username.isalpha():
        if request.headers.get('Content-Type') == 'application/json':
            if request.is_json:
                try:
                    dateOfBirth=datetime.strptime(request.get_json()['dateOfBirth'], app.config["DATE_FORMAT"])
                    if dateOfBirth < datetime.now():
                        if get_birthdate(username):
                            update_birthdate(username, dateOfBirth)
                            return ('', 204)
                        else:
                            add_birthdate(username, dateOfBirth)
                            return ('', 204)
                    else:
                        return ({"error": "date must not exceed today"}, 400)
                except (Exception) as parseError:
                    print(parseError)
                    return ({"error": "parsing error: {}".format(parseError)}, 400)
            else:
                return ({"error": "body of PUT request should be json-formatted"}, 400)             
        else:
            return ({"error": "header 'Content-Type' should be application/json"}, 400)
    else:
        return ({"error": "username must contain only letters"}, 400)

if __name__ == '__main__':
    HOST="localhost"
    if os.environ.get('APP_HOST'):
            HOST=os.environ.get('APP_HOST')
    PORT=5000
    if os.environ.get('APP_PORT'):
            PORT=os.environ.get('APP_PORT')
    app.run(host=HOST, port=PORT, debug=True)
