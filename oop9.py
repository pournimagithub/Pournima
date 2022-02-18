#Example of Multiple Inheritance
class employee1():
    def __init__(self, name, age, salary):  
        self.name = name
        self.age = age
        self.salary = salary
 
class employee2():
    def __init__(self,name,age,salary,id):
     self.name = name
     self.age = age
     self.salary = salary
     self.id = id
 
class childemployee(employee1,employee2):
    def __init__(self, name, age, salary,id):
     self.name = name
     self.age = age
     self.salary = salary
     self.id = id
emp1 = employee1('harshit',22,1000)
emp2 = employee2('arjun',23,2000,1234)
 
print(emp1.age)
print(emp2.id)