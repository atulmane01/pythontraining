'''

Methods In DataFrame:

 3.sum:
    Pandas dataframe.sum() function return the sum of the values for the requested axis
    
'''
# Example Use sum() function to find the sum of all the values over the index axis.:

# import pandas as pd
#
# # Creating the dataframe
# df = pd.read_csv("sample.csv")
# print(df.sum(axis = 0,skipna=True))
#
# #skipna : Exclude NA/null values when computing the result.
#
# # Use sum() function to find the sum of all the values over the column axis.
#
# # sum over the column axis.
# print(df.sum(axis = 1, skipna = True))


'''
4.  The drop() :
    method removes the specified row or column.
    By specifying the column axis (axis='columns'), the drop() method removes the specified column.
    By spcifying the row axis (axis='index'), the drop() method removes the specified row.
'''
# Example:
import pandas as pd

# data = {
#   "name": ["Sally", "Mary", "John"],
#   "age": [50, 40, 30],
#   "qualified": [True, False, False]
# }
#
# df = pd.DataFrame(data)
#
# newdf = df.drop("age", axis='columns')
#
# print(newdf)

'''
5.Mean:
    Return the average (mean) value for each column:
'''
# df = pd.DataFrame({"A":[12, 4, 5, 44, 1],
#                    "B":[5, 2, 54, 3, 2],
#                    "C":[20, 16, 7, None, 8],
#                    "D":[14, 3, 17, 2, 6]})

# print(df.mean(axis=0))

# df = pd.DataFrame({"A":[12, 4, 5, None, 1],
#                    "B":[7, 2, 54, 3, None],
#                    "C":[20, 16, 11, 3, 8],
#                    "D":[14, 3, None, 2, 6]})
# print(df.mean(axis=1,skipna=True))

'''
6.Max:
    The max() method returns a Series with the maximum value of each column.
    By specifying the column axis (axis='columns'), the max() method searches column-wise and returns the maximum value for each row.
'''
data = [[10, 18, 11], [13, 15, 8], [9, 20, 3]]

df = pd.DataFrame(data)
print(df)
print(df.max(axis=0))
print(df.max(axis=1))

'''
7.min:
    min() function returns the minimum of the values in the given object.
    
'''

print(df.min(axis = 0))
print(df.min(axis = 1))

'''
8.Describe:
    The describe() method returns description of the data in the DataFrame.

    If the DataFrame contains numerical data, the description contains these information for each column:
'''
print(df.describe())


'''
9.Shape:
    The shape property returns a tuple containing the shape of the DataFrame.
    The shape is the number of rows and columns of the DataFrame
'''
df = pd.read_csv('nba.csv')
print("Shape")
print(df.shape)