# SkillConcept.py

# Programming For All
# Author: Gabriel Fabian, 2017


from .ExtLearnLink import *

class SkillConcept():

	def __init__(self, skillConceptName, id, description, location, extLearnLinks=None):
		self.skillConceptName = skillConceptName
		self.id = id
		self.description = description
		self.extLearnLinks = extLearnLinks or []
		self.location = location