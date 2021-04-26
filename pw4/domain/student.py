
students=[]
studentID=[]
stuname=[]
studob=[]

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
