# Admin.py

# Programming For All
# Author: Gabriel Fabian, 2017

from .Person import *

class Admin(Person):

	def __init__(self, first, last, id, role, email):
		Person.__init__(self, first, last, id, email)
		self.role = role