class student:
    def __init__(self,name,corect,tries):
        self.name=name
        self.corect=corect
        self.tries=tries
    def printe(self):
        print(self.name+" "+str(self.corect)+' '+str(self.tries))
students=[]
for _ in range(int(input())):
    name=input()
    scored,submit=map(int,input().split())
    students.append(student(name,scored,submit))
students.sort(key=lambda x:(-x.corect,x.tries))
for studen in students:
    studen.printe()