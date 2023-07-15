'''Python program to demonstrate multiple inheritance'''

#Parent 
class Vehicle:
	def __init__(self, efficiency, type ):
		self.eff=efficiency
		self.type=type

	def display_vehicle(self):
		print("Efficiency: {}".format(self.eff))
		print("Type : {}".format(self.type))

class Car:
	def __init__(self, mileage, performance ):
		self.mileage=mileage
		self.perf=performance

	def display_car(self):
		print("Mileage: {}".format(self.mileage))
		print("Performance : {}".format(self.perf))

class BMW(Vehicle, Car):
	def __init__(self,efficiency, type, mileage, performance, model, color):
		self.color=color
		self.model=model
		Vehicle.__init__(self, efficiency, type)
		Car.__init__(self, mileage, performance)

	def display(self):
		print("Model: {}".format(self.model))
		print("Color : {}".format(self.color))
		self.display_vehicle()
		self.display_car()

bmw= BMW(50, 'B', '29kmpl', 60, 'x1', 'black')
bmw.display()

