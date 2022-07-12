# 1. 导包
import unittest
# 2. 实例化加载对象并组装加载用例---> 得到 suite 对象
# unittest.TestLoader().discover('用例所在的目录路径', '用例代码名字')
# 用例代码名字可以使用*
# suite = unittest.TestLoader().discover('./case', 'hm_*')
suite = unittest.TestLoader().discover('./case', 'hm_case_*')
# suite = unittest.TestLoader().discover('./case', 'hm_case_01*')
# 3. 实例化运行对象并运行
unittest.TextTestRunner().run(suite)
# runner = unittest.TextTestRunner()
# runner.run(suite)

