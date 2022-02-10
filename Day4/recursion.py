'''
1.What is recursion:
    The term Recursion can be defined as the process of defining something in terms of itself. In simple words, it is a process in which a function calls itself directly or indirectly.
    A complicated function can be split down into smaller sub-problems utilizing recursion.

    The process in which a function calls itself directly or indirectly is called recursion
    and the corresponding function is called as recursive function
'''

#Without Recursion factorial of number

number = int(input("Enter a number: "))
factorial = 1
if number < 0:
   print(" Factorial does not exist for negative numbers")
elif number == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,number + 1):
       factorial = factorial*i
   print("The factorial of",number,"is",factorial)


#with Recursion factorial of number:

#
# def fact(n):
#     return 1 if (n == 1 or n == 0) else n * fact(n - 1);
#
# num = int(input("Enter The Number"))
# print("Factorial of", num, "is", )
# fact(num)