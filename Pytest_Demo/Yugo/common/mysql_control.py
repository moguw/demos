"""
操作数据库
利用ssh隧道对mysql进行连接
"""

# -- coding:UTF-8 --
import pymysql
from sshtunnel import SSHTunnelForwarder
from Yugo.common.logger_control import *
from Yugo.common.yaml_control import *
"""mysql连接信息 """
mysql_host = args("mysql_host")
mysql_user = args("mysql_user")
mysql_passwd= args("mysql_passwd")
mysql_port= args("mysql_port")
# db_name='g_configurations'

"""ssh连接信息"""
ssh_host= args("ssh_host")
ssh_port = args("ssh_port")
ssh_user = args("ssh_user")
ssh_private_key = args("ssh_private_key")
charset= args("charset")
#连接数据库
def handle_db_data(sql):
    retry_count = 10
    init_connect_count = 0
    connect_res = True
    while connect_res and init_connect_count < retry_count:
        try:
            with SSHTunnelForwarder(
                (ssh_host, ssh_port),
                ssh_pkey=ssh_private_key,
                ssh_username= ssh_user,
                remote_bind_address=(mysql_host, mysql_port)) as server:
                conn = pymysql.connect(host= mysql_host
                                        , user= mysql_user
                                        , passwd=mysql_passwd
                                        , port= server.local_bind_port
                                        # , db=db_name
                                        , charset=charset
                                        )
                # while True:
                
                try:
                    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
                    cur.execute(sql) 
                    data = cur.fetchall()
                    connect_res = False 
                    try:
                        new_data = data[0]
                        return (new_data)   
                    except:
                        logger.warning("数据库中无法查询到该数据")
                except Exception as error:
                    logger.warning("sql语句执行错误")
                    
        except:
            logger.warning("重新连接mysql")
            init_connect_count += 1

# def handle_db_token(sql):
#     retry_count = 10
#     init_connect_count = 0
#     connect_res = True
#     while connect_res and init_connect_count < retry_count:
#         try:
#             with SSHTunnelForwarder(
#                 (ssh_host, ssh_port),
#                 ssh_pkey=ssh_private_key,
#                 ssh_username= ssh_user,
#                 remote_bind_address=(mysql_host, mysql_port)) as server:
#                 conn = pymysql.connect(host= mysql_host
#                                         , user= mysql_user
#                                         , passwd=mysql_passwd
#                                         , port= server.local_bind_port
#                                         # , db=db_name
#                                         , charset=charset
#                                         )
#                 # while True:
                
#                 try:
#                     cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
#                     cur.execute(sql) 
#                     data = cur.fetchall()
#                     connect_res = False 
#                     try:
#                         new_data = data[0]["reset_password_token"]
#                         return (new_data)   
#                     except:
#                         logger.warning("数据库中无法查询到该数据")
#                 except Exception as error:
#                     logger.warning("连接mysql失败")
                    
#         except:
#             logger.warning("重新连接mysql")
#             init_connect_count += 1


# print(handle_db_data('SELECT * FROM g_bookings.students where id  = 120624')["contact_email"])






