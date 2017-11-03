# Skill.py

# Programming For All
# Author: Gabriel Fabian, 2017

from .SkillConcept import *
import json

class Skill():

	defaultSkillConceptIds = [1,2,3]

	def __init__(self, skillName, skillUrl, skillConceptsIds=defaultSkillConceptIds, skillConceptsCompleted=[1,2]):
		self.skillName = skillName
		self.skillUrl = skillUrl
		self.skillConceptsIds = skillConceptsIds
		self.skillConceptsCompleted = skillConceptsCompleted