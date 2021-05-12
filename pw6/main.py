import curses
import zipfile
from zipfile import ZipFile
import os
from input import *
from output import  *
import pickle
scr=curses.initscr()
curses.start_color()

#main
def main() :
        scr.refresh()
        scr.clear()
        scr.addstr("MENU: 1.input student and course information   2.exit\n")
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
            scr.addstr("exiting!")
            curses.napms(3000)
            curses.endwin()

            exit()


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


#file compressing
        scr.addstr("there ain't nothing to do with this program.")
        scr.addstr("we gonna pick something!")
        stupick=open("student.dat","ab")
        for stu in students:
            pickle.dump(stu,stupick)
        for cou in courses:
            pickle.dump(cou,stupick)
        for mak in marksinfo:
            pickle.dump(mak,stupick)
            break

main()
