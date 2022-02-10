'''
    1.How to access it:
    We can access data of DataFrames in many ways,

'''
import pandas as pd
dictObj = {'EmpId' : ['E01','E02','E03','E04'],
       'EmpName' : ['Raj','Atul','Reena','Ayushi'],
       'Department' : ['IT','IT','HR','Accounts']}
df=pd.DataFrame(dictObj, index=['First','Second','Third','Fourth'])
print(df)



#
# Using the row name and row index number along with the column, we can easily access a single value of a DataFrame.

# Example:
print(df.EmpName[2])  ## Access using row index
##Output Reena




