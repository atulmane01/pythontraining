'''
1.Why we use deep copy instead of shallow Completed copy:

    Shallow Copy reflects changes made to the new/copied object in the original object.
     Deep copy doesn't reflect changes made to the new/copied object in the original object
     . ... Deep copy stores the copy of the original
    object and recursively copies the objects as well. Shallow copy is faster

'''
# Example:

# import copy
# old_list=[[0,1,2],[4,6,7],[7,2,7]]
#
# new_list=copy.copy(old_list)
#
# new_list[0]=[8,3,5]
#
# print(old_list)
# print(new_list)



# import copy
#
# old_list=[[0,1,2],[4,6,7],[7,2,7]]
# new_list=copy.deepcopy(old_list)
# new_list[0]=[8,3,5]
# print(old_list)
# print(new_list)

