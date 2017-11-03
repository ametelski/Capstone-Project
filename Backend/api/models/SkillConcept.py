# SkillConcept.py

# Programming For All
# Author: Gabriel Fabian, 2017


from .ExtLearnLink import *

class SkillConcept():

	def __init__(self, skillConceptName, skillConceptId, skillDescription, location, extLearnLinks=None, completed=False):
		self.skillConceptName = skillConceptName
		self.skillConceptId = skillConceptId
		self.skillDescription = skillDescription
		self.extLearnLinks = extLearnLinks or []
		self.completed = completed
		self.location = location