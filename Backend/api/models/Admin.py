# Admin.py

# Programming For All
# Author: Gabriel Fabian, 2017

from Person import *

class Admin(Person):

	def __init__(self, first, last, id, role):
		Person.__init__(self, first, last, id)
		self.role = role