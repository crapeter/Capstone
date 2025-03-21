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
import os
from dotenv import load_dotenv
load_dotenv()

class Data:
    def __init__(self):
        self.FILE1 = col.idx1
        self.FILE2 = col.idx2
        self.FILE3 = col.idx3

        # f1_
        self.grader_preferences = pd.read_excel(os.getenv('FILE1')).dropna(how="all")

        # f2_, iloc[1:] is used to skip the first row, which is a dummy row that is not needed.
        self.grader_info = pd.read_excel(os.getenv('FILE2')).dropna(how="all").iloc[1:].reset_index(drop=True)

        # f3_
        self.classes = pd.read_excel(os.getenv('FILE3')).dropna(how="all")

        # split courses into undergrad and grad courses, !!! to access data via a list, use .values.tolist() !!!
        self.undergrad_courses, self.grad_courses = self.split_courses(self.classes)

        # splits the students between graders and TA's, !!! to access data via a list, use .values.tolist() !!!
        self.graders_only, self.TAs = self.split_grader_info(self.grader_info)

    # Functions used to print information about the excel files and variables. These are used for debugging purposes.
    # ------------------------------------------------------------------------------------------------ #
    def print_preferences(self):
        for idx, row in self.grader_preferences.iterrows():
            print(f"idx: {idx}, Grader: {row[col.f1_grader_name]}, Advisor: {row[col.f1_advisor]}, Course Preferences: {row[col.f1_course_pref]}")

    def print_info(self):
        for idx, row in self.grader_info.iterrows():
            print(f"idx: {idx}, Grader: {row[col.f2_grader_name]}, Class Times: {row[col.f2_class_times]}, Courses: {row[col.f2_grader_courses]}, Taught Courses: {self.format_courses_taught(row[col.f2_taught_courses])}, Notes: {row[col.f2_notes]}")

    def print_classes(self):
        for idx, row in self.classes.iterrows():
            print(f"idx: {idx}, Class: {row[col.f3_crn]}, Department: {row[col.f3_department]}, Course Name: {row[col.f3_course_title]}, Days: {row[col.f3_days]}, Time: {row[col.f3_times]}")

    def print_graders_only(self):
        pprint([s[self.FILE2.get(col.f2_grader_name)] for s in self.graders_only.values.tolist()])

    def print_tas_only(self):
        pprint([s[self.FILE2.get(col.f2_grader_name)] for s in self.TAs.values.tolist()])

    def format_courses_taught(courses: str) -> list[str]:
        return [course.strip() for course in courses.split("\n") if course.strip()]
    # ------------------------------------------------------------------------------------------------ #

    # This function uses boolean masking to split the courses into undergrad and grad courses. Undergrad courses are courses with a course number less than 5000. Grad courses are courses with a course number greater than or equal to 5000.
    def split_courses(self, courses):
        u_courses = courses[courses[col.f3_course_number] // 1000 < 5]
        g_courses = courses[courses[col.f3_course_number] // 1000 >= 5]
        return u_courses, g_courses

    # This function uses boolean masking to split the grader info into graders and TA's. Graders are students who have the word 'grader' in their notes. TA's are students who do not have the word 'grader' in their notes.
    def split_grader_info(self, g_info):
        filtered = g_info[col.f2_notes].str.fullmatch('grader', case=False, na=False)
        return g_info.loc[filtered], g_info.loc[~filtered]


if __name__ == "__main__":
    data = Data()
    for uc in data.undergrad_courses.values.tolist():
        print(f"Course Title: {uc[data.FILE3.get(col.f3_course_title)]}\nCourse Instructor: {uc[data.FILE3.get(col.f3_instructor)]}\n")
