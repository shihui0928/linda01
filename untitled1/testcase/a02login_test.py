import unittest, requests, json,time
from public import global_params as gp
from log import log

class login_test(unittest.TestCase):

    def setUp(self):
        pass

    def test_login(self):
        str1 = str(gp.get_value(0))
        data = '{\"phone\":\"15012730582\",\"authcode\":\"'+str1+'\",\"TaskID\":\"12345\",\"RegistrationID\":\"171976fa8abaa711375\"}'
        url = 'http://183.2.168.226/member/login?send='+data
        response = requests.post(url)
        response_info = json.loads(response.text)
        print(response.status_code)
        print(response.text)
        h=gp.set_value2(response_info["Data"]["Token"])
        gp.set_value2(response_info["Data"]["UserID"])


        log02=log.Log()
        log02.debug(time.strftime('%Y_%M_%d')+"hahahahahh")

        try:
            self.assertEqual(response_info["code"],200)
            self.assertEqual(response_info["msg"],"用户登录成功")
        except Exception as e:
            print("登陆接口测试失败!")
            raise e


    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()

