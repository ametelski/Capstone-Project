# Person.py

# Programming For All
# Author: Gabriel Fabian, 2017

import json
import bson.json_util

class Person():

	def __init__(self, first, last, id, email):
		self.firstName = first
		self.lastName = last
		self.id = id
		self.email = email