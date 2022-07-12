# 1. 导包
import unittest
# 2. 使用系统默认提供的加载对象并组装加载用例
suite = unittest.defaultTestLoader.discover('./case', 'hm*')
# 3. 实例化运行对象并运行
unittest.TextTestRunner().run(suite)
