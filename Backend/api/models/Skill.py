# Skill.py

# Programming For All
# Author: Gabriel Fabian, 2017

from .SkillConcept import *
import json

class Skill():

	defaultSkillConcepts = defaultSkillConcepts = [
        SkillConcept('Repetition', 1, 'to help kids with...', 'R1C2', ['www.link1.com', 'www.link2.com'], False),
        SkillConcept('Condition', 2, 'Student Has COMPLETED this MODULE...', 'R2C1', ['www.link1.com', 'www.link2.com'],
                     False),
        SkillConcept('Procedural', 3, 'to help kids with...', 'R2C3', ['www.link1.com', 'www.link2.com'], False)]

	def __init__(self, name, url, skillConcepts=defaultSkillConcepts, completedPercentage=0):
		self.name = name
		self.url = url
		self.skillConcepts = skillConcepts
		self.completedPercentage = completedPercentage