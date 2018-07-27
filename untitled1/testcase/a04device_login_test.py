import unittest,requests,json
from public import global_params as gp

class device_login(unittest.TestCase):

    def setUp(self):
        pass

    def test_login(self):
        data="{\"DeviceSN\":\"SFEV3412\",\"RegistrationID\":\"171976fa8abaa711375\"}"
        url="http://183.2.168.226/member/login?send="+data
        response=requests.post(url)
        response_info=json.loads(response.text)
        gp.set_value2(response_info["Data"]["DeviceID"])

        # try:
        #     self.assertEqual(response_info["code",200])
        #     self.assertEqual(response_info["msg"],"盒子登录成功")
        # except Exception as e:
        #     print("登陆盒子失败")
        #     raise e
        try:
            self.assertEqual(response_info["code"],200)
            self.assertEqual(response_info["msg"],"盒子登录成功")
        except Exception as e:
            print("登陆接口测试失败!")
            raise e

    def tearDown(self):
        pass

if __name__ =="__main__":
    unittest.main()


