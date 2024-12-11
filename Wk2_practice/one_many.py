# 2. 1-to-Many Relationship: Department and Employees

#Class employee 
class Employee: 
    def __init__(self, name, id):
        self.name = name 
        self.id = id
      
# Class Department 
class Department: 
    def __init__(self, department_name):
        self.department_name = department_name
    
        #Where we will store/append name of employees
        self.employee_list = [] 

   
    #instance method that is going to add employees to the employee_list 
    def add_employees(self,employee):
        # if employee in self.employee_list:
            self.employee_list.append(employee)

    #instance method that removes employees from the list 
    def remove_employees(self,employee):
        if employee in self.employee_list: 
            self.employee_list.remove(employee)
        else: 
            print(f"{self.department_name} department does not have {employee.name} in the department")
    
    # transfer employee to another department 
    def transfer_employer(self, employee, transferred_department ):
        if employee in self.employee_list:
            #take the removed employee. add them to 
            self.remove_employees(employee)
            transferred_department.add_employees(employee)
            
            print(f"{employee.name} has been transferred to {transferred_department.department_name}")
        else: 
            print(f"{employee.name} is not in {self.department_name}")

    # methods that shows/print the all-list all employees
    def show_list(self):
        # print(self.employee_list)
        # # if self.department_name:
        # #     print([employee for employee in self.employee_list ])
        
        #or
        print(f"{self.department_name}",[{employee.name, employee.id} for employee in self.employee_list])
        
        # print(f"Employees in {self.department_name}:{self.employee_list}")
            

#Department object 
human_resource = Department("HumanResource")
finance = Department("Finance")


#Employee Object
employee1 = Employee("Maria", 45)# hr 
employee2 = Employee("James", 56) # hr
employee5 = Employee("Kamau",558) # finance 


# Calling the functions and we are going to pass employees. /object. 
#adding employees 
human_resource.add_employees(employee1)
human_resource.add_employees(employee2)
finance.add_employees(employee5)

#remove employers
#removing employee 2 from hr department 
human_resource.remove_employees(employee2)

finance.show_list()
human_resource.show_list()

# transfer 
# transfer employee5 to hr department
human_resource.transfer_employer(employee5,finance)

#show list 
finance.show_list()
human_resource.show_list()
   
