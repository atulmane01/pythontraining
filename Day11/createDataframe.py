'''
1.How to Create a Data Frame:
    Pandas DataFrame is a 2-dimensional labeled data structure with columns of potentially different types. It is
    generally the most commonly used pandas object.
    Pandas DataFrame can be created in multiple ways. Let’s discuss different ways to create a DataFrame one by one.
'''
# Method #1: Creating Pandas DataFrame from lists of lists.
# Import pandas library
import pandas as pd

# initialize list of lists
data = [['tom', 10], ['nick', 15], ['juli', 14]]

# Create the pandas DataFrame
df = pd.DataFrame(data, columns = ['Name', 'Age'])

# print dataframe.
print(df)

'''
# Method #2: Creating DataFrame from dict of narray/lists:
To create DataFrame from dict of narray/list, all the narray must be of same length. 
If index is passed then the length index should be equal to the length of arrays. 
If no index is passed, then by default, index will be range(n) where n is the array length.
'''



# initialize data of lists.
data = {'Name': ['Tom', 'nick', 'krish', 'jack'],
        'Age': [20, 21, 19, 18]}

# Create DataFrame
df = pd.DataFrame(data)

# Print the output.
print(df)


'''
Method #3: Creates a indexes DataFrame using arrays.:
'''
import pandas as pd
# initialize data of lists.
data = {'Name': ['Tom', 'Jack', 'nick', 'juli'],
        'marks': [99, 98, 95, 90]}

# Creates pandas DataFrame.
df = pd.DataFrame(data, index=['rank1',
                               'rank2',
                               'rank3',
                               'rank4'])

# print the data
print(df)

'''
Method #4: Creating Dataframe from list of dicts
Pandas DataFrame can be created by passing lists of dictionaries as a input data. By default dictionary keys taken as columns.

'''

import pandas as pd

# Initialize data to lists.
data = [{'a': 1, 'b': 2, 'c': 3},
        {'a': 10, 'b': 20, 'c': 30}]

# Creates DataFrame.
df = pd.DataFrame(data)

# Print the data
print(df)

