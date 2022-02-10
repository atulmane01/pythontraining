'''

1. What is object:
    The object is an entity that has a state and behavior associated with it. It may be any real-world object
    like a mouse, keyboard, chair, table, pen, etc. Integers, strings, floating-point numbers, even arrays, and dictionaries,
    are all objects. More specifically,
    any single integer or any single string is an object.


'''

class Abc:

    def add(self,a,b):
        c=a+b
        print(c)
s=Abc()
s.add(2,3)
