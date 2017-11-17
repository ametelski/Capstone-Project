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
    greeting = [{'greeting': 'Hello World!'}]
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

'''
    skill = Python || HTML || CSS
'''
@app.route('/students/<int:studentId>/<skillName>', methods=['GET'])
def get_student_skill_concepts(studentId, skillName):

    output = None
    aStudent = students.find_one({'id': int(studentId)})
    for aSkill in aStudent['skills']:
        if aSkill == skillName.lower():
            for skillConceptId in aSkill['skillConceptsIds']:
                concept = skillConcepts.find_one({'id':skillConceptId})
                concept['_id'] = str(concept['_id'])
                output.append(concept)

    return jsonify({'skillConcepts': output})

@app.route('/students/<int:studentId>/skills', methods=['GET'])
def get_student_skills(studentId):
    aStudent = students.find_one({'id': studentId})
    aStudent['_id']=str(aStudent['_id'])
    for i in range(len(aStudent['skills'])):
        aSkill = aStudent['skills'][i]
        aSkill["skillConcepts"] = []
        for aSkillConceptId in aSkill['skillConceptsIds']:
            aSkill["skillConcepts"].append(skillConcepts.find_one({'id': aSkillConceptId}))
            del aSkill["skillConcepts"][len(aSkill["skillConcepts"])-1]['_id']
        completedPercentage = len(aSkill['skillConceptsCompleted'])*100 / len(aSkill['skillConceptsIds'])
        aSkill['completedPercentage'] = completedPercentage
        del aSkill['skillConceptsIds']
        del aSkill['skillConceptsCompleted']
        aStudent['skills'][i] = aSkill

    output = aStudent['skills']
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

'''
    http://127.0.0.1:5000/completed?studentID=12345&skillConcept=concept
'''
@app.route('/students/<int:studentId>/skillConcepts/completed', methods=['GET'])
def get_completed(studentId):
    output = []
    student = students.find_one({'id': studentId})
    for aSkill in student['skills']:
        completed = {'skillName':aSkill['name'], 'skillConceptsCompleted':[]}
        for skillConceptId in aSkill['skillConceptsCompleted']:
            skillConcept = skillConcepts.find_one({'id': skillConceptId})
            skillConcept['_id'] = str(skillConcept['_id'])
            completed['skillConceptsCompleted'].append(skillConcept)
        output.append(completed)

    return jsonify({'skillConcepts': output})

@app.route('/students/<int:studentId>/skillName/<string:skillName>/skillConceptId/<int:skillConceptId>/mark_completed', methods=['POST'])
def mark_concept_completed(studentId, skillName, skillConceptId):
    aStudent = students.find_one({'id':studentId})
    for aSkill in aStudent['skills']:
        if aSkill['skillName'].lower() == skillName.lower():
            aSkill['skillConceptsCompleted'] = set(aSkill['skillConceptsCompleted'])
            aSkill['skillConceptsCompleted'].add(skillConceptId)
            aSkill['skillConceptsCompleted'] = list(aSkill['skillConceptsCompleted'])
            students.update(
                {
                    'id':studentId,
                },
                {
                    '$set':{'skills': aStudent['skills']}
                }
            )
            break;
    return jsonify({})

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

def populate_db():
    dummyAdmin = Admin('Cindy', 'Smith', 2, 'Admin', 'admin1@pfa.com')
    dummyStudent = Student('Timmy', 'Junior', 1, 12, 'student1@pfa.com')
    dummyStudent2 = Student('Bob', 'Well', 2, 10, 'student2@pfa.com')
    scratchSkill = Skill("Scratch", "/scratch", [1,2,3,4,5,6,7,8])
    add_skill(scratchSkill)
    add_student(dummyStudent)
    add_student(dummyStudent2)
    add_admin(dummyAdmin)

    #default skillConcept entries for database
    scratchSkillConcepts = [
        SkillConcept('Sequencing', 1, 'IF and WHEN you\'re ready to dive in, here\'s the place to start! Learn all about sequencing and how to take control of your program\'s flow!', 'R1C1', ['https://codeclubprojects.org/en-GB/scratch/rock-band/', 'https://scratchtutorials.com/tutorials/animate-your-name-using-colors'], False),
        SkillConcept('Repitition', 2, 'Well done, well done, well done. Let\'s learn about repitition!', 'R1C2', ['https://codeclubprojects.org/en-GB/scratch/lost-in-space/', 'https://scratch.mit.edu/projects/89696985/'],
                     False),
        SkillConcept('Variables', 3, 'What\'s a variable, you say? Let\'s get to the bottom of this by busting some ghosts!' , 'R2C2', ['https://codeclubprojects.org/en-GB/scratch/ghostbusters/', 'https://scratch.mit.edu/projects/98831292/'], False),
        SkillConcept('Selection', 4, 'Build you\'re own chatbot to learn about selection!', 'R2C1', ['https://codeclubprojects.org/en-GB/scratch/chatbot/'], False),
        SkillConcept('Boolean Operators', 5, 'If(you == havingFun) then let\'s continue on and learn about boolean operators!', 'R3C1', ['https://codeclubprojects.org/en-GB/scratch/paint-box/', 'https://wiki.scratch.mit.edu/wiki/Boolean_Block'], False),
        SkillConcept('Data Structures', 6, 'Data WHAT?! Impress your friends and family by making you\'re very own clone of Snake!', 'R3C2', ['https://codeclubprojects.org/en-GB/scratch/memory/','https://www.goshdarngames.com/scratch-snake-tutorial/', 'https://scratch.mit.edu/projects/17457737/'], False),
        SkillConcept('Functions', 7, 'Let\'s dive right in and write some funky functions!', 'R4C2', ['https://codeclubprojects.org/en-GB/scratch/clone-wars/', 'https://codeclubprojects.org/en-GB/scratch/space-junk/', 'https://codeclubprojects.org/en-GB/scratch/catch-the-dots/'], False),
        SkillConcept('Project Management (Boss Mode)', 8, 'Welcome to the boss fight. WoW! Look how far you\'ve come!! You can do it!', 'R4C1', ['https://codeclubprojects.org/en-GB/scratch/binary-hero/'], False)]
    


    for newSkillConcept in scratchSkillConcepts:
        add_skill_concept(newSkillConcept);


if __name__ == '__main__':
    clean_db()
    populate_db()
    app.run()
