# SkillConcept.py

# Programming For All
# Author: Gabriel Fabian, 2017


from .ExtLearnLink import *

class SkillConcept():

	def __init__(self, skillTitle, skillDescription, location, extLearnLinks=None, completed=False):
		self.skillTitle = skillTitle
		self.skillDescription = skillDescription
		self.extLearnLinks = extLearnLinks 
		self.completed = completed  
		self.location = location