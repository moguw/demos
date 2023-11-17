import pytest,allure
from Yugo.common.request_control import *
from Yugo.common.assert_control import *
from Yugo.common.dependent_control import *


# @pytest.mark.smoke
@pytest.mark.regression
@allure.step("test_verifyStudentResetPasswordToken")
# @pytest.mark.run(order=3)
@graphql_control.get_graphql_query()
@pytest.mark.parametrize("Args",Yamls()["test_verifyStudentResetPasswordToken"])
def test_verifyStudentResetPasswordToken(authToken,Args,query=None):
    user_id = D_BASE64(get_global_data("createUser_01"))
    reset_password_token_sql ='SELECT * FROM  g_users.student_users us, g_bookings.students bs where us.id = bs.student_user_id AND bs.id = %s' %user_id
    if handle_db_data(reset_password_token_sql)["reset_password_token"] is not None:
        TestData = str(NewArgs(Args)).replace("$token",handle_db_data(reset_password_token_sql)["reset_password_token"])
        response = http_request(ast.literal_eval(TestData),query,authToken)
        """(断言Args["response"]和response的值)"""
        assert_equality(Args["response"],response)
        """id存入cache(Args->key,response->value)"""
        # setcahce_id(Args,response)
    else:
        logger.info("%s user's email has been verify" %user_id)