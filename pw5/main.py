import curses
import zipfile
import os
from input import stucount,inputmarks,inputstuinfo,inputcourseinfo,coucount,calgpa
from output import displaystuinfo,displaymark,displaycouinfo,gpasorting
scr=curses.initscr()
curses.start_color()
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
                scr.refresh()"
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
                file_list = ['student.txt', 'course.txt', 'marks.txt']
                with zipfile.ZipFile('student.dat', 'w') as new_zip:
                    for file_name in file_list:
                        new_zip.write(file_name)
                    for file_name in file_list:
                        os.remove(file_name)
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
            file_list = ['students.txt', 'courses.txt', 'marks.txt']
            with zipfile.ZipFile('student.dat', 'w') as new_zip:
                for file_name in file_list:
                    new_zip.write(file_name)
                for file_name in file_list:
                    os.remove(file_name)
            exit()

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
#file compressing
scr.addstr("We gonna stop the program now!")
file_list = ['student.txt', 'course.txt', 'marks.txt']
with zipfile.ZipFile('student.dat', 'w') as new_zip:
                         for file_name in file_list:
                             new_zip.write(file_name)
                         for file_name in file_list:
                             os.remove(file_name)
exit()

main()
