# import pytest,allure,sys,json
# from Yugo.common.assert_control import *
# from Yugo.common.request_control import *
# from Yugo.common.dependent_control import *


# @pytest.mark.smoke
# @allure.step("test_createStripeCharge")
# @pytest.mark.parametrize("Args",Yamls()["test_createStripeCharge"])
# @graphql_control.get_graphql_query()
# def test_createStripeCharge(SP_authToken,Args,query=None):
#     TestData = NewArgs(Args)
#     response = SP_http_request(TestData,query,SP_authToken)
#     # response =http_request(Args["args"],query,authToken)
#     """(断言Args["response"]和response的值)"""
#     assert_equality(Args["response"],response)
#     """id存入cache(Args->key,response->value)"""
    # setcahce_id(Args,response)



         
         






