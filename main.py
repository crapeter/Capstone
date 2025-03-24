# from pprint import pprint
from data import Data
from assign import Assign
import column_names as col

'''
This is the main function, it's where the program will run
'''
def main():
	data = Data()
	assign = Assign(data)
	'''Uncomment out once the functions are implemented'''
	# assign.create_graph() # TODO: implement this function in assign.py
	# assignments = assign.assign_ta_graders() # TODO: implement this function in assign.py

	# assignments.to_excel('name_tbd.xlsx', index=False)

if __name__ == "__main__":
	main()