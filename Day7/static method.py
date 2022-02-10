'''
Static Method:
    Static methods, much like class methods, are methods that are bound to a class rather than its object.
    They do not require a class instance creation. So, they are not dependent on the state of the object.
    They can be called both by the class and its object.

    Syntax:
    	@staticmethod
    	def method_name():
    		method body


'''

# Example:

class Add:
	@staticmethod
	def disply(a,b):
		c=a+b
		print("addition is =",c)
add=Add()
Add.disply(10,20)


