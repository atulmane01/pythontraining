# List = [10, 20, 30, 40, 50, 60]
# print("original list ")
# print(List)
#
# # changing the first value
# List[0] = 11
#
# # changing the second value
# List[1] = 21
# print("after changing")
# print(List)



# 2concatenation of list

# test_list3 = [1, 4, 5, 6, 5]
# test_list4 = [3, 5, 7, 2, 5]
#
# # using + operator to concat
# test_list3 = test_list3 + test_list4
#
# # Printing concatenated list
# print ("Concatenated list using + : "+ str(test_list3))


# numbers = [2, 3, 5, 2, 11, 2, 7]
# # check the count of 2
# count = numbers.count(numbers)
# print('Count of 2:', count)

# create a list
# prime_numbers = [2, 3, 5]
# # create another list
# numbers = [1, 4]
# # add all elements of prime_numbers to numbers
# prime_numbers.extend(numbers)
# print('List after extend():', prime_numbers)
#


# cars = ['Ford', 'BMW', 'Volvo']
# cars.sort()
#
# print(cars)
#

# even_nums = []
# for x in range(21):
#     if x%2 == 0:
#         even_nums.append(x)
# print(even_nums)


# str = "HiIamATulhowareyou !"
# # accessing the character of str at 0th index
# print(str[0])
# # accessing the character of str at 6th index
# print(str[6])
# # accessing the character of str at 10th index
# print(str[10])

# str = "HiIamATulhowareyou!"
# # accessing the character of str at 0th index
# print(str[-1])
# # accessing the character of str at 6th index
# print(str[-5])
# # accessing the character of str at 10th index
# print(str[-10])

# str ="Hello Everyone!"
#
# print("Original String :-")
# print(str)
#
# # reversing the string using slicing
# print("Reverse String :-")
# print(str[: : -1])


# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
#
# set3 = set1.union(set2)
# print(set3)


# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
#
# set1.update(set2)
# print(set1)


# fruits = {"apple", "banana", "cherry"}
# x = fruits.copy()
# print(x)

#
# fruits = {"apple", "banana", "cherry"}
#
# fruits.pop()
#
# print(fruits)

# fruits = {"apple", "banana", "cherry"}
#
# fruits.discard("banana")
#
# print(fruits)


# dict = {'Name': 'Zara', 'Age': 7}
# print(dict.items())

# dict = {'Name': 'Zara', 'Age': 7}
# dict2 = {'Sex': 'female' }
# dict.update(dict2)
# print ("updated dict : ", dict)
#
#

# Union
# set Conacat
# set1 = {"a","b" ,"c"}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)
# print(set3)
#
#
# # update
# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
# set1.update(set2)
# print(set1)


# lst=["sravan",98,"harsha","jyothika","deepika",78, 90,"ramya"]
#
# print(lst)
#

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
# print(newlist)
#
#
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#
# newlist = [x for x in fruits if "a" in x]
#
# print(newlist)



# 1.Create List of Even Numbers with List Comprehension

myList = [5,2,8,9]
evensList = [x for x in myList if x % 2 == 0]
print(evensList)

def even(no):
    print( [x for x in range(no) if x%2==0])
even(100)


# 2.Some operation using Multiple if conditions.
#
list_1 = [-2, -1, 0, 1, 2, 3]
list_2 = [4, 5, 6, 7, 8]
list_3 = [ x * y for x in list_1 for y in list_2 if x > 0 if y % 2 == 0 ]
print(list_3)

#3.Checking the length of words in list using dict Comprehension

words=['this','that','is','if','that','is','if','this','that']
print({i:words.count(i) for i in words})

#4.Printing the square numbers from 1-30 using dict Comprehension

print({x:x**2 for x in range(1,31) })


list1 = [1, 5, 1, 1, 2]
total = lambda a :sum(list1),list1
print("Sum of all elements in given list: ", total)

