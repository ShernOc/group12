# 2. 1-to-Many Relationship: Department and Employees
# Scenario: A department can have multiple employees, but each employee belongs to one department.
# Create Department and Employee classes.
# Implement methods in Department to add and remove employees.
# Include attributes such as name and id for Employee and department_name for Department.

# Task: Write a function to list all employees in a department and one to transfer an employee to another department.

#Multiple employers 

#Department class 
class Department: 
    empl_list = []
    def __init__(self, department_name):
        self.department_name = department_name
    
    #method add  
    def add_employees(self,employee):
        self.employee = []
        self.employee.append(employee)

    #method remove 
    def remove_employees(self, employee):
        self.employee.remove(employee)
        
    #created a class method
    def list_of_all_employees(cls, employees):
        
    

#Class employee 
class Employee: 
    def __init__(self, name, id):
        self.name = name 
        self.id = id 
        
         
#Object 
d = Department("Human Resource")

#Object 
emp1 = Employee("Maria", 45)
emp5 = Employee("Kimbo",2 )

#connect department with 




    