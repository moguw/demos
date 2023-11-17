import pytest,allure,sys,json
from Yugo.common.assert_control import *
from Yugo.common.request_control import *
from Yugo.common.dependent_control import *


@pytest.mark.smoke
@pytest.mark.regression
@allure.step("登录测试")
@pytest.mark.parametrize("Args",Yamls()["test_login"])
@graphql_control.get_graphql_query()
def test_login(Args,query=None):
    TestData = NewArgs(Args)
    response = http_request(TestData,query)
    # response = http_request(Args["args"],query)
    """（断言Args["response"]和response的值）"""
    assert_equality(Args["response"],response)



         
         






