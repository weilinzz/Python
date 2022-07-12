# 1. 导包
import unittest

# 2. 创建测试类
from tool import login


class TestLogin(unittest.TestCase):
    # 正确的用户名和密码: admin, 123456, 登录成功
    def test_username_password_ok(self):
        self.assertEqual('登录成功', login('admin', '123456'))

    # 错误的用户名: root, 123456, 登录失败
    def test_username_error_password_ok(self):
        self.assertEqual('登录失败', login('root', '123456'))

    # 错误的密码: admin, 123123, 登录失败
    def test_username_ok_password_error(self):
        self.assertEqual('登录失败', login('admin', '123123'))

    # 错误的用户名和错误的密码: aaa, 123123, 登录失败
    def test_username_error_password_error(self):
        self.assertEqual('登录失败', login('aaa', '123123'))
