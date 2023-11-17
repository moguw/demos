"""
requests 接口请求
"""

import requests,json
from Yugo.common.logger_control import *
from Yugo.common import graphql_control
from Yugo.common.yaml_control import *
# tokenPath = token_path()



class SendRequest:
    def gibbs_apiRequest(variables,query,headers=None):
        try: 
            var = {"json": {'query': query, 'variables': variables}}
            # headers = read_data(tokenPath)
            rps = requests.post(url=args('gibbs_url'), **var,headers=headers)
            logger.info('**' * 40)
            logger.info(f"variables: {json.dumps(variables)}") 
            logger.info(f"Response: {rps.json()}")          
        except TimeoutError:
            logger.info('访问超时')
        else:
            return rps
  
    def sp_apiRequest(variables,query,headers=None):
        try: 
            var = {"json": {'query': query, 'variables': variables}}
            # headers = read_data(tokenPath)
            rps = requests.post(url=args('sp_url'), **var,headers=headers)
            logger.info('**' * 40)
            logger.info(f"variables: {json.dumps(variables)}") 
            logger.info(f"Response: {rps.json()}")
        except TimeoutError:
            logger.info('访问超时')
        else:
            return rps

def http_request(variables,query,headers=None):
    rsp = SendRequest.gibbs_apiRequest(variables,query,headers)
    return rsp

def SP_http_request(variables,query,headers=None):
    rsp = SendRequest.sp_apiRequest(variables,query,headers)
    return rsp





# def show_caller(level=1):
#     def show(func):
#         def wrapper(*args, **kwargs):
#             func(*args, **kwargs)
#             print('{0.f_code.co_filename}:{0.f_code.co_name}:{0.f_lineno}'.format(sys._getframe(level)))
#         return wrapper
#     return show       

    # @staticmethod
    # def request_log(variables,rsp):
    #     output_logger().info(f"variables: {json.dumps(variables)}")
    #     output_logger().info(f"Response: {rsp.json()}")


        


# class Requests:
#     def get_req(self,url, params, **kw):
#         try:
#             rsp = requests.get(url=url, params=params, **kw)
#         except TimeoutError:
#             logging.error('访问超时')
#         else:
#             return rsp

#     def post_Req(self, url, data=None, json=None, **kw):
#         # '''封装一个post方法，发送post请求'''
#         try:  # 当处理不成功时，比如URL地址输入方式错误，或者接口超时timeout，需要抛出一个异常
#             res = requests.post(url, data=data, json=json, **kw)  # 其中data是form表单形式的
#         except TimeoutError:
#             # 记录日志信息，放入logger里边，这样我们就能知道问题出在哪里
#             logging.error('访问不成功')
#         else:
#             return res
#         # vist方法是整合接口请求的方法

#     def vist_Req(self, method, url, params=None, data=None, json=None, **kw):
#         """访问接口"""
#         'GET,如果传输进来的是大写的GET。可以使用lower方法'
#         if method.lower == 'get':
#             return self.get_Req(url, params=params, **kw)
#         elif method.lower == 'post':
#             return self.post_Req(url, data=data, json=json, params=params, **kw)

#         # 如果接口中还有其他的请求方式比如put,option之类色，可以用下方的方法，实际工作中常用的是get和post
#         else:
#             return requests.request(method, url, **kw)

#     def json(self, method, url, params=None, data=None, json=None, **kw):  # json是要再vist方法下去进行进一步的处理
#         """访问接口，获取json数据"""
#         res = self.vist_Req(url, method, params=params, data=data, json=json, **kw)
#         # 获取json数据
#         try:
#             return res.json()
#         except:
#             # 记录日志信息
#             logging.error('不是json格式的数据')




