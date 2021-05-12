
courses=[]
courseID=[]
coursecres=[]
coursename=[]
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