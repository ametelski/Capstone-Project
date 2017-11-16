# Student.py

# Programming For All
# Author: Gabriel Fabian, 2017

from .Person import *
from .Skill import *

class Student(Person):
	defaultSkills = [Skill("HTML", "www.linkToTheTree.com"), \
					Skill("Python", "www.linkToTheTree.com"), \
					Skill("CSS", "www.linkToTheTree.com"), \
					Skill("Scratch", "\\scratchTree")
					]

	def __init__(self, first, last, id, age, email, skillConceptsCompleted=[], skills=["HTML, Python, CSS, Scratch"]):
		Person.__init__(self, first, last, id, email)
		self.age = age
		self.skillConceptsCompleted = skillConceptsCompleted
		self.skills = skills