"""
打印日志
"""
import logging
import os,sys
import time
#if not exits log文件夹，则创建文件夹
def create_file():
    log_dir = os.path.dirname(os.getcwd()) + '/Yugo_Pytest/Pytest_Demo/Yugo/log/'
    print(log_dir)
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)
    else:
        pass
    now_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    log_file = log_dir + now_time + '.log'
    return log_file


class Log(object):
    def __init__(self, name, level='DEBUG'):
        self.__name = name
        self.__path = create_file()
        self.__level = level
        self.__logger = logging.getLogger(self.__name)
        self.__logger.setLevel(self.__level)

    def __ini_handler(self):
        """初始化handler"""
        self.__logger.handlers.clear()
        stream_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(self.__path, encoding='utf-8')
        return stream_handler, file_handler

    def __set_handler(self, stream_handler, file_handler, level='DEBUG'):
        """设置handler级别并添加到logger收集器"""
        stream_handler.setLevel(level)
        file_handler.setLevel(level)
        self.__logger.addHandler(stream_handler)
        self.__logger.addHandler(file_handler)

    def __set_formatter(self, stream_handler, file_handler):
        """设置日志输出格式"""
        formatter = logging.Formatter('[%(asctime)s]-[%(name)s]-[%(filename)s]-[line:%(lineno)d]'
                                      '-[%(levelname)s]: %(message)s',
                                      datefmt='%a, %d %b %Y %H:%M:%S')
    
        stream_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

    def __close_handler(self, stream_handler, file_handler):
        """关闭handler"""
        stream_handler.close()
        file_handler.close()


    @property
    def Logger(self):
        """构造收集器，返回looger"""
        stream_handler, file_handler = self.__ini_handler()
        self.__set_handler(stream_handler, file_handler)
        self.__set_formatter(stream_handler, file_handler)
        self.__close_handler(stream_handler, file_handler)
        return self.__logger
        
logger= Log(os.path.basename(sys.argv[0])).Logger
# def A():
#     log = Log(__name__)
#     logger = log.Logger
#     return logger

# def loggers():
#     # 调用common.logs打印日志
#     # log_file = os.path.basename(sys.argv[0])
#     log = Log(__name__)
#     logger = log.Logger
#     return logger


# if __name__ == '__main__':
#     log = Log(__name__)
#     logger = log.Logger
#     logger.debug('I am a debug message')
#     logger.info('I am a info message')
#     logger.warning('I am a warning message')
#     logger.error('I am a error message')
#     logger.critical('I am a critical message')
