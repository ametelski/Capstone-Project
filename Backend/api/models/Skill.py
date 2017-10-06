# Skill.py

# Programming For All
# Author: Gabriel Fabian, 2017

from .SkillConcept import *

class Skill():

	def __init__(self, skillName, skillUrl, skillConcepts, skillConceptsCompleted):
		self.skillName = skillName
		self.skillUrl = skillUrl
		self.skillConceptsCompleted = skillConceptsCompleted
		if skillConcepts != None:
			self.skillConcepts = skillConcepts
		#Default concepts
		else:
			skillConcept1 = SkillConcept("Repetition", "to help kids with...", "R1C2",
										 ["www.link1.com", "www.link2.com"],False)
			skillConcept2 = SkillConcept("Condition", "to help kids with...", "R2C1",
										 ["www.link1.com", "www.link2.com"], False)
			skillConcept3 = SkillConcept("Procedural", "to help kids with...", "R2C3",
										 ["www.link1.com", "www.link2.com"], False)
			self.skillConcepts = [skillConcept1, skillConcept2, skillConcept3]

	def __str__(self):
		return "Skill name: {}, Skill Url: {}, Skill Concepts Completed: {}, Skill Concepts: {}".format(self.skillName, self.skillUrl, self.skillConceptsCompleted, self.skillConcepts)