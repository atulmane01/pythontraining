#problem with json data

import json
with open('/home/atul/simple.json' ,'r') as persondata:
    employee=json.load(persondata)
    print(employee)


#The error is occured because of Your Json data in the form of like
#
# [
#   {
#     'id': "A001",
#     'name': "Tom",
#     'math': 60,
#     'physics': 66,
#     'chemistry': 61
#   }
# ]
#
# # Your Data is in the form of as like in double quates
#
# [
#   {
#     "id": "A001",
#     "name": "Tom",
#     "math": 60,
#     "physics": 66,
#     "chemistry": 61
#   }
# ]