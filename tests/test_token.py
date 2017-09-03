import unittest
import json
from urllib import request
from myapp.main.data import device_data
class TokenTestCase(unittest.TestCase):
    def test_get_token(self):
        headers = {'Content-Type': 'application/json'}
        # data = {"email": "dongfang3654@outlook.com", "password": "123456"}
        data = device_data
        data = json.dumps(data).encode('utf-8')
        url = 'http://127.0.0.1:5000/upload'
        req = request.Request(url, headers=headers, data=data)
        response = request.urlopen(req).read()
        print(response)
