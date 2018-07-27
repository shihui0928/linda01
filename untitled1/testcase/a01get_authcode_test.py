import unittest,requests,json
from public import global_params as gp

class get_authcode_test(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_authcode(self):
        response=requests.get('http://183.2.168.226/member/getAuthCode?send={"phone":"15012730582"}')

        print(response.status_code)
        print(response.text)
        response_info=json.loads(response.text)
        print(response_info)
        gp.set_value(response_info["CodeInfo"]["authcode"])

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
