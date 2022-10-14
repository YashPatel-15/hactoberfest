class Employee:
    def __init__(self, employee_id, employee_name, employee_designation, employee_salary):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.employee_designation = employee_designation
        self.employee_salary = employee_salary
    								# inc_sal function
    def inc_sal(self):
        if self.employee_designation == "Manager":
            salary = self.employee_salary + 5000
            return salary
        elif self.employee_designation == "General Manager":
            salary = self.employee_salary + 10000
            return salary
        elif self.employee_designation == "CEO":
            salary = self.employee_salary + 20000
            return salary
        elif self.employee_designation == "worker":
            salary = self.employee_salary + 2000
            return salary
# taking_input
e_id = int(input("Enter the Employee ID : "))
e_name = input("Enter the Employee Name : ")
e_designation = input("Enter the Employee Designation : ")
e_salary = int(input("Enter the Employee Salary : "))
# creating obj of Employee class
emp_obj = Employee(e_id, e_name, e_designation, e_salary)
# getting access of inc_sal function
salary = emp_obj.inc_sal()
print("Incremental Employee Salary is : ", salary)
# another way
print("Incremental Employee Salary is : %d" % salary)
