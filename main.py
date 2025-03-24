'''
Basic rules:
	1.	For graduate courses, it is strongly encouraged to select PhD students.
	2.	Faculty may prefer their own PhD students or research students to be their TA/graders.
	3.	Avoid the overlapping of your class time and students' class time.
	4.	TA/grader can NOT be TA of their spring 2025 registered course.
	5.	For a TA/grader, we prefer not to assign more than two courses.
	6.	For one course, we prefer not to assign more than two TA/graders.

Output:
	1. Needs to be an excel file
	2. The excel file should have the columns: Course Number, Section Number (1 or 2), Instructor, Assignment (TA/grader), Course Title, Days, Times, BUilding, Room Number
'''

from pprint import pprint
import pandas as pd
import column_names as col
from data import Data

# TODO: get this to work
'''
This is the main function, it's where the program will run
'''
def main():
	data = Data()
	print(data.ta_grader_avail.iloc[0].tolist())
	print(data.ta_grader_preferred_courses.iloc[0].tolist())
	print(data.special_request_from_courses.iloc[0].tolist())

if __name__ == "__main__":
	main()