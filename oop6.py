#Example of single inheritance
class employee1():
    def __init__(self, name, age, salary):  
        self.name = name
        self.age = age
        self.salary = salary
 
class childemployee(employee1):
    def __init__(self, name, age, salary,id):
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id
emp1 = employee1('harshit',22,1000)
 
print(emp1.age)