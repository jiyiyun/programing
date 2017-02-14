#Class 
__metaclass__ = type

class Person:
	def __init__(self,name):
		self.name = name

	def getName(self):
		return self.name

	def color(self,color):
		print("%s is %s " %(self.name ,color))


girl1 = Person('maria')
print(girl1.name)
print(girl1.color)