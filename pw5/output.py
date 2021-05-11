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
    for stu_d in students:
        scr.addstr("student's name: %s   student's ID: %s   student's dob: %s" %(stu_d.getname(),stu_d.getid(),stu_d.getdob()))
        scr.refresh()
#display courses's information
def displaycouinfo():
    scr.addstr("this is the list of all course: \n")
    scr.refresh()
    for cou_r in courses:
        scr.addstr(" course's name: %s    course's ID: %s    number of credits : %s" %(cou_r.getcname(), cou_r.getcid(), cou_r.getcredits()))
        scr.refresh()
#display marks
def displaymark():
    for ma_k in marksinfo:
        scr.addstr("student's ID   course's ID: %s   : %s mark: %s" %(ma_k.getid(),ma_k.getcid(),ma_k.getmark))
        scr.refresh()
#gpa sorting
def gpasorting():
    somark=np.array(gpa)
    somark[::-1].sort()
    scr.addstr("After sorting,the list of gpa is:%s"%(somark))
    scr.refresh()