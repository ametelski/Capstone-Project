# Student.py

# Programming For All
# Author: Gabriel Fabian, 2017

from Person import *

class Student(Person):

	def __init__(self, first, last, id, age):
		Person.__init__(self, first, last, id)
		self.age = age