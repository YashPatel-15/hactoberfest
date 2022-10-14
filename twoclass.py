class Employee:						#create class “employee”
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def employee_details(self):				#define function
        print('Name is ' ,self.name)
        print('Age is ',self.age)
class Qualification:					#create class “Qualification”
    def __init__(self,degree,college):
        self.degree=degree
        self.college=college
    def qualification_details(self):
        print('Name of degree',self.degree)
        print('Name of college',self.college)
class Scientist(Employee,Qualification):
    def __init__(self,name,age,degree,college):
        Employee.__init__(self,name,age)
        Qualification.__init__(self,degree,college)
        print("Scientist's Details:-")
class Manager(Employee,Qualification):
    def __init__(self,name,age,degree,college):
        Employee.__init__(self,name,age)
        Qualification.__init__(self,degree,college)
        print('Manager\'s deatils:-')

s1=Scientist('keval',20,'PHD','Oxford University')
s1.employee_details()
s1.qualification_details()

m1=Manager('Herry',35,'MBA','Parul university')
m1.employee_details()
m1.qualification_details()
