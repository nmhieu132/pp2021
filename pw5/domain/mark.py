
marksinfo=[]
marks=[]
gpa=[]
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