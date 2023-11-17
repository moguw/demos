import pytest,allure,sys,json
from Yugo.common.assert_control import *
from Yugo.common.request_control import *
from Yugo.common.dependent_control import *


@pytest.mark.smoke
@pytest.mark.regression
@allure.step("test_studentFillPersonalDetail")
@pytest.mark.parametrize("Args",Yamls()["test_studentFillPersonalDetail"])
@graphql_control.get_graphql_query()
def test_studentFillPersonalDetail(SP_authToken,Args,query=None):
    TestData = NewArgs(Args)
    response = SP_http_request(TestData,query,SP_authToken)
    # response =http_request(Args["args"],query,authToken)
    """(断言Args["response"]和response的值)"""
    assert_equality(Args["response"],response)
    """id存入cache(Args->key,response->value)"""
    # setcahce_id(Args,response)



         
         






