
#smallest of three numbers
# numbers=[10,15,5,24,45]
# numbers.sort()
# rev=numbers
# #used indexing
# print("Smallest element is:", rev[:3])
# print(numbers)


a=input()
b=input()
c=input()

if (a < b) and (a < c) :
    print(a, "is the smallest of three numbers.")
if (b < a) and (b < c):
    print(b, "is the smallest of three numbers.")
if c < a and c < b:
    print(c, "is the smallest of three numbers.")


