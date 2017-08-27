import unittest
import json
from urllib import request
class TokenTestCase(unittest.TestCase):
    def test_get_token(self):
        headers = {'Content-Type': 'application/json'}
        data = {"email": "dongfang3654@outlook.com", "password": "123456"}
        data = json.dumps(data).encode('utf-8')
        url = 'http://127.0.0.1:5000/token'
        req = request.Request(url, headers=headers, data=data)
        response = request.urlopen(req).read()
        self.assertTrue(response is not None)