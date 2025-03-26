import unittest
from api.login_api import login

#定义一个全局变量，用于存储sessionId
sessionId = ""

class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        # 初始化测试数据
        self.username = "AILRXb/P3CaqWse7pcnL0Xl/NTc0bqDhx63l7ZozbjxSWkvUqwWO3Y0tMsJkh1lvInyhW8lex/vfcUtA3Bk6IA=="
        self.password = "lpvoH2lamhwBLe32F4u32H/jV3CqHhnzfYACi/MChtse2nvUzvGDnOgKPjD25tCOMPYZGi5zdP6BoyBH40EemA=="

    def tearDown(self) -> None:
        # 清理测试数据
        pass

    #case1: 输入正确的用户名和密码，登录成功
    def test_login(self):
        # 实际结果 ：调用登录接口，获取返回结果
        actual_result = login(self.username, self.password)
        self.assertEqual(1, actual_result.get('code'))
        self.assertEqual('操作成功', actual_result.get('msg'))
        #提取字段里的sessionId值，放入全局变量中供其他方法调用
        global sessionId
        sessionId = actual_result.get('data').get('sessionId')
        print(sessionId)

    # case2: 输入错误的用户名或密码，登录失败
    def test_login_failed(self):
        wrong_username = "wrong_admin"
        wrong_password = "wrong_123456"
        actual_result = login(wrong_username, wrong_password)
        self.assertEqual(0, actual_result.get('code'))

    # case3: 输入空的用户名或密码，登录失败
    def test_login_empty(self):
        empty_username = ""
        empty_password = ""
        actual_result = login(empty_username, empty_password)
        self.assertEqual(0, actual_result.get('code'))
        self.assertIn('用户名不能为空', actual_result.get('msg'))

