'''Python program to demonstrate single inheritance'''

#Parent class or Base Class
class Person(object):
	def __init__(self, name, id):
		self.name=name
		self.id=id

	def info(self):
		print(self.name)
		print(self.id)
	
	def print(self):
		print("My name is {} and my id number is {}". format(self.name, self.id))

#Child class or Deived class
class Student(Person):
	def __init__(self, name, id, std):
		self.std=std
		Person.__init__(self, name, id) # invoking __init__ of Parent class

	def print(self):
		print("My name is {} and my id number is {} and I am in {} standard". format(self.name, self.id, self.std))

	
std1= Student('Malan', 20, 10)
std2= Student('Pritee', 12, 10)

# calling method of Person class using Derived class object
std1.info()
# calling method of overrided function of Person class
std1.print()
std2.print()

		

		