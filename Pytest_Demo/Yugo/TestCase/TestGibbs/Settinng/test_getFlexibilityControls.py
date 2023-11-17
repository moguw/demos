import pytest,allure
from Yugo.common.yaml_control import *
from Yugo.common.request_control import *
from Yugo.common.assert_control import *
from Yugo.common.dependent_control import *

# @pytest.mark.smoke
@pytest.mark.regression
@allure.step("getFlexibilityControls")
# @pytest.mark.run(order=2)
@graphql_control.get_graphql_query()
@pytest.mark.parametrize("Args",Yamls()["test_getFlexibilityControls"])
def test_getFlexibilityControls(authToken,Args,query=None):
    TestData = NewArgs(Args)
    response = http_request(TestData,query,authToken)
    # response =http_request(Args["args"],query,authToken)
    """(断言Args["response"]和response的值)"""
    assert_equality(Args["response"],response)
    """id存入cache(Args->key,response->value)"""
    set_global_data(Args["case"]["id"],response.json()["data"]["getFlexibilityControls"]["setUpRateType"]["value"])



         





