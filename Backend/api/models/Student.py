# Student.py

# Programming For All
# Author: Gabriel Fabian, 2017

from Person import *
from Skill import *

class Student(Person):

	def __init__(self, first, last, id, age, email, skills=None):
		Person.__init__(self, first, last, id, email)
		self.age = age
		self.skills = skills