from elasticsearch import Elasticsearch
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

es = Elasticsearch(['https://localhost:9200'], http_auth=('elastic', 'elastic'), verify_certs=False)

body = {
    "mappings": {
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
        }
    }

}


def function():
    p = 0
    es.indices.create(index='summer', params=None, headers=None, ignore=400, body=body)
    # es.index(index='custom-mapping-index', document='Sensor_Data_RTH1.json', doc_type=None, id=None, params=None, headers=None)

    with open('Sensor_Data_RTH3.json') as f:
        data = json.loads(f.read())
        for row in range(len(data)):
            # put document into elastic search
            es.index(index="summer", body=data[row], id=p)
            # print(obj)
            p = p + 1


function()
# es.bulk(body='Sensor_Data_RTH1.json', index='custom-mapping-index', doc_type=None, params=None, headers=None)
