import unittest, requests, json
from public import global_params as gp

class inform_wifi_test(unittest.TestCase):

    def setUp(self):
        pass

    def test_login(self):
        deviceID = str(gp.get_value2(2))
        data = '{\"DeviceID\":\"'+deviceID+'\",\"RegistrationID\":\"171976fa8abaa711370\"}'
        url = 'http://183.2.168.226/member/login?send='+data
        response = requests.post(url)
        response_info = json.loads(response.text)
        print(response.status_code)
        print(response.text)


        try:
            self.assertEqual(response_info["code"],200)
            self.assertEqual(response_info["msg"],"Success")
        except Exception as e:
            print("登陆接口测试失败!")
            raise e


    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
