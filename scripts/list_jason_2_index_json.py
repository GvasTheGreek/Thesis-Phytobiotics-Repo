# Having a dict type json and wanna create an index type json in order
# to readable by Elasticsearch.

import json
import requests
import os


i = 0
f = open('Sensor_Data_RTH1.json', "r")
# Reading from file
data = json.loads(f.read())
print(len(data))

# Iterating through the json
# list
# for i in range(len(data)):
# print(data[i])

# Closing file
f.close()

with open('Sensor_Data_RTH1.json', 'w') as f:
    for i in range(len(data)):
        json.dump({"index": {"_id": i}}, f)
        f.write('\n')
        json.dump((data[i]), f)
        f.write('\n')
