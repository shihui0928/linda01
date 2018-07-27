import unittest,json,requests
from public import global_params as gp
import base64

class useinfo_phone(unittest.TestCase):

    def setUp(self):
        pass

    def test_userinfo(self):
        key=str(gp.get_key(0))
        userID=str(gp.get_value2(1))
        a=base64.b64encode(userID.encode('utf-8'))
        a1=str(a,'utf-8')
        data = '{\"key\":\"'+key+a1+'\",\"UserID\":\"'+userID+'\",\"DataType\":\"3\"}'
        # data='{\"key\":\"'+key+a1+'\",\"UserID\":\"'+userID+'\",\"DataType\":\"3\"}'
        url="http://183.2.168.226/member/getUser?send="+data
        response=requests.post(url)
        response_info=json.loads(response.text)

        try:
            self.assertEqual(response_info["code"],200)
        except Exception as e:
            print("获取用户信息失败")
            raise e

    def tearDown(self):
        pass

if __name__ =="__main__":
    unittest.main()


