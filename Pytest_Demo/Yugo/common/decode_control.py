"""
处理decode Id
"""

import base64
import json

def D_BASE64(origStr):
    #当输入的base64字符串不是3的倍数时添加相应的=号
    if origStr != "":
        if(len(origStr)%3 == 1): 
            origStr += "=="
        elif(len(origStr)%3 == 2): 
            origStr += "=" 
        
        dStr = base64.b64decode(origStr).decode()
        decode_id = json.loads(dStr)["id"]
        return decode_id
    else:
        return -1
# print(D_BASE64(''))
