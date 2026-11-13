# lib import
import json


# creating dict
data1 = {
    'name': 'OJ Simpson',
    'age': 30,
    'city': "few. York, NY",
    'interests': ['Traveling', 'Football', 'Golf', 'Running', 'Videogames', 'History'],
    'is_student': False
}


# creating JSON file
with open ('data1.json', 'w') as json_file:
    json.dump(data1, json_file, indent=4)


# display success text
print('Data was writen to JSON')