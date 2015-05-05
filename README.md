Date: 4/4/15
Author: Karen MacPherson

This script was made to be a quick way for teachers and/or professors to drop a number of the lowest grades at the end of the semester because they are merciful. The script will clear the cells with the dropped grade, and then update the student's total score for the semester as well as the total possible score. 

First argument is the input file. It needs to be tab delimited and in a certain format (template coming soon). Num is the number of grades you want dropped.

> python dropGrades.py 'inputfile.csv' num

It will run with any number of students and any number of assignments as long as the format is correct. It will create a comma delimited file called output.csv that can go straight back into Excel or Numbers. 