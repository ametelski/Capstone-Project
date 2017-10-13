# Skill.py

# Programming For All
# Author: Gabriel Fabian, 2017

from .SkillConcept import *
import json

class Skill():

	defaultSkillConcepts = [SkillConcept("Repetition", "to help kids with...", "R1C2", ["www.link1.com", "www.link2.com"],False), \
							SkillConcept("Condition", "to help kids with...", "R2C1", ["www.link1.com", "www.link2.com"], False), \
							SkillConcept("Procedural", "to help kids with...", "R2C3", ["www.link1.com", "www.link2.com"], False)]

	def __init__(self, skillName, skillUrl, skillConcepts=defaultSkillConcepts, skillConceptsCompleted=0):
		self.skillName = skillName
		self.skillUrl = skillUrl
		self.skillConcepts = skillConcepts
		self.skillConceptsCompleted = skillConceptsCompleted