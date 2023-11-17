from os import environ
import pytest
from Yugo.common.yaml_control import *
from Yugo.common.logger_control import *
from Yugo.common.request_control import *


@pytest.fixture(scope="session", autouse=False)
def clear_report():
    """如clean命名无法删除报告，这里手动删除"""
    pass

@pytest.fixture(scope='module',autouse=True)
def testcase_name(request):
    name = request.node.name
    logger.info('开始执行用例:%s\n',name)


@pytest.fixture(scope='session')
@graphql_control.get_graphql_query()
def authToken(query=None):   
        rps = http_request(args('admin_login_user')[0],query)
        authTokens = rps.json()['data']['login']['authToken']
        headers = {f"gibbs-authorization-{args('environment')}": f"Bearer {authTokens}"}
        logger.info("token:"+str(headers))
        return headers


def pytest_collection_modifyitems(items):
    # 自定义用例顺序
    appoint_items = [
                    # Gibbs Case
                    "test_login","test_createStudentUser","test_verifyStudentResetPasswordToken","test_resetStudentUserPassword","test_createAcademicYear","test_createContractTemplate","test_getFlexibilityControls","test_createRoomGroup","test_CreateTenancyOption","test_createCustomizedInstallment","test_initRateCard","test_getRateCards","test_updateMainCard","test_createAdditionalFee","test_updateAcademicYearBookingStatus",
                    "test_CreateBooking","test_getBedsForSelection","test_SelectBed","test_getInstallmentsForSelection","test_getInstallmentWithPlans","test_selectInstallment",
                    #  SP Case
                    "test_studentLogin","test_studentFillPersonalDetail","test_studentAcceptTerms","test_studentGetBooking","test_createStripeCharge","test_createPayment"
                    
                    ]

    # 指定运行顺序
    run_items = []
    for i in appoint_items:
        for item in items:
            module_item = item.name.split("[")[0]
            if i == module_item:
                run_items.append(item)

    for i in run_items:
        run_index = run_items.index(i)
        items_index = items.index(i)

        if run_index != items_index:
            n_data = items[run_index]
            run_index = items.index(n_data)
            items[items_index], items[run_index] = items[run_index], items[items_index]





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













                




















