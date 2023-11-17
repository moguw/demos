"""
处理相互依赖数据(ID)的用例
处理yaml中的随机数(randomNum)

"""
from Yugo.common.logger_control import *
import random,ast,json
def is_except_result(Args_rsp):
    results = Args_rsp["response"]["except_result"]
    return results

def is_dependent(Args_rsp):
    results1 = Args_rsp["dependence_case"]["is_dependent"]
    return results1

def apiName(Args_rsp):
    apiName = Args_rsp["response"]["apiName"]
    return apiName
def typeName(Args_rsp):
    typeName = Args_rsp["response"]["type_name"]
    return typeName
    

global_data = {}
def set_global_data(keys, value):
    """
    设置全局变量，用于关联参数
    """
    global_data[keys] = value
    return set_global_data


def get_global_data(keys):
    """
    从全局变量global_data中取值
    """
    return global_data.get(keys)  

def setcahce_id(Args_rsp,actual_rsp):
    try:
        """将用例中的ID存储到cache中"""
        if is_except_result(Args_rsp) == "sucess":
            if "type_name" in Args_rsp["response"].keys():
                return set_global_data(Args_rsp["case"]["id"],actual_rsp.json()["data"][f"{apiName(Args_rsp)}"][f"{typeName(Args_rsp)}"][0]["id"])
            elif "getInstallmentWithPlans" in Args_rsp["response"].values():
                return set_global_data(Args_rsp["case"]["id"],actual_rsp.json()["data"][f"{apiName(Args_rsp)}"]["installmentDataHash"])
            elif "getInstallmentsForSelection" in Args_rsp["response"].values():
                return set_global_data(Args_rsp["case"]["id"],actual_rsp.json()["data"][f"{apiName(Args_rsp)}"]["installments"][-1]["installmentId"])
            elif "getBedsForSelection" in Args_rsp["response"].values():
                return set_global_data(Args_rsp["case"]["id"],actual_rsp.json()["data"][f"{apiName(Args_rsp)}"]["beds"][-1]["bedId"])
            elif "createStudentUser" in Args_rsp["response"].values():
                return set_global_data(Args_rsp["case"]["id"],actual_rsp.json()["data"][f"{apiName(Args_rsp)}"]["studentInfo"]["id"])
            else:
                return set_global_data(Args_rsp["case"]["id"],actual_rsp.json()["data"][f"{apiName(Args_rsp)}"]["id"])
    except:
        logger.warning("id不存在")

# def getcahce_id(Args_rsp):
#     """获取cache中的ID"""
#     for i in range(len(Args_rsp["dependence_case"]["id"])):
#         return get_global_data(Args_rsp["dependence_case"]["id"][i])
# Args_rsp["case"]["id"]+

def NewArgs(Args_rsp):
        """
        处理相互数据（ID）依赖的用例
        处理yaml中的随机数（randomNum）
        """
        try:
            json_data = json.dumps(Args_rsp["args"])
            data = str(json_data)
            # """dependence 为true且参数中使用随机数"""
            if is_dependent(Args_rsp) == True and "$randomNum" in data:
                for i in range(len(Args_rsp["dependence_case"]["caseId"])):
                    id = get_global_data(Args_rsp["dependence_case"]["caseId"][i])
                    Args_rsp["args"] = str(Args_rsp["args"]
                    ).replace("$"+Args_rsp["dependence_case"]["key"][i],str(id)
                    ).replace("$randomNum",str(random.randint(10,100000)))
                return ast.literal_eval(Args_rsp["args"])
            # """dependence 为true且参数中不使用随机数"""
            elif is_dependent(Args_rsp) == True and "$randomNum" not in data:
                for i in range(len(Args_rsp["dependence_case"]["caseId"])):
                    id = get_global_data(Args_rsp["dependence_case"]["caseId"][i])  
                    Args_rsp["args"] = str(Args_rsp["args"]
                    ).replace("$"+Args_rsp["dependence_case"]["key"][i],str(id))
                return ast.literal_eval(Args_rsp["args"])
            # """dependence 为false且参数中使用随机数"""
            elif "$randomNum" in data and is_dependent(Args_rsp) == False:
                args = str(Args_rsp["args"]).replace("$randomNum",str(random.randint(10,100000)))
                new_args = ast.literal_eval(args)
                return new_args
            # """dependence 为false且参数中不使用随机数"""
            elif "$randomNum" not in data and is_dependent(Args_rsp) == False:
                return Args_rsp["args"]  
        except:
            logger.error("无可用的数据")






# def NewArgs(Args_rsp):
#         json_data = json.dumps(Args_rsp["args"])
#         data = str(json_data)
#         if is_dependent(Args_rsp) == True and  "$randomNum" in data:
#             for i in range(len(Args_rsp["dependence_case"]["id"])):
#                 id = get_global_data(Args_rsp["dependence_case"]["id"][i])
#                 # aaa = (Args_rsp)["args"]
#                 (Args_rsp)["args"] = str((Args_rsp)["args"]).replace("$"+Args_rsp["dependence_case"]["key"][i],str(id)).replace("$randomNum",Args_rsp["case"]["id"]+str(random.randint(10,100000)))
             
#                 # new_Args = 
#             return ast.literal_eval((Args_rsp)["args"])
#         else:
#             return (Args_rsp)["args"]
  
# def getcahce_id(Args_rsp):
#     for i in range(len(Args_rsp["dependence_case"]["id"])):

#     # """断言正确用例"""
#         return get_global_data(Args_rsp["dependence_case"]["id"][i])

# def NewArgs(Args_rsp):
#         if is_dependent(Args_rsp) == True:
#             for i in range(len(Args_rsp["dependence_case"]["id"])):
#                 id = getcahce_id(Args_rsp)
#                 Args = str(randomNum(Args_rsp)).replace("$"+Args_rsp["dependence_case"]["key"][i],str(id))
#                 new_Args = ast.literal_eval(Args)
#                 return new_Args
#         else:
#             return randomNum(Args_rsp)
  


# def NewArgs(Args_rsp):
#         if dependent(Args_rsp) == True:
#             id = getcahce_id(Args_rsp)
#             Args = str(Args_rsp["args"]).replace("$"+Args_rsp["dependence_case"]["name"],str(id))
#             new_Args = ast.literal_eval(Args)
#             return new_Args
#         else:
#             return Args_rsp["args"]

# def randomNum(Args_rsp):
#     json_data = json.dumps(Args_rsp["args"])
#     data = str(json_data)
#     if "$randomNum" in data:
#         args = str(Args_rsp["args"]).replace("$randomNum",Args_rsp["case"]["id"]+str(random.randint(10,100000)))
#         new_args = ast.literal_eval(args)
#         return new_args
#     else:
#         args = Args_rsp["args"]
#         return args








