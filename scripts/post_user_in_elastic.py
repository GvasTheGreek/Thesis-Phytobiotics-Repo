import requests
import time
from requests.auth import HTTPBasicAuth
from requests.structures import CaseInsensitiveDict


response = requests.get('https://host.docker.internal:9200',
                        verify=False,
                        auth=HTTPBasicAuth('elastic', 'elastic'))

# print request object
# print(response)

data = {
    "password": "linuxhint",
    "enabled": True,
    "roles": ["superuser", "kibana_admin"],
    "full_name": "Linux Hint",
    "email": "example@linuxhint.com",
    "metadata": {
        "intelligence": 7
    }
}

headers = {
    'content-type': 'application/json'
}

username = "new-user"
r = requests.post('https://host.docker.internal:9200/_security/user/' + username, json=data, headers=headers, verify=False, auth=('elastic', 'elastic'))


# r = requests.post('https://host.docker.internal:9200/summer/_bulk?pretty', headers=headers, data=payload, verify=False, auth=('elastic', 'elastic'))  # 18/8
print(r)
