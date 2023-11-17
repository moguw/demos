import pytest,allure
from Yugo.common.assert_control import *
from Yugo.common.request_control import *
from Yugo.common.yaml_control import *
from Yugo.common.dependent_control import *



# @pytest.mark.smoke
@pytest.mark.regression
@allure.step("创建tenancyOptions")
# @pytest.mark.run(order=4)
@graphql_control.get_graphql_query()
@pytest.mark.parametrize("Args",Yamls()["test_create_tenancyOptions"])
def test_CreateTenancyOption(authToken,Args,query=None):
    # actual_response = http_request(Args["args"])
    response = http_request(NewArgs(Args),query,authToken)
    """(断言Args["response"]和response的值)"""
    assert_equality(Args["response"],response)
    """id存入cache(Args->key,response->value)"""
    setcahce_id(Args,response)
        
 










    