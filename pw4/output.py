import curses
import  numpy as  np


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