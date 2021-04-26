import curses
import  math
import  numpy as  np
from pw4.domain.student import student
from pw4.domain.course import course
from  pw4.domain.mark import mark

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

scr=curses.initscr()
curses.start_color()
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
