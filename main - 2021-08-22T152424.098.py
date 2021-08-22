class Person:
	def __init__(self,name, age):
		self.name=name
		delf.age=age

	def myfunc(self):
			print("Helo my name is"+self.name)

p1=Person("John", 36)
p1.myfunc()

#Parent class is the class being inherited from, also called base class.
#Child class is the class that inherits from another class, also called derived class.

class Person:
	def__init__(self, faname,lname):
		self.firstname=fname
		delf.lasname=lname

def printname(self):
	print(self.firstname, self.lastname)

x=Person("John","Doe")
x.printname()

#Creaing a child class
class Student(Person):
	pass
		def __init__(self, fname, lname):
			super().__init__(fname, lname)
			self.graduationyear=year
	def welcome(self):
		print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
    Person.__init__(self, fname, lname)