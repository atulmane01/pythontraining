'''

1)How to Delete a Data Frame:
    Clearing a pandas DataFrame releases the memory allocated to it.
    USE del TO CLEAR A DATAFRAME
    Call del on every reference to a single pandas.DataFrame to fully clear it from memory.

    Syntax:

        del df['column_name']

'''


# importing the module
import pandas as pd

# creating a DataFrame
my_df = {'Name': ['Rutuja', 'Anuja'],
		'ID': [1, 2], 'Age': [20, 19]}
df = pd.DataFrame(my_df)
print(df)
#display("Original DataFrame")
#display(df)

print("deleting a column")
del df['Age']
print(df)
#display("DataFrame after deletion")
#display(df)
