# run.py

# Programming For All
# TODO: Divide the routes in to separate files using Blueprints to simplify and modularize the project.
# http://flask.pocoo.org/docs/0.12/blueprints/
# Author: Gabriel Fabian, 2017
# Author: Miguel Deniz
# Last update: 10/2/17

from models.Admin import *
from models.Student import *
from models.Skill import *
from pymongo import MongoClient
import json
import bson.json_util
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
    studentDict = student.__dict__
    for x in range(0, len(studentDict["skills"])):
        studentDict["skills"][x] = studentDict["skills"][x].__dict__
        for i in range(0, len(studentDict["skills"][x]["skillConcepts"])):
            studentDict["skills"][x]["skillConcepts"][i] = studentDict["skills"][x]["skillConcepts"][i].__dict__
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
    #Output everything in Students
    for aStudent in students.find():
        aStudent['_id'] = "discard this"
        output.append(aStudent)
    #Output hardcoded, will have to change everytime design of student is changed
    '''    output.append({'firstName' : student['firstName'], 'lastName' : student['lastName'], \
            'id' : student['id'], 'age' : student['age'], 'email' : student['email']}) '''
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
        
        http://127.0.0.1:5000/getSkill?userID=USER_ID
    
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
                    "skillName": "Python", 
                    "skillURL": "www.url1.com"
                }, 
                {
                    "skillConcepts": "concepts", 
                    "skillConceptsCompleted": "78", 
                    "skillName": "CSS", 
                    "skillURL": "www.url2.com"
                }
            ]
        }
'''
@app.route("/getSkill", methods=['GET'])
def get_skill():
    output = None
    studentID = request.args.get('studentID');
    for aStudent in students.find({"id": int(studentID)}):
        aStudent['_id']="discard this";
        output = aStudent["skills"]           #since ID is unique, there should only be 1 student object returned
    return jsonify(output)


'''
    Description:
        Returns the skill concepts for a specific userID and skillType
    
        http://127.0.0.1:5000/getSkillConcept?userID=12345&skillType=Python

    Params:
        userID, skillType
    Returns:
        JSON
        
        {
          "completed": true, 
          "extLearnLinks": "www.google.com,www.bing.com,www.ask.com", 
          "location": "1,2", 
          "skillDescription": "Python skill concepts", 
          "skillTitle": "Python"
        }

'''
@app.route('/getSkillConcepts', methods=['GET'])
def get_skill_concept():

    """TODO: Returns skill concepts based on the USER ID from the database """

    studentID = request.args.get('studentID');
    skillType = request.args.get('skillType');
    output = None

    skillConcepts = None
    for aStudent in students.find({"id": int(studentID)}):
        for aSkill in aStudent["skills"]:
            if aSkill["skillName"].lower() == skillType.lower():
                output = aSkill["skillConcepts"]
                return jsonify(output)

    return "Could not find skill concepts"

'''
    Description:
        Returns a boolean that depending if the skill concept is completed by the given user ID.
        
        http://127.0.0.1:5000/completed?studentID=12345&skillConcept=concept
    
    Params:
        studentID, skillType, skillTitle
        
    Returns:
        JSON
        
        {
          "completed": false, 
          "skillConcept": "concept", 
          "studentID": "200"
        }
'''
@app.route('/completed', methods=['GET'])
def get_completed():

    '''TODO: Return completion based on the USER ID and SKILL CONCEPT from the database'''

    studentID = request.args.get('studentID');
    skillType = request.args.get('skillType');
    skillTitle = request.args.get('skillTitle');
    if studentID == None or skillTitle == None or skillType == None:
        return "Bad parameter"
    output = {}

    for aStudent in students.find({"id": int(studentID)}):
        for aSkill in aStudent["skills"]:
            if aSkill["skillName"].lower() == skillType.lower():
                for aConcept in aSkill["skillConcepts"]:
                    if aConcept["skillTitle"].lower() == skillTitle.lower():
                        output["completed"] = aConcept["completed"]
                        output["skillTitle"] = aConcept["skillTitle"]
                        output["studentID"] = studentID
                        return jsonify(output)

    return "Could not fine the skillConcept"


def populate_db():
    dummyAdmin = Admin('Cindy', 'Smith', 2, 'Admin', 'admin1@pfa.com')
    dummyStudent = Student('Timmy', 'Junior', 1, 12, 'student1@pfa.com',None)
    dummyStudent2 = Student('Bob', 'Well', 2, 10, 'student2@pfa.com', None)
    add_student(dummyStudent)
    add_student(dummyStudent2)
    add_admin(dummyAdmin)


if __name__ == "__main__":
    clean_db()
    populate_db()
    app.run()