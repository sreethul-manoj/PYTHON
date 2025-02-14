class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Employee:
    def __init__(self,emp_id,salary):
        self.emp_id=emp_id
        self.salary=salary
class Manager(person,Employee):
    def __init__(self,name,age,emp_id,salary,department):
        person.__init__(self,name,age)
        Employee.__init__(self,emp_id,salary)
        self.department=department
    def display(self):
        print(f"name :{self.name}")
        print(f"age :{self.age}")
        print(f"emp_id :{self.emp_id}")
        print(f"salary :{self.salary}")
        print(f"department:{self.department}")
m=Manager("aswani",27,11,1000000000,"python")
m.display()


