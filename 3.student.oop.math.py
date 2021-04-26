import math
import numpy as np
import curses
students=[]
studentID=[]
stuname=[]
studob=[]

courses=[]
courseID=[]
coursecres=[]
coursename=[]

marksinfo=[]
marks=[]
gpa=[]
#curses initializing
scr=curses.initscr()
curses.start_color()
#student
class student:
    def __init__(self,id,name,dob):
        self.id=id
        self.name=name
        self.dob=dob

    def getid(self):
        return self.id
    def getname(self):
        return self.name
    def getdob(self):
        return self.dob
#courses
class course:
    def __init__(self,cid,cname,credits):
        self.cid=cid
        self.cname=cname
        self.credits=credits

    def getcid(self):
        return self.cid
    def getcname(self):
        return self.cname
    def getcredits(self):
        return self.credits
#marks
class mark:
    def __init__(self,id,cid,mark,gpa=0):
        self.id=id
        self.cid=cid
        self.mark=mark
        self.gpa=gpa

    def getcid(self):
        return self.cid
    def getid(self):
        return self.id
    def getmark(self):
        return self.mark
    def getgpa(self):
        return self.gpa
    def setgpa(self):
        self.gpa=gpa
#student count
def stucount():
    scr.addstr("How many students we have?")
    scr.refresh()
    numos=int(scr.getstr().decode())
    if numos <= 0:
        curses.init_pair(1,curses.COLOR_BLACK,curses.COLOR_WHITE)
        scr.addstr("Wrong number!\n",curses.color_pair(1))
        scr.refresh()
        curses.napms(10000)
        scr.clear()
        scr.refresh()
    else:
        return numos
#course count
def coucount():
    scr.addstr("How many courses that we have?")
    scr.refresh()
    numoc=int(scr.getstr().decode())
    if numoc<=0:
        curses.init_pair(1,curses.COLOR_BLACK,curses.COLOR_WHITE)
        scr.addstr("Wrong number!\n",curses.color_pair(1))
        scr.refresh()
        scr.napms(10000)
        scr.clear()
        scr.refresh()
    else:
        return numoc
#input student's information
def inputstuinfo():
    scr.addstr("Enter ID of this student: ")
    scr.refresh()
    id=scr.getstr().decode()

    scr.addstr("Enter name of this student: ")
    scr.refresh()
    name=scr.getstr().decode()

    scr.addstr("Enter dob of this student: ")
    scr.refresh()
    dob=scr.getstr().decode()

    stu=student(id,name,dob)
    students.append(stu)
    studentID.append(id)
    stuname.append(name)
    scr.refresh()
    scr.clear()
#input courses information
def inputcourseinfo():
    scr.addstr("Enter ID of this course: ")
    scr.refresh()
    cid=scr.getstr().decode()

    scr.addstr(("Enter name of this course: "))
    scr.refresh()
    cname=scr.getstr().decode()

    scr.addstr("How many credits for this course?: ")
    scr.refresh()
    credits=float(scr.getstr().decode())

    cou=course(cid,cname,credits)
    courses.append(cou)
    courseID.append(cid)
    coursename.append(cname)
    coursecres.append(credits)
    scr.refresh()
    scr.clear()
#input marks for students
def inputmarks():
    scr.addstr("Lets choose a course! ")
    cid=(scr.getstr().decode())
    scr.refresh()
    if cid in courseID:
        scr.addstr("Enter ID of who deserve this mark: ")
        id=scr.getstr().decode()
        scr.refresh()
        if id in studentID:
            scr.addstr("Enter mark of this student(positve number that smaller than 20): ")
            mar = math.floor(float(scr.getstr().decode()))
        else:
            exit()
    else:
        exit()
    marks.append(mar)
    m_ark=mark(id, cid, mar)
    marksinfo.append(m_ark)
#calculate gpa
def calgpa():
    rawmark=np.array(marks)
    crepersub=np.array(coursecres)
    scr.addstr("Enter a student ID: ")
    id=scr.getstr().decode()
    if id in studentID:
        for i in range(len(marksinfo)):
            sumresult=np.sum(np.multiply(rawmark,crepersub))
            sumcre=np.sum(crepersub)
            scr.refresh()
            _gpa=sumresult/sumcre
            scr.refresh()
    else:
        return 0
    gpa.append(_gpa)
    scr.refresh()
    for m in marksinfo:
        scr.clear()
        scr.refresh()
        scr.addstr("ID and mark: %s    GPA: %s\n" % (m.getid(), _gpa))
        scr.refresh()
        break
#display student's information
def displaystuinfo():
    scr.addstr("this is the list of student: \n")
    scr.refresh()
    for stu in students:
        scr.addstr("student's name: %s   student's ID: %s   student's dob: %s" %(stu.getname(),stu.getid(),stu.getdob()))
        scr.refresh()
#display courses's information
def displaycouinfo():
    scr.addstr("this is the list of all course: \n")
    scr.refresh()
    for cou in courses:
        scr.addstr(" course's name: %s    course's ID: %s    number of credits : %s" %(cou.getcname(), cou.getcid(), cou.getcredits()))
        scr.refresh()
#display marks
def displaymark():
    for ma in marksinfo:
        scr.addstr("student's ID   course's ID: %s   : %s mark: %s" %(ma.getid(),ma.getcid(),ma.getmark))
        scr.refresh()
#gpa sorting
def gpasorting():
    somark=np.array(gpa)
    somark[::-1].sort()
    scr.addstr("After sorting,the list of gpa is:%s"%(somark))
    scr.refresh()
#main
def main() :
        scr.refresh()
        scr.clear()
        scr.addstr("MENU: 1.input student information  2.input course information  3.exit\n")
        scr.addstr("Enter your choice: ")
        scr.refresh()
        choice1 = int(scr.getstr().decode())
        if choice1==1:
            nums=stucount()
            scr.clear()
            scr.refresh()
            for i in range(nums):
                scr.addstr(f"student {i+1}\n")
                inputstuinfo()
                scr.refresh()
            numoc=coucount()
            scr.refresh()
            scr.clear()
            for i in range(numoc):
                scr.addstr(f"course {i+1}\n")
                inputcourseinfo()
                scr.refresh()
                scr.clear()
                inputmarks()
                scr.refresh()
                break

        elif choice1==2:
            numoc=coucount()
            scr.refresh()
            scr.clear()
            for i in range(numoc):
                scr.addstr(f"course {i + 1}\n")
                inputcourseinfo()
                scr.refresh()
                nums=int(stucount())
                scr.refresh()
                scr.clear()
                for i in range(nums):
                    scr.addstr(f"student {i+1}\n")
                    inputstuinfo()
                    scr.refresh()
                    scr.clear()
                    inputmarks()
                    scr.refresh()
                    scr.clear()
                break
        elif choice1==3:
            scr.addstr("exiting!")
            curses.napms(3000)
            curses.endwin()

        while True:
            scr.addstr("Calculation gpa:\n")
            calgpa()
            curses.napms(1000)
            scr.clear()
            scr.refresh()
            scr.addstr("list Course:\n")
            displaycouinfo()
            curses.napms(1000)
            scr.clear()
            scr.refresh()
            scr.addstr("list Student:\n")
            displaystuinfo()
            curses.napms(1000)
            scr.clear()
            scr.refresh()
            scr.addstr("list mark:\n")
            displaymark()
            curses.napms(1000)
            scr.clear()
            scr.refresh()
            scr.addstr("gpa sort:\n")
            gpasorting()
            curses.napms(1000)

            break
main()







