'''
Instance Variable And Instance Method


1.What is instance variable and what is instance method:

    1.instance variable:

    Instance variables are used within the instance method. We use the instance method to perform a set of actions on the
    data/value provided by the instance variable.

    We can access the instance variable using the object and dot (.) operator.

    2.instance method:
        instance method are the methods which act as upon instance variable of the class .instance method need to know the memory address
        of the instance which is provided throgh self variable by default as first parameter for the instance method

        syntax:

        def method_name(self):
            fucntion body

         def method_name(self,f1,f2):
            fucntion body

'''


# class student:
#     def __init__(self,name,age):
#         self.name=name                      #instance variables
#         self.age=age
#     def msg(self):                          #instance method
#         print(self.name+" " +self.age)
# print("object 1")
#
# s1=student("abc","20")
# print(s1.name)
# print(s1.age)
# s1.msg()
# print("object 2")#
#
# s2=student("xyz","22")
# print(s1.name)
# print(s1.age)
# s2.msg()





'''
2.In how many ways we can declare an instance variable:
    There are two ways to access the instance variable of class:
        1. by using self and object reference.
        2.Using getattr() method
         '''
# 1.Within the class by using self and object reference.

# class student:
#
#     # constructor
#     def __init__(self, name, rollno):
#         # instance variable
#         self.name = name
#         self.rollno = rollno
#     def display(self):
#         # using self to access
#         # variable inside class
#         print("hello my name is:", self.name)
#         print("my roll number is:", self.rollno)
#
# # object created
# s = student('HARRY', 1001)
# # function call through object
# s.display()
# # accessing variable from
# # outside the class
# print(s.name)

#ASK FOR THIS
# 2.Using getattr() method

# class emp:
#     name = 'Harsh'
#     salary = '25000'
#
#     def show(self):
#         print(self.name)
#         print(self.salary)
#
#
# # Driver Code
# e1 = emp()
# # Use getattr instead of e1.name
# print(getattr(e1, 'name'))
#
# # returns true if object has attribute
# print(hasattr(e1, 'name'))
#
# # sets an attribute
# setattr(e1, 'height', 152)
#
# # returns the value of attribute name height
# print(getattr(e1, 'height'))
#
# # delete the attribute
# delattr(emp, 'salary')








'''
4. How to initialize instance variables with different values:
    We can modify the value of the instance variable and assign a new value to it using the object reference.
'''
#Example :

# class Student:
#     # constructor
#     def __init__(self, name, age):
#         # Instance variable
#         self.name = name
#         self.age = age
#
# # create object
# stud = Student("Jessa", 20)
#
# print('Before')
# print('Name:', stud.name, 'Age:', stud.age)
#
# # modify instance variable
# stud.name = 'shri'
# stud.age = 15
#
# print('After')
# print('Name:', stud.name, 'Age:', stud.age)








'''
5.How to access an instance variable outside the class:

    we can access instance variable with using object_name.variable_name
    
'''

# Example:

# class Mobile:
#             def __init__(self):
#
#                 self.model="Realme X"              #instace Variable
#             def show_model(self):                  #instce Method
#                 print(self.model)                  #accesing instance varible
# realme= Mobile()
# realme.show_model()
# print(realme.model)                                #Accesing instance varible from outside class


'''
6. How to access instance variables inside an instance method :
    To accesss instance variable we need instance method with self as an fisrt parameter 
    then we can access instance varible using self.variable_name
'''
# Example

class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age
    # instance method access instance variable
    def show(self):
        print('Name:', stud.name, 'Age:', stud.age)
# create object
stud = Student("Jessa", 20)
# call instance method
stud.show()