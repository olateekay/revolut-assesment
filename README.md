# revolut-assesment
  DevOps Engineer Test
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