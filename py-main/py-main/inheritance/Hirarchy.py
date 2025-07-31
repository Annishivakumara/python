class Person:

    def setPersondetails(self, name, age):
        self.name=name
        self.age=age

    def getPersondetails(self):
        print(f"name:-{self.name} and Age:- {self.age}")

class Student(Person):

    def setstudentDetails(self,student_id, course):
        self.student_id=student_id
        self.course=course

    def getstudentdetails(self):
        self.getPersondetails()
        print(f"Student id:- {self.student_id} and Course :-{self.course}")
class faculty(Student):

    def setfacultydeatils(self,name,age):
        self.name=name
        self.age=age

    def getfacultydetails(self):
        print(f"faculty  name:-{self.name} and {self.age}")
        
fac=faculty()


fac.setstudentDetails("1CSE", "Python")
fac.setfacultydeatils("Blessed", 30)

print("Details")
fac.getPersondetails()
fac.getstudentdetails()
fac.getfacultydetails()
