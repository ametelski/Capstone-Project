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
from flask_cors import CORS


# if your instance of mongo is hosted elsewhere, change the params here to match
client = MongoClient('localhost', 27017)
db = client.ProgrammingForAll
admins = db.admins
students = db.students
testObjs = db.testObjs


app = Flask(__name__)
CORS(app)
title = "Programming for All"
heading = "PFA"


def clean_db():
    admins.drop()
    students.drop()

def add_student(student):
    jsonStudent = json.dumps(student, default=lambda o: o.__dict__)
    objStudent = json.loads(jsonStudent)
    students.insert(objStudent)


def add_admin(admin):
    admins.insert(admin.__dict__)


@app.route("/")
def hello():
    greeting = [{'greeting': 'Hello World!'}]
    return jsonify({'messages': greeting})


@app.route("/students", methods=['GET'])
def get_all_students():
    output = []
    for student in students.find():
        student['_id'] = str(student['_id'])
        output.append(student)

    return jsonify({'students' : output})

@app.route("/students/<int:studentId>", methods=['GET'])
def get_student_by_id(studentId):
    output = None
    for student in students.find({'id': studentId}):
        student['_id'] = str(student['_id'])
        output = student

    return jsonify({'student' : output})

'''
    skillConcept = Python || HTML || CSS
'''
@app.route('/students/<int:studentId>/<skillConcept>', methods=['GET'])
def get_student_skill_concepts(studentId, skillConcept):
    studentID = studentId
    skillType = skillConcept
    output = None

    skillConcepts = None
    for aStudent in students.find({"id": int(studentID)}):
        for aSkill in aStudent["skills"]:
            if aSkill["skillName"].lower() == skillType.lower():
                output = aSkill["skillConcepts"]

    return jsonify({'skillConcepts': output})

@app.route("/students/<int:studentId>/skills", methods=['GET'])
def get_student_skills(studentId):
    output = []
    for aStudent in students.find({"id": studentId}):
        aStudent['_id']=str(aStudent['_id'])
        output = aStudent["skills"]
    return jsonify({'skills': output})

@app.route("/admins", methods=['GET'])
def get_all_admins():
    output = []
    for admin in admins.find():
        admin['_id'] = str(admin['_id'])
        output.append(admin)
    return jsonify({'admins' : output})

'''
    http://127.0.0.1:5000/completed?studentID=12345&skillConcept=concept
'''
@app.route('/students/<int:studentId>/skillConcepts/completed', methods=['GET'])
def get_completed(studentId):
    output = []
    student = students.find_one({"id": studentId})
    for skill in student['skills']:
        for skillConcept in skill['skillConcepts']:
            if skillConcept['completed'] == True:
                output.append(skillConcept)

    return jsonify({'skillConcepts': output})


def populate_db():
    dummyAdmin = Admin('Cindy', 'Smith', 2, 'Admin', 'admin1@pfa.com')
    dummyStudent = Student('Timmy', 'Junior', 1, 12, 'student1@pfa.com')
    dummyStudent2 = Student('Bob', 'Well', 2, 10, 'student2@pfa.com')
    add_student(dummyStudent)
    add_student(dummyStudent2)
    add_admin(dummyAdmin)


if __name__ == "__main__":
    clean_db()
    populate_db()
    app.run()