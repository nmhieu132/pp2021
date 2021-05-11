import curses
import zipfile
from zipfile import ZipFile
import os
from input import stucount,inputmarks,inputstuinfo,inputcourseinfo,coucount,calgpa
from output import  displaymark,displaystuinfo,displaycouinfo,gpasorting
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
            flist = ['students.txt', 'courses.txt', 'marks.txt']
            with zipfile.ZipFile('student.dat', 'w') as newz:
                for fname in flist:
                    newz.write(fname)
                for fname in flist:
                    os.remove(fname)
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
        scr.addstr("1.Compress then exit  2.Exit immediately")
        compr=int(scr.getstr())
        if compr==1:
            flist = ['students.txt', 'courses.txt', 'marks.txt']
            with zipfile.ZipFile('student.dat', 'w') as newz:
                for fname in flist:
                    newz.write(fname)
                for fname in flist:
                    os.remove(fname)
        else:
            exit()

        scr.addstr("1.Decompress and load file 2.exit")
        decom=int(scr.getstr())
        if decom==1:
            if os.path.isfile('students.dat'):
                scr.addstr("This file students.dat exits \n")
                zipf = ZipFile('students.dat', 'r')
                zipf.extractall()
                if os.path.isfile('Students.txt'):
                    f = open('Students.txt', 'r')
                    f.readline()
                if os.path.isfile('Courses.txt'):
                    f = open('Courses.txt', 'r')
                    f.readline()
                if os.path.isfile('Marks.txt'):
                    f = open('Marks.txt', 'r')
                    f.readline()
main()
