import unittest


class TestLogin(unittest.TestCase):
    def setUp(self):  # 测试方法执行之前执行的内容
        print('输入登录的网址...')

    def tearDown(self) -> None:
        print('.....关闭页面')

    @classmethod
    def setUpClass(cls) -> None:
        print('测试开始之前, 打开浏览器------')

    @classmethod
    def tearDownClass(cls) -> None:
        print('---------测试结束, 关闭浏览器')

    def test_login1(self):
        print('输入测试数据 1 并点击登录')

    def test_login2(self):
        print('输入测试数据 2 并点击登录')

    def test_login3(self):
        print('输入测试数据 3 并点击登录')

    def test_login4(self):
        print('输入测试数据 4 并点击登录')