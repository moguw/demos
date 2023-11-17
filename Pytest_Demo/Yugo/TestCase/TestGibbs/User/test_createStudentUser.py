import pytest,allure,sys,json
from Yugo.common.assert_control import *
from Yugo.common.request_control import *
from Yugo.common.dependent_control import *



# @pytest.mark.smoke
@pytest.mark.regression
@allure.step("test_createStudentUser")
@pytest.mark.parametrize("Args",Yamls()["test_create_studentUser"])
@graphql_control.get_graphql_query()
def test_createStudentUser(authToken,Args,query=None):
    user_id =D_BASE64(args("studentId"))
    sql = "SELECT * FROM g_bookings.students where id = %s" %user_id
    if handle_db_data(sql)is None:
        TestData = NewArgs(Args)
        response = http_request(TestData,query,authToken)
        # response = http_request(Args["args"],query)
        """（断言Args["response"]和response的值）"""
        assert_equality(Args["response"],response)
        setcahce_id(Args,response)
    else:
        set_global_data(Args["case"]["id"],args("studentId"))
        logger.info("studentId already exist,studentId is %s" %args("studentId"))




         
         






