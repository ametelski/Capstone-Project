# Person.py

# Programming For All
# Author: Gabriel Fabian, 2017

class Person():

	def __init__(self, first, last, id):
		self.firstName = first
		self.lastName = last
		self.id = id

	def __str__(self):
		return "First Name: {}, Last Name: {}, ID: {}".format(self.firstName, self.lastName, self.id)