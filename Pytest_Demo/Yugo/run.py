import pytest,allure,os
from common import allure_control


if __name__ == "__main__":
    markers_type = os.environ['markers']
    pytest.main(['-m %s']) % str(markers_type)
    # pytest.main(["-m smoke"])
    # pytest.main(["-m regression"])

    """生成allure报告"""
    """
    
    pytest.main(["-m smoke","--alluredir", "../PYTEST_DEMO/Yugo/report/"])
    cmd = 'allure serve ../Pytest_Demo/Yugo/report --clean-alluredir'
    allure_control.allure_report(cmd)
    
    """
    """
        --reruns: 失败重跑次数
        --count: 重复执行次数
        -v: 显示错误位置以及错误的详细信息
        -s: 等价于 pytest --capture=no 可以捕获print函数的输出
        -q: 简化输出信息
        -m: 运行指定标签的测试用例
        -x: 一旦错误，则停止运行
        --maxfail: 设置最大失败次数，当超出这个阈值时，则不会在执行测试用例
        "--reruns=3", "--reruns-delay=2"
    """





