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
import networkx as nx
import column_names as col

'''
This class will be where the sorting algorithms will be implemented, following the restraints at the top of this file.
It will take in the data from the Data class and output the sorted data.
The sorted data will be stored in a pandas dataframe.
The sorted data will be stored in an excel file.
The excel file will be named 'name_tbd.xlsx'.
'''
class Assign:
	# get hours: (course_num % 1000) // 100
	def __init__(self, data):
		self.data = data
		self.graph = nx.Graph()

	# TODO: implement this function to check if the assignment is viable, following the rules at the top of this file.
	def is_viable(self, ta, course):
		return True

	def create_graph(self):
		# Add nodes for TAs/graders, bipartite=0
		for _, ta in self.data.ta_grader_avail.iterrows():
			self.graph.add_node(ta[col.s1_grader_name], bipartite=0)  

		# Add nodes for courses with their section numbers as unique identifiers, bipartite=1
		for _, course in self.data.grad_courses.iterrows():
			course_id = f"{course[col.f3_course_number]}-{course[col.f3_section_number]}"
			self.graph.add_node(course_id, bipartite=1)  

		# Add edges between TAs/graders and courses if the assignment is viable
		for _, ta in self.data.ta_grader_avail.iterrows():
			for _, course in self.data.grad_courses.iterrows():
				course_id = f"{course[col.f3_course_number]}-{course[col.f3_section_number]}"
				if self.is_viable(ta, course):
					self.graph.add_edge(ta[col.s1_grader_name], course_id)

	def assign_ta_graders(self):
		matching = nx.bipartite.maximum_matching(self.graph)

		# Convert matching to a list of assignments
		assignments = []
		for ta, course in matching.items():
			if ta in self.data.ta_grader_avail[col.s1_grader_name].values:
				course_number, section_number = course.split('-')
				course_info = self.data.grad_courses[
					(self.data.grad_courses[col.f3_course_number] == int(course_number)) &
					(self.data.grad_courses[col.f3_section_number] == int(section_number))
				].iloc[0]
				assignments.append({
					'Course Number': course,
					'Section Number': course_info[col.f3_section_number],
					'Instructor': course_info[col.f3_instructor],
					'Assignment': ta,
					'Course Title': course_info[col.f3_course_title],
					'Days': course_info[col.f3_days],
					'Times': course_info[col.f3_times],
					'Building': course_info[col.f3_building],
					'Room Number': course_info[col.f3_room_number]
				})

		return pd.DataFrame(assignments)