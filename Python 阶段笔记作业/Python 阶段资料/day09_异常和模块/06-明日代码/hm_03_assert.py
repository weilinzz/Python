import unittest


class Demo(unittest.TestCase):
    def test_assertEqual(self):
        # 假设某次测试实际结果 3, 预期结果 3
        self.assertEqual(3, 3)
        # self.assertEqual(3, 4)  # 实际结果 4, 预期结果 3

    def test_assertIn(self):
        # self.assertIn('admin', '欢迎 admin 用户登录')  # 包含,通过
        # self.assertIn('admin', '欢迎 adminnnnnnnn 用户登录')  # 包含,通过
        # self.assertIn('admin', '欢迎 aaaaaadminnnnnnnn 用户登录')  # 包含,通过
        # self.assertIn('admin', '欢迎 adddddmin 用户登录')  # 不包含,用例不通过
        self.assertIn('admin', 'admin')  # 包含,通过
