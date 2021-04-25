students=[]
studentID=[]
courses=[]
coursesID=[]
Mark=[]
#student
class student:
    def __init__(self,id,name,dob):
        self.id=id
        self.name=name
        self.dob=dob
        students.append(self)
        studentID.append(self.id)
    def studentcount():
        numost=int(input("enter number of students"))
        if numost<0:
            print("there's no student!")
            return 0
        else:
            return numost
    def inputstuinfo():
        id = input("enter student's id for these student: ")
        name = input("enter name of these student: ")
        dob = input("enter day of birth of these student: ")
        student(id, name, dob)
    def stuinfo(self):
        print("id:",self.id,"name:",self.name,"dob:",self.dob)


#course
class course:
    def __init__(self,cid,name):
        self.cid=cid
        self.name=name
        courses.append(self)
        coursesID.append(self.cid)
    def coucount():
        numoc=int(input("enter number of courses!"))
        if numoc<0:
            print("theres no course!")
            return 0
        else:
            return numoc
    def inputcourseinfo():
        cid=input("enter the id of this course")
        name=input("enter the name of this course")
        course(cid,name)
    def cinfo(self):
        print("cid:",self.cid,"cname:",self.name)

#mark
class mark:
    def __init__(self,cid,id,marks):
        self.cid=cid
        self.id=id
        self.marks=marks
        Mark.append(self)

    def inputmarks():
        print("enter a course's id:")
        cid = input()
        if cid in coursesID:
            id=input(("enter a student's id:"))
            if id in studentID:
                marks=float(input("enter marks of this student!"))
                if marks<0:
                    print("error")
                    marks=float(input())
            else:
                print("this student does not exist")
                return 0
        else:
            print("this course does not exist")
            return 0
        mark(cid,id,marks)

    def printmark(self):
        print("courseID:", self.cid, "studentID:", self.id, "marks:", self.marks)
#display
class display:
    def displaystu():
        print("This is the list of students")
        for i in range(0,len(students)):
            print(student.stuinfo(students[i]))
    def displaycourse():
        print("This is the list of courses")
        for i in range(0,len(courses)):
            print(course.cinfo(courses[i]))
    def displaymark():
        print("This is what your kid get")
        for i in range(0,len(Mark)):
            print(mark.printmark(Mark[i]))
#main
    def svscmangement():
        print("Show the program what you want to do first:\n 1.input number and information of students 2.exit")
        choice1=int(input())
        if choice1==1:
            numost=student.studentcount()
            for i in range (numost):
                student.inputstuinfo()
            print("next what you want to do? 1.input number and information of courses 2.exit")
            nchoice1 = int(input())
            if nchoice1==1:
                numoc=course.coucount()
                for i in range(numoc):
                    course.inputcourseinfo()
                    nchoice2=int(input("want to add marks? 1:yes 2:no"))
                    if nchoice2==1:
                        mark.inputmarks()
                        display.displaystu()
                        display.displaycourse()
                        display.displaymark()
                        break
                    else:
                        exit()
            else:
                exit()
        else:
            exit()
display.svscmangement()


