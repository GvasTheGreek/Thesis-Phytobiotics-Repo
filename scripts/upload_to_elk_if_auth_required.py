import requests
import time
from requests.auth import HTTPBasicAuth
from requests.structures import CaseInsensitiveDict

time.sleep(5)

response = requests.get('https://host.docker.internal:9200',
                        verify=False,
                        auth=HTTPBasicAuth('elastic', 'elastic'))

# print request object
print(response)
json_data = {
    'properties': {
        'CO2 (ppm)': {
            'type': 'date',
        },
        'Entity Name': {
            'type': 'text',
        },
        'NH3 (ppm)': {
            'type': 'long',
        },
        'Timestamp': {
            'type': 'date',
            'format': 'yyyy-MM-dd HH:mm:ss',
        },
        'ambient_light (lux)': {
            'type': 'long',
        },
        'ambient_noise (dB)': {
            'type': 'long',
        },
        'humidity (%)': {
            'type': 'long',
        },
        'temperature (°C)': {
            'type': 'double',
        },
    },
}

payload = open("Sensor_Data_RTH1.json", 'rb')
headers = {
    'content-type': 'application/json'
}
r = requests.put('https://localhost:9200/nypd?pretty', verify=False, auth=('elastic', 'elastic'))
print(r)
r = requests.put('https://localhost:9200/nypd/_mapping', headers=headers, verify=False, auth=('elastic', 'elastic'), json=json_data)
print(r)
r = requests.post('https://localhost:9200/nypd2/_bulk?pretty', headers=headers, data=payload, verify=False, auth=('elastic', 'elastic'))  # 18/8
print(r)

new_index = {
    "source": {
        "index": "nypd2",
        "query": {
            "match_all": {}
        }
    },

    "dest": {
        "index": "nypd"
    }
}

time.sleep(10)
r = requests.post('https://localhost:9200/_reindex', headers=headers, json=new_index, verify=False, auth=HTTPBasicAuth('elastic', 'elastic'))
print(r)
