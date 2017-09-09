# run.py

# Programming For All
# Author: Gabriel Fabian, 2017

from models.Person import *
from models.Admin import *
from models.Student import *
from pymongo import MongoClient
import json

def get_db():
    client = MongoClient('localhost:27017')
    db = client.ProgrammingForAll
    return db

def add_student(db, student):
    db.countries.insert({"name" : "Canada"})

def add_admin(db, admin):
    db.countries.insert({"name" : "Canada"})
    
def get_country(db):
    return db.countries.find_one()

if __name__ == "__main__":

	dummyStudent = Student("Charlie", "Foo", 1, 12)
	dummyAdmin = Admin("Melissa", "Bar", 2, "Admin")

	print json.dumps(dummyAdmin.__dict__)

	print dummyStudent

    #db = get_db() 
    #add_country(db)
    #print get_country(db)