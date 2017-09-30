# ExtLearnLink.py

# Programming For All
# Author: Gabriel Fabian, 2017

class ExtLearnLink():

	def __init__(self, shortName, url):
		self.shortName = shortName
		self.url = url


	def __str__(self):
		return "Short Name: {}, Url: {}".format(self.shortName, self.url)