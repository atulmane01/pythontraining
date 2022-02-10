'''
Class Method:
	n Python, the @classmethod decorator is used to declare a method in the class as a class method that can be called using
	ClassName.MethodName().
	The class method can also be called using an object of the class.
    Syntax:

    @classmethod
       def fun(cls, arg1, arg2, ...):
    Where,

    fun: the function that needs to be converted into a class method
    returns: a class method for function.
    classmethod() methods are bound to a class rather than an object. Class methods can be called by both class and object.
    These methods can be called with a class or with an object


'''


# Exapmle:

class student:
    counter = 0

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

        student.counter = student.counter + 1

    def msg(self):
        print(self.name + " got" + self.marks, "%")

    @classmethod
    def object_count(cls):
        return cls.counter


s1 = student("sia", "93")
s2 = student("sia", "93")

print(student.object_count())

'''
Though classmethod and staticmethod are quite similar, there's a slight difference in usage for both entities: 
classmethod must have a reference to a class object as 
the first parameter, whereas staticmethod can have no parameters at all
    
2. What is the usage of class method:

Uses of classmethod() function are used in factory 
design patterns where we want to call many functions with the class name rather than an object

'''