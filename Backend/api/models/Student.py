# Student.py

# Programming For All
# Author: Gabriel Fabian, 2017

from .Person import *
from .Skill import *

class Student(Person):

	def __init__(self, first, last, id, age, email, skills):
		Person.__init__(self, first, last, id, email)
		self.age = age
		if(skills != None):
			self.skills = skills
		else:	#Default skills
			skill1 = Skill("HTML", "www.linkToTheTree.com", None, 0)
			skill2 = Skill("Python", "www.linkToTheTree.com", None, 0)
			skill3 = Skill("CSS", "www.linkToTheTree.com", None, 0)
		self.skills = [skill1,skill2,skill3]