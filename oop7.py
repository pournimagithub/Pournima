#Example of Multilevel inheritance
class employee():
    def __init__(self,name,age,salary):  
        self.name = name
        self.age = age
        self.salary = salary
class childemployee1(employee):
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
 
class childemployee2(childemployee1):
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
emp1 = employee('harshit',22,1000)
emp2 = childemployee1('arjun',23,2000)
 
print(emp1.age)
print(emp2.age)