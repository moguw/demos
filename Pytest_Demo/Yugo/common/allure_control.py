"""
allure 生成测试报告
"""
import shell
from common.shell_control import *
def allure_report(cmd):
    shell = Shell()
    # cmd = 'allure serve ../Pytest_Demo/yugo/report --clean-alluredir'
    return shell.invoke(cmd)