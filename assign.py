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

# from pprint import pprint
import pandas as pd
import column_names as col

# get hours: (course_num % 1000) // 100

class Assign:
	pass