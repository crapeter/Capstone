# from pprint import pprint
import pandas as pd
import column_names as col
import os
from dotenv import load_dotenv
load_dotenv()

class Data:
	def __init__(self):
		self.FILE1 = col.idx1
		self.FILE2 = col.idx2
		self.FILE3 = col.idx3

		# f1_
		self.general_info = pd.read_excel(os.getenv('FILE1')).dropna(how="all")

		# f2_, iloc[1:] is used to skip the first row, which is a dummy row that is not needed.
		self.grader_info = pd.read_excel(os.getenv('FILE2'), sheet_name=None)
		self.ta_grader_avail = self.grader_info['TAgraderAvail'].dropna(how="all").iloc[1:].reset_index(drop=True)
		self.ta_grader_preferred_courses = self.grader_info['TA grader preferred courses'].dropna(how="all").iloc[1:].reset_index(drop=True)
		self.special_request_from_courses = self.grader_info['special request from courses'].dropna(how="all").iloc[1:].reset_index(drop=True)

		# f3_
		self.classes = pd.read_excel(os.getenv('FILE3')).dropna(how="all")

		# split courses into undergrad and grad courses, !!! to access data via a list, use .values.tolist() !!!
		self.undergrad_courses, self.grad_courses = self.split_courses(self.classes)

		# splits the students between masters and phd, !!! to access data via a list, use .values.tolist() !!!
		# masters students are required to take 20 hours, compared to phd which is between 10 and 20 inclusive
		self.masters_students, self.phd_students = self.split_grader_info(self.ta_grader_avail, self.general_info)

	# This function uses boolean masking to split the courses into undergrad and grad courses. Undergrad courses are courses with a course number less than 5000. Grad courses are courses with a course number greater than or equal to 5000.
	def split_courses(self, courses):
		u_courses = courses[courses[col.f3_course_number] // 1000 < 5]
		g_courses = courses[courses[col.f3_course_number] // 1000 >= 5]
		return u_courses, g_courses

	# This function uses boolean masking to split the grader info into graders and TA's. Graders are students who have the word 'grader' in their notes. TA's are students who do not have the word 'grader' in their notes.
	def split_grader_info(self, gr_info, g_info):
		general_filter = g_info[col.f1_advisor].isna() | (g_info[col.f1_advisor].str.strip() == '')
		return gr_info.loc[general_filter], gr_info.loc[~general_filter]
