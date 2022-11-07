#Simon Gelber - CSC365 Lab 1
#School Search

import sys

#Student class containing each student's information
class Student:

    def __init__(self, lastname, firstname, grade,
                 classroom, bus, gpa, teacherlname, teacherfname):
        self.lName = lastname

        self.fName = firstname

        self.grade = grade

        self.classroom = classroom

        self.bus = bus

        self.gpa = gpa

        self.teacherlName = teacherlname

        self.teacherfName = teacherfname

#student command
def command_S(studentList, command):
    if len(command) == 2:
        for student in studentList:
            if student.lName == command[1]:
                print("Student: %s, %s, %d, %d | Teacher: %s, %s" % (student.lName,student.fName,
                      int(student.grade),int(student.classroom),student.teacherlName,student.teacherfName))
    elif len(command) == 3 and (command[2] == 'B' or command[2] == "Bus"):
        for student in studentList:
            if student.lName == command[1]:
                print("Student: %s, %s | Bus Route: %d" % (student.lName,student.fName,
                      int(student.bus)))
    else:
        print("Invalid command.")

#teacher command
def command_T(studentList, command):
    if len(command) == 2:
        for student in studentList:
            if student.teacherlName == command[1]:
                print("Student: %s, %s | Teacher: %s, %s" % (student.lName,student.fName,student.teacherlName,student.teacherfName))
    else:
        print("Invalid command.")

#bus command
def command_B(studentList, command):
    if len(command) == 2:
        for student in studentList:
            if student.bus == command[1]:
                print("Student: %s, %s, %d, %d" % (student.lName,student.fName,int(student.grade),int(student.classroom)))
    else:
        print("Invalid command.")


#grade command
def command_G(studentList, command):
    emptyflag = 0
    if len(command) == 2:
        for student in studentList:
            if student.grade == command[1]:
                print("Student: %s, %s" % (student.lName,student.fName))
                emptyflag = 1
        if emptyflag == 0:
            print("There are Zero students in grade %s" % command[1])
    elif len(command) == 3 and (command[2] == 'H' or command[2] == "High"):
        max = []
        for student in studentList:
            if student.grade == command[1]:
                if len(max) == 0:
                    max.append(student)
                else:
                    if float(student.gpa) > float(max[0].gpa):
                        max[0] = student
        if len(max) == 0:
            print("There are Zero students in grade %s" % command[1])
        else:
            print("Student with Highest GPA: %s, %s, %4.2f, %s, %s, %d" % (max[0].lName, max[0].fName,
                float(max[0].gpa),max[0].teacherlName,max[0].teacherfName, int(max[0].bus)))

    elif len(command) == 3 and (command[2] == 'L' or command[2] == "Low"):
        min = []
        for student in studentList:
            if student.grade == command[1]:
                if len(min) == 0:
                    min.append(student)
                else:
                    if float(student.gpa) < float(min[0].gpa):
                        min[0] = student
        if len(min) == 0:
            print("There are Zero students in grade %s" % command[1])
        else:
            print("Student with Lowest GPA: %s, %s, %4.2f, %s, %s, %d" % (min[0].lName, min[0].fName,
                float(min[0].gpa),min[0].teacherlName,min[0].teacherfName, int(min[0].bus)))

    else:
        print("Invalid command.")

#average command
def command_A(studentList, command):
    gpa_list = []
    if len(command) == 2:
        for student in studentList:
            if student.grade == command[1]:
                gpa_list.append(float(student.gpa))
        if len(gpa_list) == 0:
            print("There are zero students in grade %s" % command[1])
        else:
            average = sum(gpa_list)/len(gpa_list)
            print("Grade: %d Average GPA: %4.2f" % (int(command[1]), average))

    else:
        print("Invalid command.")

#info command
def command_I(studentList, command):
    if len(command) == 1:
        for i in range(0,7):
            count = 0
            for student in studentList:
                if int(student.grade) == i:
                    count += 1
            print("%d: %d" % (i,count))
    else:
        print("Invalid command.")

#process user input
def parseInput(studentList):
    i = input("> ")
    while(1):
        commands = i.split(" ")
        if commands[0] == "S:" or commands[0] == "Student:":
            command_S(studentList, commands)
        elif commands[0] == "T:" or commands[0] == "Teacher:":
            command_T(studentList, commands)
        elif commands[0] == "B:" or commands[0] == "Bus:":
            command_B(studentList, commands)
        elif commands[0] == "G:" or commands[0] == "Grade:":
            command_G(studentList, commands)
        elif commands[0] == "A:" or commands[0] == "Average:":
            command_A(studentList, commands)
        elif commands[0] == "I" or commands[0] == "Info":
            command_I(studentList, commands)
        elif commands[0] == "Q" or commands[0] == "Quit":
            break
        else:
            print("Invalid Command.")


        i = input("> ")


def main(argv):
    studentList = []
    try:
        file = open(argv[1], "r")
    except OSError:
        print("Could not open file: ", argv[1])
        sys.exit()
    else:
        studentline = file.readline()
        while studentline:
            studentline = studentline.strip()
            student = studentline.split(",")
            if len(student) != 8:
                print("File format invalid...Incorrect number of columns. Exiting.")
                file.close()
                sys.exit()
            studentList.append(Student(student[0],student[1],student[2], student[3],student[4],student[5], student[6],student[7]))
            studentline = file.readline()
        parseInput(studentList)
        file.close()










if __name__ == "__main__":
    main(sys.argv)