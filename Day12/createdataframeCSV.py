'''

1.How to create Data frame using CSV:
    CSV files are the “comma-separated values”, these values are separated by commas, this file can be
    view like as excel file. In Python, Pandas is the most important library coming to data science.
    We need to deal with huge datasets while analyzing the data, which usually can get in
    CSV file format. Creating a pandas data-frame using CSV files can be achieved in multiple ways.

'''
import pandas as pd
#Method #1: Using read_csv() method: read_csv() is an important pandas function to read csv files and do operations on it.

# creating a data frame
df = pd.read_csv("nba.csv")
print(df.head())

#Method #2: Using read_table() method: read_table() is another important pandas function to read csv
# files and create data frame from it.

df = pd.read_table("nba.csv", delimiter =", ",engine='python')
print(df.tail())

#Method #3: Using csv module: One can directly import the csv files using csv module and then create a
# data frame using that csv file.

import csv

with open("sample.csv") as csv_file:
    # read the csv file
    csv_reader = csv.reader(csv_file)

    # now we can use this csv files into the pandas
    df = pd.DataFrame([csv_reader], index=None)

# iterating values of first column
for val in list(df[1]):
    print(val)


'''
2. How to write CSV from Dataframe:
    
'''

data = {
  "name": ["Sally", "Mary", "John"],
  "age": [50, 40, 30],
  "qualified": [True, False, False],
    "salary":[100,300,500]
}

df=pd.DataFrame(data,columns=['name','age','qualified','salary'])
df.to_csv('new_crate.csv')


'''
3.Indexing and Slicing:
    With the help of Pandas, we can perform many functions on data set like Slicing, Indexing. 
'''

#1.Slicing

# importing pandas library
import pandas as pd

# Initializing the nested list with Data set
player_list = [['M.S.Dhoni', 36, 75, 5428000],
			['A.B.D Villers', 38, 74, 3428000],
			    ['V.Kholi', 31, 70, 8428000],
			['S.Smith', 34, 80, 4428000],
			['C.Gayle', 40, 100, 4528000],
			['J.Root', 33, 72, 7028000],
			['K.Peterson', 42, 85, 2528000]]

# creating a pandas dataframe
df = pd.DataFrame(player_list, columns=['Name', 'Age', 'Weight', 'Salary'])

# data frame before slicing
print(df)


#Now Usuing Slicing


# Slicing rows in data frame
df1 = df.iloc[0:4]

print(df1)


# Slicing columnss in data frame
df1 = df.iloc[:,0:2]

print(df1)


#2.indexing

df = pd.DataFrame({
                    'Networking': [45, 34, 23, 8, 21],
                    'Web Engineering': [32, 43, 23, 50, 21],
                    'Complier Design': [14, 42, 21, 12, 45]
                    },
                    )
# before Setting its takes bydefault as 0 ,1 ,2 upto so on
print(df)

#after setting indexes

df = pd.DataFrame({
                    'Networking': [45, 34, 23, 8, 21],
                    'Web Engineering': [32, 43, 23, 50, 21],
                    'Complier Design': [14, 42, 21, 12, 45]
                    }, index=['Abhishek', 'Saumya', 'Ayushi', 'Saksham', 'Rajveer']
                    )

print(df)