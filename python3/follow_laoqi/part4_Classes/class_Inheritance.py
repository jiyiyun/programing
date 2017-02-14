__metaclass__ = type

class Person:
	def speak(self):
		print "This speak is in class not inheritance"

	def setHeight(self):
		print "old calss 216 cm"

	def weight(self):
		print "weight is old class 60 kg"

class man(Person):
	def setHeight(self):
		print "The height is new 199,not father_class"

if __name__ == "__main__":
	jack = man()
	jack.setHeight()
	jack.speak()
	jack.weight()
