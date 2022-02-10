'''
Operations that can be performed on a DataFrame are:


    Creating a DataFrame
    Dealing with Rows and Columns
    Indexing and Selecting Data
    Iterating over rows and columns


'''
'''
1.Creating a DataFrame:
    

'''

# import pandas as pd
# import pandas as pd
#
# # list of strings
# lst = ['Geeks', 'For', 'Geeks', 'is',
#        'portal', 'for', 'Geeks']
#
# # Calling DataFrame constructor on list
# df = pd.DataFrame(lst)
# print(df)
'''
2.Dealing with Rows and Columns:
    A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns. 
    We can perform basic operations on rows/columns like selecting, deleting, adding, and renaming.
'''
import pandas as pd

# Define a dictionary containing employee data
# data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
#         'Age': [27, 24, 22, 32],
#         'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
#         'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}
#
# # Convert the dictionary into DataFrame
# df = pd.DataFrame(data)
#
# # select two columns
# print(df[['Name', 'Qualification']])

'''
Indexing a Dataframe using indexing operator [] :
    Indexing operator is used to refer to the square brackets following an object. The .loc and .iloc indexers also
     use the indexing operator to make selections. In this indexing operator to refer to df[].
'''
import pandas as pd

# making data frame from csv file
data = pd.read_csv("nba.csv", index_col="Name")

# retrieving columns by indexing operator
print(data)
first = data["Age"]

print(first)

'''
    Iterating over rows :
'''
# import pandas as pd
#
# # dictionary of lists
# dict = {'name': ["aparna", "pankaj", "sudhir", "Geeku"],
#         'degree': ["MBA", "BCA", "M.Tech", "MBA"],
#         'score': [90, 40, 80, 98]}
#
# # creating a dataframe from a dictionary
# df = pd.DataFrame(dict)
#
# print(df)
