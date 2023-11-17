"""
读取yaml数据文件
"""
import os,time,datetime,yaml,ast,random
from typing import Any, Text, Union

env_file = 'SmokeCase-uat3.yaml'
project_path = '/Pytest_Demo/Yugo/conf/env/'

def env_path():
    current_path = os.path.dirname(os.path.abspath('.'))
    env_file_path = current_path + project_path + env_file
    return env_file_path

def read_data(file_path):
    with open(file_path, 'r') as f:
        data = yaml.load(f.read(), Loader=yaml.FullLoader)
        return data

def Yamls():
    datasyaml = read_data(env_path())
    return datasyaml

# 读取yaml中的环境的信息
def args(args):
    return  Yamls()[args]




# def set_caches(file_path,value: Any) -> None:
#         """
#         设置多组缓存数据
#         :param value: 缓存内容
#         :return:
#         """
#         with open(file_path, 'w', encoding='utf-8') as file:
#             file.write(str(value))


    


# def clear_cache(file_path):
#      with open(file_path, 'w') as f:
#          f.truncate()





