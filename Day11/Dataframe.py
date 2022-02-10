'''

What is Data Frame:
    is two-dimensional size-mutable, potentially heterogeneous tabular data structure with
    labeled axes (rows and columns). A Data frame is a two-dimensional data structure, i.e.,
    data is aligned in a tabular fashion in rows and columns.
    Pandas DataFrame consists of three principal components, the data, rows, and columns.

'''

import pandas as pd

# Define a dictionary containing employee data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age': [27, 24, 22, 32],
        'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

# select two columns
print(df[['Name', 'Qualification']])