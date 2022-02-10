'''
Accessing Rows
    We can access rows of a DataFrame in two ways.

    By using loc and iloc

    Pandas provide a unique method to retrieve rows from a Data frame. DataFrame.loc[] method is a method that takes
    only index labels and returns row or dataframe if the index label exists in the caller data frame.

    Purely integer-location based indexing for selection by position

    syntax:
       <DataFrame Object>.loc [ [ <row name>] ]  = Access a single row or multiple rows by name.

       <DataFrame Object>.iloc [ [<row index no> ] ] = Access a single or multiple rows by row index no
'''
'''
property DataFrame.loc
Access a group of rows and columns by label(s) or a boolean array.

.loc[] is primarily label based, but may also be used with a boolean array.
'''

# importing pandas package

# making data frame from csv file
import pandas as pd
dictObj = {'EmpId' : ['E01','E02','E03','E04'],
       'EmpName' : ['Raj','Atul','Reena','Ayushi'],
       'Department' : ['IT','IT','HR','Accounts']}
df=pd.DataFrame(dictObj, index=['First','Second','Third','Fourth'])
print(df)

# df.loc[[‘Second’]]   ## Access row using location, pass row name
print(df.iloc[[2]])  ## Access row using row index number




