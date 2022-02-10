# Created a Class
from re import A


class Program:
	# Created Parameterized Constructor
	def _init_(self, f, s):
		self.first = f
		self.second = s	
	# Funcion to Swap Variables
	def calculate(self):
		self.first , self.second= self.second , self.first

	#Function to Display Variables
	def display(self):
		print("Swapped Variable F: " + str(self.first))
		print("Swapped Variable S: " + str(self.second))
		
	
# creating object of the class this will invoke parameterized constructor with user input
obj = Program(input("Enter Variable F: "),input("Enter Variable S: "))

# Perform Swap
obj.calculate()

# display result
obj.display()