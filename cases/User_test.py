import unittest

from api.User_api import get_user_list

class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        # 初始化测试数据
        self.projectId = "000000"
        self.departmentId = ""

    def tearDown(self) -> None:
        # 清理测试数据
        pass

    #case1: 输入正确的项目ID和部门ID，获取用户列表
    def test_get_user_list(self):
        # 实际结果 ：调用登录接口，获取返回结果
        actual_result = get_user_list(self.projectId, self.departmentId)
        self.assertLess(0, actual_result.get('total'))

    #case2:输入错误的项目ID或部门ID，获取用户列表
    def test_get_user_list_failed(self):
        wrong_projectId = "wrong_projectId"
        wrong_departmentId = "wrong_departmentId"
        actual_result = get_user_list(wrong_projectId, wrong_departmentId)
        self.assertEqual(0, actual_result.get('total'))

    #case3:输入空的项目ID或部门ID，获取用户列表
    def test_get_user_list_empty(self):
        empty_projectId = ""
        empty_departmentId = ""
        actual_result = get_user_list(empty_projectId, empty_departmentId)
        self.assertEqual(0, actual_result.get('total'))

    #case4：输入不存在的项目ID或部门ID，获取用户列表
    def test_get_user_list_not_exist(self):
        not_exist_projectId = "123456"
        not_exist_departmentId = ""
        actual_result = get_user_list(not_exist_projectId, not_exist_departmentId)