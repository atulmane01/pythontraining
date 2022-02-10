'''
1.How to create Data frame using JSON:
    Along with CSV, JSON is another commonly found format for datasets, especially when extracting data from web APIs.
'''

import pandas as pd
customer_json_file = 'simple.json'

customers_json = pd.read_json(customer_json_file,convert_dates=True)

print(customers_json.head())




'''
2.How to write JSON from Dataframe:
    

'''
import pandas as pd
data = {'Product': ['Desktop Computer','Tablet','iPhone','Laptop'],
        'Price': [700,250,800,1200],
        'avd':[188,55,66,77]
        }

df = pd.DataFrame(data, columns= ['Product', 'Price','avd'])

df.to_json ('asdf.json')
print(df)





