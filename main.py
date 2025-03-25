# from pprint import pprint
from data import Data
from assign import Assign
import column_names as col

'''
This is the main function, it's where the program will run
This will eventually be an endpoint for the web app (probably using Flask), but before that we need to make sure that the program works as expected.
'''
def main():
	data = Data()
	# assign = Assign(data)
	'''Uncomment out once the functions are implemented'''
	# assign.create_graph()
	# assignments = assign.assign_ta_graders()

	# assignments.to_excel('name_tbd.xlsx', index=False)

if __name__ == "__main__":
	main()