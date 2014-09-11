__author__ = 'Jon'

import requests
r = requests.get('http://127.0.0.1:8081/people/')
print r.text


