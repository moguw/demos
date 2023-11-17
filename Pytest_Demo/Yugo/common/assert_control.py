"""

用例结果断言
response.status_code 断言
response.json() 与接口实际期望结果断言

"""
from Yugo.common.logger_control import *
from Yugo.common.mysql_control import *
from Yugo.common.decode_control import *
import json
def is_except_result(Args_rsp):
    results = Args_rsp["except_result"]
    return results
    

def assert_equality(Args_rsp,actual_rsp):
    """断言正确用例"""
    if is_except_result(Args_rsp) == "sucess":
        codes = Args_rsp["except_code"]
        apiName = Args_rsp["apiName"]
        logger.debug("期望 status_code 结果为:"+ str(codes)+
                    ";实际 status_code 结果为:"+ 
                    str(actual_rsp.status_code))
        assert codes == actual_rsp.status_code
        if Args_rsp["except_msg"] != "":
            msgs = Args_rsp["except_msg"]
            logger.debug("期望 sucess_msg 结果为:"+ str(msgs)+
                        ";实际 sucess_msg 结果为:"+ 
                        str(actual_rsp.json()["data"]))
            assert str(msgs) in str(actual_rsp.json()["data"])
        else:
            pass
        if "sql_query" in Args_rsp.keys():
            if Args_rsp["sql_query"] != "":
                sql_except_result_id = handle_db_data(str(Args_rsp["sql_query"]).replace("$id",str(D_BASE64(actual_rsp.json()["data"][f"{apiName}"]["id"]))))["id"]
                logger.debug("sql查询结果为:"+str(sql_except_result_id)+";实际response结果为:"+
                str(D_BASE64(actual_rsp.json()["data"][f"{apiName}"]["id"])))
                assert sql_except_result_id == D_BASE64(actual_rsp.json()["data"][f"{apiName}"]["id"])
            else:
                pass
        else: 
            logger.warning("参数中缺少sql_query")


        """断言失败用例"""
    else:
        codes = Args_rsp["except_code"]
        logger.debug("期望 status_code 结果为:"+ str(codes)+
                    ";实际 status_code 结果为:"+ str(actual_rsp.status_code))
        assert codes == actual_rsp.status_code
        msgs = Args_rsp["except_msg"]
        logger.debug("期望 errors_msg 结果为:"+ str(msgs)+
                    ";实际 errors_msg 结果为:"+ 
                    actual_rsp.json()["errors"][0]["message"])
        assert msgs in actual_rsp.json()["errors"][0]["message"]
  




