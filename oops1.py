class Student:
    college='Aditya'
    def __init__(self,r,n):
        self.rollno=r
        self.name=n
        self.college='AEC'
    def display(self):
        print(self.rollno,self.name,Student.college)
    @classmethod
    def classMethod(cls):
        print(cls.college)
    @staticmethod
    def iseven(num):
        if num%2:
            print('odd')
        else:
            print('even')
s=Student(123,'Mouni')
s.display()
s.classMethod()
s.iseven(100)

    
