import sys

inp = sys.argv[1]
dropNum = int(sys.argv[2])

#Student data structure that will hold all info associated with a student (or row in datasheet)
class Student(object):
	def __init__(self, info, gradeslist, topPoints):
		self.info = info
		self.grades = map(int, gradeslist[0:-2])
		self.total = int(gradeslist[-2])
		self.possible = int(gradeslist[-1])
		self.gradespercent = [float(a)/float(b) for a, b in zip(self.grades, topPoints)]
		#self.ave = float(self.total)/float(self.possible)




# A min function that will only evaluate the floats (this is to avoid evaluating None or empty strings)
def mymin(array):
	minimum = 1.0
	for elem in array:
		if type(elem)==float:
			if elem<minimum:
				minimum = elem
	return minimum




#finds the index of the lowest percent grades in a student's gradesarray
#reduces total by that grade, and possible by that assignment's top points
#then replaces that grade with an empty string
def DropLowestAssignment(students, num, topPoints):
	for x in range(num):
		for student in students:
			lowindex = student.gradespercent.index(mymin(student.gradespercent))
			student.total -= student.grades[lowindex]
			student.possible -= topPoints[lowindex]
			student.grades[lowindex] = ''
			student.gradespercent[lowindex] = ''



#Inputing data from file into datatypes
rows = open(inp, 'r')

studentList = []
title = rows.readline().strip('\r\n')
temp = rows.readline().strip('\r\n').split(',')
topPoints = map(int, temp[4:-2])

for line in rows.readlines():
	linelist = line.strip('\r\n').split(',')
	studentList.append(Student(linelist[0:4], linelist[4:], topPoints))




#Calling main function to drop grades from the student list
#This function modifies the Student class and topPoints
DropLowestAssignment(studentList, dropNum, topPoints)



#writing results back to comma delimited file
fo = open('output.csv', 'w+')
fo.write(title+"\n")
fo.write(",".join(temp)+"\n")
for student in studentList:
	fo.write(",".join(student.info)+',')
	fo.write(",".join(map(str, student.grades))+',')
	fo.write(str(student.total)+',')
	fo.write(str(student.possible)+'\n')
fo.close()




