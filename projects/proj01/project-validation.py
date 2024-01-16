
# Do NOT edit this file. Instead, just call it from the command line,
# using the instructions in the assignment notebook.

import sys
questions = sys.argv[1:]


valid_ids = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13']
break_flag = False
invalid_ids = []
for question in questions:
    if question != 'all' and question not in valid_ids:
        invalid_ids.append(question)

if len(invalid_ids) > 0:
    print(str(invalid_ids) + ' is/are not a valid question number(s). The possible question numbers are ' + str(valid_ids) + '.')
    sys.exit()

# Initialize Otter
import otter
grader = otter.Notebook("project.ipynb")

# %load_ext autoreload
# %autoreload 2

import pandas as pd
import numpy as np
from pathlib import Path

import plotly.express as px
import plotly.io as pio
pio.renderers.default = "plotly_mimetype+notebook"

from project import *

grades_fp = Path('data') / 'grades.csv'
grades = pd.read_csv(grades_fp)
grades.head()

if 'q1' in questions or questions == [] or 'all' in questions:
    print(grader.check("q1"))

if 'q2' in questions or questions == [] or 'all' in questions:
    print(grader.check("q2"))

if 'q3' in questions or questions == [] or 'all' in questions:
    print(grader.check("q3"))

if 'q4' in questions or questions == [] or 'all' in questions:
    print(grader.check("q4"))

if 'q5' in questions or questions == [] or 'all' in questions:
    print(grader.check("q5"))

if 'q6' in questions or questions == [] or 'all' in questions:
    print(grader.check("q6"))

if 'q7' in questions or questions == [] or 'all' in questions:
    print(grader.check("q7"))

final_breakdown_fp = Path('data') / 'final_exam_breakdown.csv'
final_breakdown = pd.read_csv(final_breakdown_fp)
final_breakdown.head()

final_breakdown.shape

grades.loc[grades['PID'] == 'A99381181', 'Final']

if 'q8' in questions or questions == [] or 'all' in questions:
    print(grader.check("q8"))

grades_combined = combine_grades(grades, raw_redemption(final_breakdown, [1, 2, 3, 7, 9, 12]))
grades_combined.head()

if 'q9' in questions or questions == [] or 'all' in questions:
    print(grader.check("q9"))

if 'q10' in questions or questions == [] or 'all' in questions:
    print(grader.check("q10"))

grades_analysis = grades_combined.assign(**{
    'Total Points Pre-Redemption': total_points(grades_combined),
    'Letter Grade Pre-Redemption': final_grades(total_points(grades_combined)),
    'Total Points Post-Redemption': total_points_post_redemption(grades_combined),
    'Letter Grade Post-Redemption': final_grades(total_points_post_redemption(grades_combined))
})
grades_analysis.head()

grades_analysis['Section'].nunique()

grades_analysis['Section'].unique()

if 'q11' in questions or questions == [] or 'all' in questions:
    print(grader.check("q11"))

if 'q12' in questions or questions == [] or 'all' in questions:
    print(grader.check("q12"))

# Run this cell to see the result, and don't change this cell --- it is needed for the tests.
fig = letter_grade_heat_map(grades_analysis)
# fig.show()

if 'q13' in questions or questions == [] or 'all' in questions:
    print(grader.check("q13"))


