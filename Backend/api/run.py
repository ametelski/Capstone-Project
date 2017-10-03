# run.py

# Programming For All
# TODO: Divide the routes in to separate files using Blueprints to simplify and modularize the project.
# http://flask.pocoo.org/docs/0.12/blueprints/
# Author: Gabriel Fabian, 2017
# Author: Miguel Deniz
# Last update: 10/2/17

from models.Person import *
from models.Admin import *
from models.Student import *
from pymongo import MongoClient
import json
from bson.json_util import dumps
from flask import *


# if your instance of mongo is hosted elsewhere, change the params here to match
client = MongoClient('localhost', 27017)
db = client.ProgrammingForAll
admins = db.admins
students = db.students


app = Flask(__name__)
title = "Programming for All"
heading = "PFA"


def clean_db():
    admins.drop()
    students.drop()

def add_student(student):
    students.insert(student.__dict__)

def add_admin(admin):
    admins.insert(admin.__dict__)

'''
    Description:
        Returns a 'Hello World!' string.
    
    Params:
        None
        
    Returns:
        JSON with String
'''
@app.route("/")
def hello():
    greeting = [{'greeting': 'Hello World!'}]
    return jsonify({'messages': greeting})


'''
    Description:
        Returns a list of students currently stored in the database

    Params:
        None

    Returns:
        JSON

        Example:
            {
                "students": [
                    {
                        "age": 12, 
                        "email": "student1@pfa.com", 
                        "firstName": "Timmy", 
                        "id": 1, 
                        "lastName": "Junior"
                    }
                ]
            }
'''
@app.route("/students", methods=['GET'])
def get_all_students():
    output = []
    for student in students.find():
        output.append({'firstName' : student['firstName'], 'lastName' : student['lastName'], \
            'id' : student['id'], 'age' : student['age'], 'email' : student['email']})
    return jsonify({'students' : output})


'''
    Description:
        Returns a list of admins currently stored in the database

    Params:
        None

    Returns:
        JSON

        Example:
            {
                "admins": [
                    {
                        "email": "admin1@pfa.com", 
                        "firstName": "Cindy", 
                        "id": 2, 
                        "lastName": "Smith", 
                        "role": "Admin"
                    }
                ]
            }
'''
@app.route("/admins", methods=['GET'])
def get_all_admins():
    output = []
    for admin in admins.find():
        output.append({'firstName' : admin['firstName'], 'lastName' : admin['lastName'], \
            'id' : admin['id'], 'role' : admin['role'], 'email' : admin['email']})
    return jsonify({'admins' : output})

'''
    Description:
        Returns a list of all skills and their statuses for a specific user.
    
    Params:
        userID
    
    Returns:
        JSON
        
        {
            "skills": [
                {
                    "skillConcepts": "concepts", 
                    "skillConceptsCompleted": "45", 
                    "skillName": "HTML", 
                    "skillURL": "www.url0.com"
                }, 
                {
                    "skillConcepts": "concepts", 
                    "skillConceptsCompleted": "23", 
                    "skillNam": "Python", 
                    "skillURL": "www.url1.com"
                }, 
                {
                    "skillConcepts": "concepts", 
                    "skillConceptsCompleted": "78", 
                    "skillNam": "CSS", 
                    "skillURL": "www.url2.com"
                }
            ]
        }
'''
@app.route("/getSkill/<userID>", methods=['GET'])
def get_skill(userID = None):

    'TODO: These are just constant values for now, later on they should be retreived from the database using the userID'

    CONST_SKILL_NAME_DESC = "skillName";
    skillName1 = "HTML";
    skillName2 = "Python";
    skillName3 = "CSS";

    CONST_SKILL_URL_DESC = "skillURL";
    skillURL1 = "www.url1.com";
    skillURL2 = "www.url2.com";
    skillURL3 = "www.url3.com";

    CONST_SKILL_COMPLETED_DESC = "skillConceptsCompleted";
    skillPercentage1 = "43";
    skillPercentage2 = "100";
    skillPercentage3 = "0";

    CONST_SKILL_CONCEPTS_DESC = "skillConcepts";
    concepts1 = "concepts1value";
    concepts2 = "concepts2value";
    concepts3 = "concepts3value";

    list = [
        {CONST_SKILL_NAME_DESC: skillName1, CONST_SKILL_URL_DESC: skillURL1, CONST_SKILL_COMPLETED_DESC: skillPercentage1, CONST_SKILL_CONCEPTS_DESC: concepts1},
        {CONST_SKILL_NAME_DESC: skillName2, CONST_SKILL_URL_DESC: skillURL2, CONST_SKILL_COMPLETED_DESC: skillPercentage2, CONST_SKILL_CONCEPTS_DESC: concepts2},
        {CONST_SKILL_NAME_DESC: skillName3, CONST_SKILL_URL_DESC: skillURL3, CONST_SKILL_COMPLETED_DESC: skillPercentage3, CONST_SKILL_CONCEPTS_DESC: concepts3}
    ]
    return jsonify(skills = list)


'''
    Description:

    Params:

    Returns:

'''
@app.route('/getSkillConcept/<userID>', methods=['GET'])
def get_skill_concept(userID = None, skillType = None):
    return jsonify({''})


def populate_db():
    dummyAdmin = Admin('Cindy', 'Smith', 2, 'Admin', 'admin1@pfa.com')
    dummyStudent = Student('Timmy', 'Junior', 1, 12, 'student1@pfa.com')
    add_student(dummyStudent)
    add_admin(dummyAdmin)


if __name__ == "__main__":
    clean_db()
    populate_db()
    app.run()