# needed to read the csv file
import csv
import sys

filename = sys.argv[1][:len(sys.argv[1])-4]

# reading the csv file
with open(filename+".csv","r") as csvfile:
    reader = csv.reader(csvfile)
    
    # a dictionary in which the keys are the student names and the values
    # are lists of grades given by their peers
    students_grades = {}
    for student in reader:
        name = student[0]
        grade = student[1]
        if name not in students_grades.keys():
            students_grades[name] = [grade]
        else:
            students_grades[name].append(grade)
    #print students_grades

    # a list of student names
    students = students_grades.keys()
    #print students
    
    try:
        if (sys.argv[2] == "members"):
            # a dictionary in which the keys are the student names
            # and the values are the numbers of grades given
            #number_of_group_members = {}
            with open(filename+"_members.csv","wb") as members_file:
                wr = csv.writer(members_file, quoting=csv.QUOTE_ALL)
                for student in students:
                    members = 0
                    for grade in students_grades[student]:
                        members+=1
                    #number_of_group_members[student] = members
                    student_members = [student, members]
                    wr.writerow(student_members)
    except:
        print("Please type 'members' or 'averages' after the filename")

    try:
        if (sys.argv[2] == "averages"):
            #students_average_grades = {}
            with open(filename+"_averages.csv","wb") as averages_file:
                wr = csv.writer(averages_file, quoting=csv.QUOTE_ALL)
                for student in students:
                    grades = map(int,students_grades[student])
                    average = reduce(lambda x, y: x + y, grades) / float(len(grades))
                    #students_average_grades[student] = average
                    student_average = [student, average]
                    wr.writerow(student_average)
    except:
        print("Please type 'members' or 'averages' after the filename")
