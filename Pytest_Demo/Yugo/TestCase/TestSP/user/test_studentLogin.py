import pytest,allure,sys,json
from Yugo.common.assert_control import *
from Yugo.common.request_control import *
from Yugo.common.dependent_control import *


# @pytest.mark.smoke
@pytest.mark.regression
@allure.step("test_studentLogin")
@pytest.mark.parametrize("Args",Yamls()["test_studentLogin"])
@graphql_control.get_graphql_query()
def test_studentLogin(Args,query=None):
    user_id = D_BASE64(get_global_data("createUser_01"))
    email_sql ="SELECT * FROM g_bookings.students where id = %s" %user_id
    TestData = str(NewArgs(Args)).replace("$email",handle_db_data(email_sql)["contact_email"])
    response = SP_http_request(ast.literal_eval(TestData),query)
    # response = http_request(Args["args"],query)
    """（断言Args["response"]和response的值）"""
    assert_equality(Args["response"],response)



         
         






