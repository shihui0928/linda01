import unittest, requests, json
from public import global_params as gp
import base64

class update(unittest.TestCase):

    def setUp(self):
        pass

    def test_login(self):
        str2 = str(gp.get_value2(0))
        userID=str(gp.get_value2(1))
        a=base64.b64encode(userID.encode('utf-8'))
        a1=str(a,'utf-8')
        # a2=str2+a1
        # key=gp.set_key(a2)
        url = 'http://183.2.168.226/member/updateToken?send='+'{"key":'+"\""+str2+a1+"\""+'}'
        response = requests.post(url)
        response_info = json.loads(response.text)
        print(response.status_code)
        print(response.text)
        gp.set_key(response_info["NewToken"])


        try:
            self.assertEqual(response_info["code"],200)
            # self.assertEqual(response_info["msg"],"用户更新token成功")
        except Exception as e:
            print("登陆更新token失败!")
            raise e


    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()