#Example of Hierarchical Inheritance
class employee():
    def __init__(self, name, age, salary):   
        self.name = name
        self.age = age
        self.salary = salary
 
class childemployee1(employee):
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
 
class childemployee2(employee):
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
emp1 = employee('harshit',22,1000)
emp2 = employee('arjun',23,2000)
 
print(emp1.age)
print(emp2.age)