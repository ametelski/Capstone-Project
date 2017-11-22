# run.py

# Programming For All
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
skills = db.skills
admins = db.admins
skillConcepts = db.skillConcepts
students = db.students
testObjs = db.testObjs


app = Flask(__name__)
CORS(app)
title = 'Programming for All'
heading = 'PFA'

def clean_db():
    skills.drop()
    admins.drop()
    students.drop()
    skillConcepts.drop()

def add_student(student):
    jsonStudent = json.dumps(student, default=lambda o: o.__dict__)
    objStudent = json.loads(jsonStudent)
    students.insert(objStudent)

def add_skill_concept(skillConcept):
    jsonSC = json.dumps(skillConcept, default=lambda o: o.__dict__)
    objSC= json.loads(jsonSC)
    skillConcepts.insert(objSC)

def add_admin(admin):
    admins.insert(admin.__dict__)

def add_skill(skill):
    jsonSC = json.dumps(skill, default=lambda o: o.__dict__)
    objSC= json.loads(jsonSC)
    skills.insert(objSC)

@app.route('/')
def hello():
    greeting = [{'greeting': 'PFA backend is up and running.'}]
    return jsonify({'messages': greeting})

@app.route('/students', methods=['GET'])
def get_all_students():
    output = []
    for student in students.find():
        student['_id'] = str(student['_id'])
        output.append(student)

    return jsonify({'students' : output})

@app.route('/students/<int:studentId>', methods=['GET'])
def get_student_by_id(studentId):
    output = None
    for student in students.find({'id': studentId}):
        student['_id'] = str(student['_id'])
        output = student
        break
    return jsonify({'student' : output})

@app.route('/students/<int:studentId>/skills', methods=['GET'])
def get_student_skills(studentId):
    output = []
    aStudent = students.find_one({'id': studentId})
    for skillName in aStudent['skills']:
        skill = skills.find_one({'skillName':skillName})
        output.append({'skillName':skillName})
    return jsonify({'skills': output})

@app.route('/admins', methods=['GET'])
def get_all_admins():
    output = []
    for admin in admins.find():
        admin['_id'] = str(admin['_id'])
        output.append(admin)
    return jsonify({'admins' : output})

@app.route('/skillConcepts/<int:skillConceptId>', methods=['GET'])
def get_skill_concept(skillConceptId):
    skillConcept = skillConcepts.find_one({'id': skillConceptId})
    skillConcept['_id'] = str(skillConcept['_id'])
    return jsonify({'skillConcept': skillConcept})

@app.route('/skillConcepts/<int:skillConceptId>/<string:dataField>', methods=['POST'])
def edit_skill_concept_description(skillConceptId,dataField):
    value = request.json['value']
    skillConcepts.update_one({'id':skillConceptId}, {'$set': {dataField:value}})
    resultConcept = skillConcepts.find_one({'id':skillConceptId})
    resultConcept['_id'] = str(resultConcept['_id'])
    return jsonify(resultConcept)

@app.route('/students/<int:studentId>/skillConcepts/completed', methods=['GET'])
def get_skill_concepts_completed_by_student(studentId):
    output = []
    student = students.find_one({'id': studentId})
    skillConceptsCompleted = student['skillConceptsCompleted']
    for skillConceptId in skillConceptsCompleted:
        sc = skillConcepts.find_one({'id': skillConceptId})
        sc['_id'] = str(sc['_id'])
        output.append(sc)
    return jsonify({'skillConcepts': output})

@app.route('/students/<int:studentId>/skillConcepts/completedIds', methods=['GET'])
def get_skill_conceptsIds_completed_by_student(studentId):
    output = []
    student = students.find_one({'id': studentId})
    skillConceptsCompleted = student['skillConceptsCompleted']
    for skillConceptId in skillConceptsCompleted:
        sc = skillConcepts.find_one({'id': skillConceptId})
        sc['_id'] = str(sc['_id'])
        output.append(sc['id'])
    return jsonify({'skillConceptsIds': output})

@app.route('/students/<int:studentId>/skillConcepts', methods=['POST'])
def mark_concept_completed(studentId):
    aStudent = students.find_one({'id':studentId})
    data = request.data
    dataDict = json.loads(data)
    skillConceptCompleted = dataDict['completedSkillConcept']
    students.update(
        { 'id': studentId },
        { '$push': {'skillConceptsCompleted': skillConceptCompleted } })
    return jsonify({"appended":skillConceptCompleted})

@app.route('/skills', methods=['GET'])
def get_all_skills():
    output = []
    for skill in skills.find():
        skill['_id'] = str(skill['_id'])
        output.append(skill)
    return jsonify({'skills' : output})

@app.route('/skills/<string:skillName>/skillConcepts', methods=['GET'])
def get_skillConcepts_for_skill(skillName):
    output = []
    skill = skills.find_one({'skillName': skillName})
    skillConceptIds = skill['skillConceptsIds']
    for entry in skillConceptIds:
        skillConcept = skillConcepts.find_one({'id':entry})
        skillConcept['_id'] = str(skillConcept['_id'])
        output.append(skillConcept)
    return jsonify({'skillConcepts' : output})

@app.route('/skills/<string:skillName>/skillConceptsIds', methods=['GET'])
def get_skillConceptsIds_for_skill(skillName):
    output = []
    skill = skills.find_one({'skillName': skillName})
    skillConceptIds = skill['skillConceptsIds']
    for entry in skillConceptIds:
        skillConcept = skillConcepts.find_one({'id':entry})
        skillConcept['_id'] = str(skillConcept['_id'])
        output.append(skillConcept['id'])
    return jsonify({'skillConceptsIds' : output})


def populate_db():
    dummyAdmin = Admin('Cindy', 'Smith', 2, 'Admin', 'admin1@pfa.com')
    dummyStudent = Student('Timmy', 'Junior', 1, 12, 'student1@pfa.com', [1,3,4])
    dummyStudent2 = Student('Bob', 'Well', 2, 10, 'student2@pfa.com', [2, 8])
    scratchSkill = Skill("Scratch", "/scratch", [1,2,3,4,5,6,7,8])
    add_skill(scratchSkill)
    add_student(dummyStudent)
    add_student(dummyStudent2)
    add_admin(dummyAdmin)

    #default skillConcept entries for database
    scratchSkillConcepts = [

        SkillConcept('Sequencing', 1, 'IF and WHEN you\'re ready to dive in, here\'s the place to start! Learn all about sequencing and how to take control of your program\'s flow!', 'R1C1', [{'shortName':'Code Club - Rock Band', 'url':'https://codeclubprojects.org/en-GB/scratch/rock-band/'}, {'shortName':'Scratch Tutorials - Name Game', 'url':'https://scratchtutorials.com/tutorials/animate-your-name-using-colors'}]),
        SkillConcept('Repitition', 2, 'Well done, well done, well done. Let\'s learn about repitition!', 'R1C2', [{'shortName':'Code Club - Lost in Space','url':'https://codeclubprojects.org/en-GB/scratch/lost-in-space/'}, {'shortName':'Scratch MIT','url':'https://scratch.mit.edu/projects/89696985/'}]),
        SkillConcept('Variables', 3, 'What\'s a variable, you say? Let\'s get to the bottom of this by busting some ghosts!' , 'R2C2', [{'shortName':'Code Club - GhostBusters', 'url':'https://codeclubprojects.org/en-GB/scratch/ghostbusters/'}, {'shortName':'Scratch MIT', 'url':'https://scratch.mit.edu/projects/98831292/'}]),
        SkillConcept('Selection', 4, 'Build you\'re own chatbot to learn about selection!', 'R2C1', [{'shortName':'Code Club - Chatbot', 'url':'https://codeclubprojects.org/en-GB/scratch/chatbot/'}]),
        SkillConcept('Boolean Operators', 5, 'If(you == havingFun) then let\'s continue on and learn about boolean operators!', 'R3C1', [{'shortName':'Code Club - Paint Box', 'url':'https://codeclubprojects.org/en-GB/scratch/paint-box/'}, {'shortName': 'Scratch MIT', 'url':'https://wiki.scratch.mit.edu/wiki/Boolean_Block'}]),
        SkillConcept('Data Structures', 6, 'Data WHAT?! Impress your friends and family by making you\'re very own clone of Snake!', 'R3C2', [{'shortName':'Code Club - Memory', 'url':'https://codeclubprojects.org/en-GB/scratch/memory/'},{'shortName':'Gosh Darn Games - Snake','url':'https://www.goshdarngames.com/scratch-snake-tutorial/'},{'shortName':'Scratch MIT', 'url':'https://scratch.mit.edu/projects/17457737/'}]),
        SkillConcept('Functions', 7, 'Let\'s dive right in and write some funky functions!', 'R4C2', [{'shortName':'Code Club - Clone Wars', 'url':'https://codeclubprojects.org/en-GB/scratch/clone-wars/'}, {'shortName':'Code Club - Space Junk','url':'https://codeclubprojects.org/en-GB/scratch/space-junk/'}, {'shortName':'Code Club - Catch the Dots', 'url': 'https://codeclubprojects.org/en-GB/scratch/catch-the-dots/'}]),
        SkillConcept('Project Management (Boss Mode)', 8, 'Welcome to the boss fight. WoW! Look how far you\'ve come!! You can do it!', 'R4C1', [{'shortName':'Code Club - Binary Hero', 'url':'https://codeclubprojects.org/en-GB/scratch/binary-hero/'}])]


    for newSkillConcept in scratchSkillConcepts:
        add_skill_concept(newSkillConcept);


if __name__ == '__main__':
    clean_db()
    populate_db()
    app.run()
