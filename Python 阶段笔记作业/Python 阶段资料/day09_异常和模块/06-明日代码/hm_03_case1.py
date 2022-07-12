# 1. 导包
import unittest

# 2. 实例化套件对象
from hm_03_case import TestLogin

suite = unittest.TestSuite()
# 3. 组装用例
suite.addTest(unittest.makeSuite(TestLogin))

# 4. 实例化运行对象
runner = unittest.TextTestRunner()
# 5. 执行套件对象
runner.run(suite)

