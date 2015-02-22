import scraper
import csv

class Categories_To_CSV(object):
	
	def __init__(self, category_dictionary):
		""" 
		initalize with dictionary from scraper.py
		"""
		self.category_dictionary = category_dictionary
	
	def put_categories_into_file(self):
		""" 
		logic that puts the contents of dictionary
		to rows and columns
		"""

def main():
	category_object = Categories_To_CSV(coursera_categories_dictionary)
	category_file_object = category_object.put_categories_into_file()

if __name__ == '__main__':
	main()