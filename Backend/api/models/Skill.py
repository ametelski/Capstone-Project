# Skill.py

# Programming For All
# Author: Gabriel Fabian, 2017

from .SkillConcept import *
import json

class Skill():

	defaultSkillConcepts = [1,2,3]

	def __init__(self, skillName, skillUrl, skillConcepts=defaultSkillConcepts, skillConceptsCompleted=[1,2]):
		self.skillName = skillName
		self.skillUrl = skillUrl
		self.skillConcepts = skillConcepts
		self.skillConceptsCompleted = skillConceptsCompleted