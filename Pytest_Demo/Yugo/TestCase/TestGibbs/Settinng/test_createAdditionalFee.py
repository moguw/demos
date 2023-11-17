import pytest,allure
from Yugo.common.yaml_control import *
from Yugo.common.request_control import *
from Yugo.common.assert_control import *
from Yugo.common.dependent_control import *

# @pytest.mark.smoke
@pytest.mark.regression
@allure.step("AdditionalFee")
# @pytest.mark.run(order=3)
@graphql_control.get_graphql_query()
@pytest.mark.parametrize("Args",Yamls()["test_create_AdditionalFee"])
def test_createAdditionalFee(authToken,Args,query=None):
    TestData = NewArgs(Args)
    response = http_request(TestData,query,authToken)
    # response =http_request(Args["args"],query,authToken)
    """(断言Args["response"]和response的值)"""
    assert_equality(Args["response"],response)
    """id存入cache(Args->key,response->value)"""
    setcahce_id(Args,response)



         





