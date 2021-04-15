#inputfuncs
def inputStucount():
    scount=int(input("How many student we have?"))
    return scount
def inputCoursecount():
    ccount=int(input("How many course we have"))
    return ccount

def inputStuinfo():
    print("Enter student infor:")
    id=input("ID:")
    name=input("name:")
    dob=input("DoB:")
    stu={"id":id,"name":name,"DoB":dob}
    return stu
def inputCourseinfo():
    print("enter course infor:")
    cid=input("course id is:")
    cname=input("course name is:")
    c={"Cid":cid,"Cname":cname}
    return c
def marksinput():
    slcid=input("enter a course's id:")
    for i in range(len(course)):
        if course[i].get("Cid")==slcid:
            cif = course[i].get("Cname")
            mar={"Course":cif,"Students and marks":[]}
            print("The name of this course is:"+course[i].get("Cname")+"\n")
            for j in range(len(students)):
                    mark=float(input("enter mark of "+students[j].get("name")+":"))
                    sif=students[j].get("name")
                    mar["Students and marks"].append((sif,mark))
            return mar
#displayfuncs
def Stusprint():
    print("The list of student is:")
    print("\n".join(map(str,students)))
def Cprint():
    print("The list of course is")
    print("\n".join(map(str,course)))
def marksprint():
    print("choose a course")
    for i in range (len(marks)):
        print(marks[i]['id'],marks[i]["cid"],marks[i][marks])
def showmarks():
    choice=input("Which course that you want to choose ?")
    for i in range(len(marks)):
        if marks[i].get("Course")== choice:
            print(marks[i])


#main
scount=inputStucount()
students=[]
marks=[]
for i in range(0,scount):
    s=inputStuinfo()
    students+=[s]
    print("\n")
ccount=inputCoursecount()
course=[]
for i in range(0,ccount):
    c=inputCourseinfo()
    course+=[c]
    print("\n")
Stusprint()
Cprint()
print("please enter marks of this student in this course.")
inp='yes'
mk=marksinput()
marks+=[mk]
showmarks()



