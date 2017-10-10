# SkillConcept.py

# Programming For All
# Author: Gabriel Fabian, 2017


from .ExtLearnLink import *

class SkillConcept():

	def __init__(self, skillConceptName, skillDescription, location, extLearnLinks=None, completed=False):
		self.skillConceptName = skillConceptName
		self.skillDescription = skillDescription
		self.extLearnLinks = extLearnLinks or []
		self.completed = completed
		self.location = location