# import pytest,allure,sys
# from Gibbs.common.Handle_data_and_logger import output_logger,output_datasYaml,ouput_datasQuery
# from Gibbs.API.Setting.RateCard import init_RateCard


# @pytest.mark.run(order=5)
# @allure.step("初始化ratecard测试")
# @pytest.mark.parametrize("propertyId, except_result, except_code, except_msg",
#                          output_datasYaml()["test_init_ratecard"])
# def test_Init_RateCard(authToken, propertyId, academicYearId,except_result,except_code,except_msg):
#     def_name = sys._getframe().f_code.co_name
#     output_logger().info('开始执行脚本%s：\n', def_name)
#     query = str(ouput_datasQuery('Init_RateCard.graphql'))
#     rps = init_RateCard(propertyId,academicYearId,query,authToken)
#     print(rps.text)

# import pytest,allure,sys
# from Gibbs.common.Handle_data_and_logger import output_logger,output_datasYaml,ouput_datasQuery
# from Gibbs.API.Setting.RateCard import get_RateCard

# @pytest.mark.run(order=6)
# @allure.step("获取ratecardId测试")
# @pytest.mark.parametrize("propertyId, except_result, except_code, except_msg",
#                          output_datasYaml()["test_init_ratecard"])
# def test_get_RateCard(authToken, propertyId, academicYearId,except_result,except_code,except_msg):
#     def_name = sys._getframe().f_code.co_name
#     output_logger().info('开始执行脚本%s：\n', def_name)
#     query = str(ouput_datasQuery('get_rateCard.graphql'))
#     rps = get_RateCard(propertyId,academicYearId,query,authToken)
#     if except_code == 200:
#         global MainCardId
#         MainCardId = rps.json()["data"]["getRateCards"]["rateCards"][0]["id"]
#         output_logger().info("MainCardId %s" % (MainCardId))
#     else:
#         output_logger().info("get rateCard failed")
#     print(rps.text)

# def setting_env_rateCardId():
#     return MainCardId


# import pytest,allure,sys
# from Gibbs.common.Handle_data_and_logger import output_logger,output_datasYaml,ouput_datasQuery
# from Gibbs.API.Setting.RateCard import update_MainCard


# @pytest.mark.run(order=7)
# @allure.step("更新ratecard测试")
# @pytest.mark.parametrize("propertyId,roomTypeId,price, except_result, except_code, except_msg",
#                          output_datasYaml()["test_update_mainCard"])
# def test_update_mainCard(authToken,propertyId,rateCardId,roomTypeId, academicYearId,price, except_result,except_code,except_msg):
#     def_name = sys._getframe().f_code.co_name
#     output_logger().info('开始执行脚本%s：\n', def_name)
#     query = str(ouput_datasQuery('update_MainCard.graphql'))
#     rps = update_MainCard(propertyId,rateCardId,roomTypeId,academicYearId,price,query,authToken)
#     print(rps.text)


# from pickletools import pyset
# import pytest,allure,sys,json
# from Gibbs.common.HandleYamls import *
# from Gibbs.common.logger import *
# from Gibbs.common.Assert import *
# from Gibbs.API.user.login import *
# @pytest.mark.smoke
# @allure.step("登录测试")
# @pytest.mark.parametrize("loginargs",get_YamlData()["test_login"])
# # @pytest.mark.parametrize("assertargs",get_checkData()["test_login_error_result"])
# def test_login(loginargs):
#     rsp = user_login(loginargs[0])
#     assert rsp.status_code == 200 
    

# string = [{"email": "support.uat1@student.com", "password": "support.uat1@student.com"},{"logign sucess"}]
# loginargs = [{'args': {'email': 'support.uat1@student.com', 'password': 'support.uat1@student.com'}}, {'code': {'except_code': 200}}]
# print(loginargs[1]["code"])
# import requests,json
# url = "https://gateway-uat1.project-g66.com/graphql?source=gibbs"

# query = """mutation UserLogin(
#     $email:String!,
#     $password: String!) {
#     login(
#         email: $email,
#         password: $password) {
#             authToken
#     }
# }"""

# variables = {"email": "support.uat1@student.com", "password": "support.uat1@student.com"}

# rps = requests.post(url=url, json={"query": query,"variables": json.dumps(variables)}) 
# print(rps.json())


#test_Login.py

# import requests,json,pytest
    
# def test_login():
#     url = "https://gateway-uat1.project-g66.com/graphql?source=gibbs"

#     query = """mutation UserLogin(
#         $email:String!,
#         $password: String!) {
#         login(
#             email: $email,
#             password: $password) {
#                 authToken
#         }
#     }"""

#     variables = {"email": "support.uat1@student.com", "password": "support.uat1@student.com"}
#     response = requests.post(url=url, json={"query": query,"variables": json.dumps(variables)}) 

#     print(response.json())
    
# if __name__ == "__main__":
#    pytest.main(["test_aaaaa.py"])


# from dataclasses import replace
# import datetime,time,os
# from ssl import _create_default_https_context
# # from distutils.command.config import config
# from functools import reduce



# def TimeStampToTime(timestamp):
#     timeStrct = time.localtime(timestamp)
#     return datetime.datetime.strftime(timeStrct,'%Y-%m-%d %H:%M:%S')


# def get_FileModifyTime(file_path):
#     # file_path= unicode(file_path,'utf8')
#     t = os.path.getmtime(file_path)
#     # datetime.datetime.strftime(t,'%Y-%m-%d %H:%M:%S')
#     return t

# # file_stat = os.stat(file_path)

# # # 获取最后修改时间
# # last_modified_time = time.ctime(file_stat.st_mtime)
# # last_modified_time1 = datetime.datetime.strptime(file_stat.st_mtime, "%Y-%m-%d %H:%M:%S")
# # print("最后修改时间：", last_modified_time1)

# def aa():
#    utc_now = datetime.datetime.utcnow()
#    s = datetime.datetime.strftime(get_FileModifyTime(file_path),'%Y-%m-%d %H:%M:%S')
#    print(s,utc_now)
# if __name__ == "__main__":
#     # s= (get_FileModifyTime(file_path) - datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")).seconds
#     # print(s)
#    aa()

# from datetime import timedelta

# root_dir = os.path.dirname(os.path.abspath('.'))
# file_path = root_dir + '/PYTEST_DEMO/Gibbs/Yaml_Data/token.yaml' 

# s = time.localtime(os.stat(file_path).st_mtime)
# t1 = time.mktime(s)

# now = time.localtime()
# t2 = time.mktime(now)

# print(t1,t2,datetime.timedelta(seconds=t2 - t1).seconds,datetime.timedelta(seconds=t2 - t1).days)
# from collections import Counter
# # from jsonpath import jsonpath
# import json,re

# aa = {
#             "propertyId":"eyJ0eXBlIjoiUHJvcGVydHkiLCJpZCI6MTY0fQ",
#             "tenancyOption":{
#                 "academicYearId": "$academicYearId",
#                 "bookingCategory": "DIRECT_LET",
#                 "description": "description",
#                 "endDate": "2023-11-02",
#                 "endDateType": "EQ",
#                 "freeCancelBehaviorType": "BEFORE",
#                 "freeCancelInterval": 1,
#                 "freeCancelPointType": "BOOKING_CONFIRMED_DATE",
#                 "intervalForTurnaround": 0,
#                 "name": "test_tenancy_11",
#                 "roomGroupIds":["eyJ0eXBlIjoiUm9vbUdyb3VwIiwiaWQiOjE0MzR9"],
#                 "startDate": "$startDate",
#                 "startDateType": "EQ",
#                 "tenancyLength": 60,
#                 "tenancyLengthType": "EQ",
#                 "tenancyType": "FIXED",
#                 "validFrom": "2023-09-02",
#                 "validTo": "2023-10-03",
#                 "viewOnWebsite": "asdasd",
#                 "linkToNomination": "asdasd",
#                 "isDifferentChargingDate": "true",
#                 "chargingStartDate": "2023-09-03",
#                 "chargingEndDate": "2023-11-01"
#             }
#         }


# key = ["academicYearId","sdfsdf"]

# strs =json.dumps(aa)
# nums = strs.count('$')
# print(nums)
# def aa():
#     for i in range(nums):
#         while key[i] == "academicYearId":
#             print("aaaa")
#             return key
#         else:
#             print("ddddd")


# aa()

# from shutil import copyfile
# path = os.path.dirname(os.path.abspath('.'))
# env_file_path = path + '/PYTEST_DEMO/Gibbs/conf/env/' + 'DataUat1.yaml'
# dst = path + '/PYTEST_DEMO/Gibbs/conf/env/'+ 'DataUat1copy.yaml'

# copyfile(env_file_path, dst)


# def clear_cache():
#      with open(dst, 'w') as f:
#          f.truncate()

# clear_cache()

# import yaml
# path = os.path.dirname(os.path.abspath('.'))
# env_file_path = path + '/PYTEST_DEMO/Gibbs/conf/env/' + 'DataUat1.yaml'
       
# def w():
#     with open(env_file_path,'r+') as f:
#         text = f.read()
#         f.seek(0,0)
#         f.write('email: &email "support.uat1@student.com"' + '\n' + text)

# w()

# with open(env_file_path, 'w') as file:
#         yaml.dump(data, file)

# def d(key):
#      with open(env_file_path,'rb') as f:
#         data =yaml.safe_load(f)
#         if key in data:
#             del data[key]
#             with open(env_file_path, 'w') as f:
#                 yaml.dump(data, f)

# if __name__ == '__main__':
#     d('email')

# startDate = str(datetime.date.today())
# endDate = str(datetime.date.today() + datetime.timedelta(days=+60))
# chargingStartDate = str(datetime.date.today())
# chargingEndDate = str(datetime.date.today() + datetime.timedelta(days=+59))
# tenancyLength =(datetime.datetime.strptime(endDate, '%Y-%m-%d') - datetime.datetime.strptime(startDate, '%Y-%m-%d')).days
# validFrom = str(datetime.date.today() + datetime.timedelta(days=-1))
# validTo = str(datetime.date.today() + datetime.timedelta(days=+30))
# import re,yaml
# from yaml_control import *
# def replace_value(yaml_file):
#     def _get(dict,list):
#         return reduce(lambda d,k:d[k],list,dict)
#     def _replace(obj):
#         for k ,v in obj.iteritems():
#             if isinstance(v,dict):
#                 _replace(v)
#             if isinstance(v,str):
#                 match = re.match(r'\${{(.*?)}}',v)
#             if match:
#                 reference = match.group(1).split('.')
#                 replace = _get(yaml_file,reference)
#                 obj[k] = re.sub(r'\${{(.*?)}}',replace,v)
#                 _replace(yaml_file)
#                 return yaml_file
# with open(env_path(),'r')as ymlfile:
#     config = yaml.safe_load(ymlfile)
#     config = replace_value(config)
# aaa = {
#           "propertyId": "eyJ0eXBlIjoiUHJvcGVydHkiLCJpZCI6MTY0fQ",
#           "academicYear": {
#               "name": "randomNum",
#               "fromYear": 2023,
#               "status": "CURRENT",
#               "isInMinPrice": "true"
#           }
#       }

# print("randomNum" in aaa)

# import json

# def parse_json(json_data):
#     try:
#         parsed_data = json.loads(json_data)
#         return parsed_data
#     except json.JSONDecodeError:
#         print("Invalid JSON data")
# def check_field(field_name, json_data, default_value=None):
#     if isinstance(json_data, list):
#         for item in json_data:
#             value = check_field(field_name, item, default_value)
#             if value is not None:
#                 return value
#     elif isinstance(json_data, dict):
#         for key, value in json_data.items():
#             if key == field_name:
#                 print("Field found:", key, ":", value)
#                 return value
#             else:
#                 value = check_field(field_name, value, default_value)
#                 if value is not None:
#                     return value
    
#     if default_value is not None:
#         print("Field not found. Returning default value:", default_value)
#         return default_value
#     else:
#         print("Field not found.")



# # JSON数据
# json_data = '''
# {
#           "propertyId": "eyJ0eXBlIjoiUHJvcGVydHkiLCJpZCI6MTY0fQ",
#           "academicYear": {
#               "name": "randomNum",
#               "fromYear": 2023,
#               "status": "CURRENT",
#               "isInMinPrice": "true"
#           }
#       }
# '''

# # 解析JSON数据
# parsed_data = parse_json(json_data)

# # 检查字段是否存在
# field_name = "name"
# field_value = check_field(field_name, parsed_data)
# if field_value is not None:
#     print("The value of", field_name, "is:", field_value)
# else:
#     print("Field not found.")

# 检查不存在的字段，并返回默认值
# field_name = "email"
# default_value = "N/A"
# field_value = check_field(field_name, parsed_data, default_value)
# print("The value of", field_name, "is:", field_value)


# import json,ast,random
# json_data = {
#           "propertyId": "eyJ0eXBlIjoiUHJvcGVydHkiLCJpZCI6MTY0fQ",
#           "academicYear": {
#               "name": "aaaa"+"randomNum",
#               "fromYear": 2023,
#               "status": "CURRENT",
#               "isInMinPrice": "true"
#           }
#       }

# aaaaa= json.dumps(json_data)
# data = str(aaaaa)
# print(data)

# if "randomNum" in data:
#     print("字符串存在于json中")
# else:
#     print("字符串不存在于json中")


# import json

# json_data = '{"name": "John Smith", "age": 30, "city": "New York"}'
# data = json.loads(json_data)

# if "John Smith" in data.values():
#     print("字符串存在于json中")
# else:
#     print("字符串不存在于json中")

# print(random.randint(10,10000))
# import json
# json_2 = ({'createAcademicYear': {'id': 'eyJ0eXBlIjoiQWNhZGVtaWNZZWFyIiwiaWQiOjc3NX0=', 'originId': 775, 'name': 'AY_0123822', 'fromYear': 2023, 'toYear': 2024, 'isEnabled': False, 'isCurrent': True, 'propertyId': 'eyJ0eXBlIjoiUHJvcGVydHkiLCJpZCI6MTY0fQ==', 'isInMinPrice': True, '__typename': 'AcademicYear', 'academicYearWithCheckStatus': {'roomGroup': {'status': 'RED', 'number': None, 'tip': 'NO_ROOM_GROUP_FOUND', 'numberUnit': 'item'}, 'tenancyOption': {'status': 'RED', 'number': None, 'tip': 'NO_TENANCY_OPTION_CREATED_YET', 'numberUnit': 'item'}, 'installment': {'status': 'ORANGE', 'number': 1, 'tip': 'NO_EXTRA_INSTALLMENT_CREATED_EXCEPT_THE_FULL_TYPE', 'numberUnit': 'item'}, 'contractTemplate': {'status': 'ORANGE', 'number': 3, 'numberUnit': 'item', 'tip': 'MISSING_FOLLOWING_ADDENDUMS_FOR_BOOKING_AMENDMENT', 'values': ['guarantor', 'tenancy', 'general', 'bed']}, 'flexibilityControl': {'status': 'RED', 'number': None, 'tip': 'NO_ITEM_FOUND', 'numberUnit': None}, 'rateCard': {'status': 'RED', 'number': None, 'tip': 'NO_RATE_CARD_CREATED_YET', 'numberUnit': None}, 'additionalFee': {'status': 'ORANGE', 'number': None, 'tip': 'NO_ADDITIONAL_FEE_ENABLED_YET', 'numberUnit': 'item'}, 'customField': {'status': 'GREY', 'number': None, 'tip': 'NO_CUSTOM_FIELD_CREATED_YET', 'numberUnit': 'item'}, 'specialOffer': {'status': 'GREY', 'tip': 'NO_SPECIAL_OFFER_CREATED_YET', 'number': None, 'numberUnit': 'item'}, 'status': False}}})
# j_2 = str(json_2)
# json_1 = ("'isCurrent': Tru0")
# j_1= str(json_1)
# print(j_1 in j_2)


# from cache_control import *
# aaa = ["AY_02","AY_03","AY_04"]
# print(range(len(aaa)))
# for i in range(len(aaa)):
#     print(aaa[i])

# def setcahce_id(Args_rsp,actual_rsp):
#     """断言正确用例"""
#         # apiName = Args_rsp["response"]["apiName"]
#     return set_global_data("id",aaa)

# def getcahce_id():
#     for i in range(len(aaa)):

#     # """断言正确用例"""
#         return get_global_data(aaa[i])

# def NewArgs(Args_rsp):

#             for i in range(len(Args_rsp["dependence_case"]["id"])):
#                 id = getcahce_id(Args_rsp)
#                 # Args = str(randomNum(Args_rsp)).replace("$"+Args_rsp["dependence_case"]["key"][i],str(id))
#                 # new_Args = ast.literal_eval(Args)
#                 # return new_Args


# def replace_exception_chars(string):
#     exception_chars_dict = {'Old': 'New', 'old': 'new'}
#     exception_chars_keys = list(exception_chars_dict.keys())
#     for exception_char in exception_chars_keys:
#         if exception_char in string:
#             # string.replace(exception_char, exception_chars_dict[exception_char])
#             string = string.replace(exception_char, exception_chars_dict[exception_char])
#     return string

# print(replace_exception_chars('Old, not old'))

# import os
# import sys
# file = os.path.basename(sys.argv[0])
# print(file)
# import os
# print(os.path.dirname(os.getcwd()))

# from socket import timeout
# import pymysql
# from sshtunnel import SSHTunnelForwarder

# host = '127.0.0.1'
# user = 'all_rw'
# passwd='LgeQXZXrd6'
# port= 3408
# db='g_bookings'
# charset='utf8'
# #连接数据库
# def connect_db():
#     with SSHTunnelForwarder(
#         ("bastion.project-g66.com", 22),
#         ssh_pkey="/Users/lihao.wang/Desktop/Project/database/privateKey的副本.txt",
#         ssh_username="dev",
#         remote_bind_address=(host, port)) as server:
#         conn = pymysql.connect(host= host
#                                 , user= user
#                                 , passwd=passwd
#                                 , port= server.local_bind_port
#                                 , db=db
#                                 , charset=charset
#                                 )
#         cur = conn.cursor()
#         sql = "select * from bookings where id = 100017"
#         cur.execute(sql)
#         data = cur.fetchall()
#         data1 = cur.fetchone()
#         print("data:",data,"data1:",data1)

# connect_db()



# aaa = ["test_login", "test_createRoomGroup"]

# print(aaa.index("test_login"))\


import json
aaa = {
        "case": {"id": "AY_02"},
        "dependence_case": {"is_dependent": False},
        "args":{
            "propertyId": "*propertyId",
            "academicYear": {
                "name": "AY_02$randomNum",
                "fromYear": 2023,
                "status": "PAST",
                "isInMinPrice": "true"
            }
        },
        "response":{"apiName": "createAcademicYear","except_result": "sucess","type_name": "rateCards",
                    "except_code": 200,"except_msg": "'isCurrent': False",
                    "sql_query": "select * from g_configurations.academic_years where id = $id"
                }
    }
ccc = {'getRateCards': {'formula': 'B', 'rateCards': [{'id': 'eyJ0eXBlIjoiUmF0ZUNhcmQiLCJpZCI6NzIwfQ==', 'originId': 720, 'name': ['room_type'], 'isBasic': True, 'active': False, 'cardType': 'TWO_D', 'cardPerformance': 'FACTOR', 'occupancyScope': None, 'occupancyBreakpointType': None, 'isIncludedNomination': None, 'academicYearId': 'eyJ0eXBlIjoiQWNhZGVtaWNZZWFyIiwiaWQiOjkxOX0=', 'incrementType': 'FIXED_AMOUNT', 'isSpecifyRoomType': True, 'isPriceLimitation': False, '__typename': 'RateCard'}]}}
# bbb = json.dumps(aaa)
print("createAcademicYears" in aaa["response"].values())
# print(type(aaa),type(bbb))
# print(type(ccc),ccc["getRateCards"]["rateCards"][0]["id"])
# from mysql_control import *
# user_id ="120624"
# sql = "SELECT * FROM g_bookings.students where id = %s" %user_id

# print(handle_db_id(sql))