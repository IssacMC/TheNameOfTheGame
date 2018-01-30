class Weapon:
	def __str__(self):
		return self.name

class Person:
	def __init__(self, name,age,foods):
		self.name = name
		self.age = age
		self.foods = foods
	def __str__(self):
		return "Name: " +self.name\
			+" Age: " + str(self.age)\
			+" Favorite food: " +str(self.foods[0])
	def birth_year():
		return 2015 - age

class Rock(Weapon):
	def __init__(self):
		self.name = "Rock"
		self.desc = "A rock for hitting things"
		self.damage = 5

class Dagger(Weapon):
	def __init__(self):
		self.name = "Dagger"
		self.desc = "A dagger for stabbing things"
		self.damage = 10

class RustySword(Weapon):
	def __init__(self):
		self.name = "Rusty sword"
		self.desc = "A sword for slashing things"
		self.damage = 20

name = input("Please enter your name: ")
age = input("Please enter your age: ")
try:
	print("You were born in {}.".format(2015-int(age)))
except ValueError:
	print("Unable to calculate the year you were born, "\
		+ '"{}" is not a number.'.format(age))


	
		










