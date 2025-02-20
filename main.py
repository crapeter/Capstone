import pandas as pd
import column_names as col
import os
from dotenv import load_dotenv
load_dotenv()

'''
f1_
'''
grader_preferences = pd.read_excel(os.getenv('FILE1')).dropna(how="all")
'''
f2_
iloc[1:] is used to skip the first row, which is a dummy row that is not needed.
'''
grader_info = pd.read_excel(os.getenv('FILE2')).dropna(how="all").iloc[1:].reset_index(drop=True)
'''
f3_
'''
classes = pd.read_excel(os.getenv('FILE3')).dropna(how="all")

def format_courses_taught(courses: str) -> list[str]:
    return [course.strip() for course in courses.split("\n") if course.strip()]

def print_preferences():
    for idx, row in grader_preferences.iterrows():
       print(f"idx: {idx}, Grader: {row[col.f1_grader_name]}, Advisor: {row[col.f1_advisor]}, Course Preferences: {row[col.f1_course_pref]}")

def print_info():
    for idx, row in grader_info.iterrows():
        print(f"idx: {idx}, Grader: {row[col.f2_grader_name]}, Class Times: {row[col.f2_class_times]}, Courses: {row[col.f2_grader_courses]}, Taught Courses: {format_courses_taught(row[col.f2_taught_courses])}, Notes: {row[col.f2_notes]}")

def print_classes():
    for idx, row in classes.iterrows():
        print(f"idx: {idx}, Class: {row[col.f3_crn]}, Department: {row[col.f3_department]}, Course Name: {row[col.f3_course_title]}, Days: {row[col.f3_days]}, Time: {row[col.f3_times]}")

if __name__ == "__main__":
    print_preferences()
    print()
    print_info()
    print()
    print_classes()