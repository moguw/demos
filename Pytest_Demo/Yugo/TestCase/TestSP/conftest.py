import pytest
from Yugo.common.yaml_control import *
from Yugo.common.logger_control import *
from Yugo.common.request_control import *
from Yugo.common.decode_control import *
from Yugo.common.mysql_control import *
from Yugo.common.dependent_control import *

@pytest.fixture(scope='module',autouse=True)
def testcase_name(request):
    name = request.node.name
    logger.info('开始执行用例:%s\n',name)

@pytest.fixture(scope='session')
@graphql_control.get_graphql_query()
def SP_authToken(query=None):
        user_id =D_BASE64(args("studentId"))
        sql = "SELECT * FROM g_bookings.students where id = %s" %user_id 
        if handle_db_data(sql)is None: 
                user_id = D_BASE64(get_global_data("createUser_01"))
                email_sql ="SELECT * FROM g_bookings.students where id = %s" %user_id
                email = handle_db_data(email_sql)["contact_email"]
                var = {"email": email,"password": args("password"),"topLandlordId": args("topLandlordId")}
                rps = SP_http_request(var,query)
                authTokens = rps.json()['data']['studentLogin']['authToken']
                headers = {f"sp-authorization-{args('environment')}": f"Bearer {authTokens}"}
                logger.info("SP_token:"+str(headers))
                return headers
        else: 
                rps = SP_http_request(args('student_login_user')[0],query)
                authTokens = rps.json()['data']['studentLogin']['authToken']
                headers = {f"sp-authorization-{args('environment')}": f"Bearer {authTokens}"}
                logger.info("SP_token:"+str(headers))
                return headers








# global_data = {}

# @pytest.fixture
# def set_global_data():
#     """
#     设置全局变量，用于关联参数
#     """
#     def _set_global_data(key, value):
#         global_data[key] = value
#     return _set_global_data
 
# @pytest.fixture
# def get_global_data():
#     """
#     从全局变量global_data中取值
#     """
#     def _get_global_data(key):
#         return global_data.get(key)
#     return _get_global_data













                




















