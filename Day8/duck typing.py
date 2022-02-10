'''
Duck Typing:
    Duck Typing is a type system used in dynamic languages. For example, Python, Perl, Ruby, PHP, Javascript, etc.
    where the type or the class of an object is less important than the method it defines. Using Duck Typing, we do not check types at all.
    Instead, we check for the presence of a given method or attribute.



'''

# Example

# Python program to demonstrate
# duck typing

class  Duck:
	def walk(self):
		print("Thapak Thapak")

class Horse:
	def walk(self):
		print("Tabadak tabkda")


def myfun(obj):
	obj.walk()


d=Duck()
myfun(d)

H=Horse()
myfun(H)