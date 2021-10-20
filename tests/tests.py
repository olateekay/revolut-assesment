import unittest
from revolut_api import app
import os
import json
from datetime import datetime
import sys
import xmlrunner

class MyTestCase(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        DB_PORT=5432
        if os.environ.get('DB_PORT'):
            DB_PORT=os.environ.get('DB_PORT')
        app.app.config["CONNECTION_STRING"]="dbname='{}' user='{}' host='{}' password='{}' port='{}'".format(os.environ.get('DB_NAME'),os.environ.get('DB_USER'), os.environ.get('DB_HOST'),os.environ.get('DB_PASSWORD'), DB_PORT)  
        self.app = app.app.test_client()
        app.app.config["USER"]="unittest"
        self.api = "/hello/"
        now = datetime.now()
        app.app.config["DATE"]="{}-12-31".format(now.year-1)
        self.format="%Y-%m-%d"
        

    def test_1_put(self):
        data = {"dateOfBirth": app.app.config["DATE"]}
        headers = {'content-type': 'application/json'}
        response = self.app.put(self.api+app.app.config["USER"],data=json.dumps(data), headers=headers)     
        print("Check adding entry - status code is equal 204")   
        self.assertEqual(204,response.status_code)

    def test_2_get(self):
        now = datetime.now()
        birthdate = datetime.strptime(app.app.config["DATE"], self.format)
        formatted_birthday = datetime(now.year, birthdate.month, birthdate.day)
        days_to_birthday=(formatted_birthday - now.today()).days+1
        if(days_to_birthday>0):
            response_message = {"message": "Hello, {}! Your birthday is in {} day(s)".format(app.app.config["USER"], days_to_birthday)}                
        elif days_to_birthday == 0:
            response_message = {"message": "Hello, {}! Happy birthday!".format(app.app.config["USER"])}
        response = self.app.get(self.api+app.app.config["USER"]) 
        print("Check get entry - status code is equal 200 and check response message")
        self.assertEqual(200,response.status_code)
        self.assertEqual(response_message,json.loads(response.get_data()))

    def test_3_put(self):
        headers = {'content-type': 'application/json'}
        now = datetime.now()
        birthdate = datetime.strptime(app.app.config["DATE"], self.format)
        today_birthday = datetime(birthdate.year, now.month, now.day)
        app.app.config["DATE"]=today_birthday.strftime(self.format)
        data = {"dateOfBirth": app.app.config["DATE"]}
        response = self.app.put(self.api+app.app.config["USER"],data=json.dumps(data), headers=headers)     
        print("Check updating entry with birthdate today- status code is equal 204")   
        self.assertEqual(204,response.status_code)

    def test_4_get(self):
        response_message = {"message": "Hello, {}! Happy birthday!".format(app.app.config["USER"])}
        response = self.app.get(self.api+app.app.config["USER"]) 
        print("Check get entry - status code is equal 200 and check response message")
        self.assertEqual(200,response.status_code)
        self.assertEqual(response_message,json.loads(response.get_data()))

if __name__ == '__main__':
    # unittest.main()
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
