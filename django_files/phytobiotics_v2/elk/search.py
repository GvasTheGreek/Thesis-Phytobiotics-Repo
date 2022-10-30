from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search , Q
from elasticsearch import RequestsHttpConnection
import requests


def search(temperature,ambient_noise):
    client = Elasticsearch(['https://localhost:9200'],
        http_auth=('elastic', 'elastic'),
        #scheme="https",
        verify_certs=False,
        connection_class=RequestsHttpConnection,
        #use_ssl=True,
        port=8000,)
    

    q = Q("bool", should=[Q("match", temperature=temperature), Q("match", ambient_noise=ambient_noise)], minimum_should_match=1)
    s = Search(using=client, index="summer").query(q)[0:100]
    
    response = s.execute()
    print("Total {} hits found".format(response.hits.total))
    search = get_results(response)
    #print(search)
    return search

def get_results(response):
    results = []
    for hit in response:
        result_tuple = (hit.temperature, hit.ambient_noise)
        results.append(result_tuple)
        #print(result_tuple)
    return results