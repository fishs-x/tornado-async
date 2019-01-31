import unittest
import requests




class AuthTest(unittest.TestCase):
    host = 'http://127.0.0.1:8888'

    def test_login(self):
        url = "/api/v1/user/auth/login"
        res = requests.post(self.host + url)
        print(res.text)

    @staticmethod
    def test_register():
        pass


if __name__ == '__main__':
    unittest.main()
