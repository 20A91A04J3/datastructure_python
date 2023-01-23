class personal:
    def __init__(self,name,phno,adhar,email):
        self.name=name
        self.phno=phno
        self.adhar=adhar
        self.email=email
    def display(self):
        print(self.name,self.phno,self.adhar,self.email)
    
class student(personal):
    def __init__(self,name,phno,adhar,email,rollno,branch,college):
        self.rollno=rollno
        self.branch=branch
        self.college=college
        super().__init__(name,phno,adhar,email)
    def display(self):
        print(self.rollno,self.branch,self.college)
        super().display()

s1=student('surya',7785648902,234567890,'20a91a04j3@aec.edu.in',123,'ECE','Aditya')
s1.display()


