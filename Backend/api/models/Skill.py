# Skill.py

# Programming For All
# Author: Gabriel Fabian, 2017

from SkillConcept import *

class Skill():

	def __init__(self, skillName, skillUrl, skillConcepts, skillConceptsCompleted=0):
		self.skillName = skillName
		self.skillUrl = skillUrl
		self.skillConceptsCompleted = skillConceptsCompleted
		self.skillConcepts = skillConcepts

	def __str__(self):
		return "Skill name: {}, Skill Url: {}, Skill Concepts Completed: {}, Skill Concepts: {}".format(self.skillName, self.skillUrl, self.skillConceptsCompleted, self.skillConcepts)