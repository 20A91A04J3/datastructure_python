class personal:
    def __init__(self,name,email,adhar,phno):
        self.name=name
        self.email=email
        self.adhar=adhar
        self.phno=phno
    def display(self):
        print(self.name,self.email,self.adhar,self.phno)
class student(personal):
    def __init__(self,name,email,adhar,phno,rollno,branch,college):
        self.rollno=rollno
        self.branch=branch
        self.college=college
        super().__init__(name,email,adhar,phno)
    def display(self):
        print(self.rollno,self.branch,self.college)
        super().display()
class employee(personal):
    def __init__(self,name,email,adhar,phno,idno,salary,dept):
        self.idno=idno
        self.salary=salary
        self.dept=dept
        super().__init__(name,email,adhar,phno)
    def display(self):
        super().display()
        print(self.idno,self.salary,self.dept)
        

s1=employee('mouni','20a91a04j3@aec.edu.in',6078456789,4567890345,4567,1000,'manager')
s2=student('mouni','20a91a04j3@aec.edu.in',6078456789,4567890345,1234,'ECE','Aditya')
s2.display()
s1.display()
