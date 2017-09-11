# run.py

# Programming For All
# TODO: Divide the routes in to separate files using Blueprints to simplify and modularize the project.
# http://flask.pocoo.org/docs/0.12/blueprints/
# Author: Gabriel Fabian, 2017

from models.Person import *
from models.Admin import *
from models.Student import *
from pymongo import MongoClient
import json
from bson.json_util import dumps
from flask import *


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

@app.route("/")
def hello():
    greeting = [{'greeting': 'Hello World!'}]
    return jsonify({'messages': greeting})

@app.route("/students", methods=['GET'])
def get_all_students():
    output = []
    for student in students.find():
        output.append({'firstName' : student['firstName'], 'lastName' : student['lastName'], \
            'id' : student['id'], 'age' : student['age']})
    return jsonify({'students' : output})

@app.route("/admins", methods=['GET'])
def get_all_admins():
    output = []
    for admin in admins.find():
        output.append({'firstName' : admin['firstName'], 'lastName' : admin['lastName'], \
            'id' : admin['id'], 'role' : admin['role']})
    return jsonify({'students' : output})

def populate_db():
    dummyAdmin = Admin('Cindy', 'Smith', 2, 'Admin')
    dummyStudent = Student('Timmy', 'Junior', 1, 12)
    add_student(dummyStudent)
    add_admin(dummyAdmin)


if __name__ == "__main__":
    clean_db()
    populate_db()
    app.run()