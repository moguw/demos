
## 框架介绍

本框架主要是基于 Python + pytest + allure + log + yaml + mysql + Jenkins 实现的接口自动化框架。

* git地址: 

## 前言

框架主要使用 python 语言编写，结合 pytest 进行二次开发

本框架支持多业务接口依赖，多进程执行，mysql 数据库断言和 接口响应断言，并且用例直接在yaml文件中维护，无需编写业务代码，
接口pytest框架生成allure报告

## 实现功能

* 测试数据隔离, 实现数据驱动
* 支持多接口数据依赖: 如A接口需要同时依赖B、C接口的响应数据作为参数
* 数据库断言: 直接在测试用例中写入查询的sql即可断言，无需编写代码
* 动态多断言: 如接口需要同时校验响应数据和sql校验，支持多场景断言
* 日志模块: 打印每个接口的日志信息
* 自定义拓展字段: 如用例中需要生成的随机数据，可直接调用


## 目录结构


    ├── data                          // 测试用例数据
    ├── logs                          // 日志层
    ├── report                        // 测试报告层
    ├── test_case                     // 测试用例代码
    ├── Graphql                       // graphql语句
    │   └── fragments            	    // 分离graphql-fragments语句
    ├── common                        // 工具类
    │   └── assert_control           // 断言
    │   └── allure_control           // 生成测试报告
    │   └── decode_control           // 处理decodeId
    │   └── dependent_control        // 处理数据（ID）相互依赖的用例
    │   └── exceptions_control       // 异常处理
    │   └── graphql_control          // 读取graphql语句
    │   └── logger_control           // 日志操作处理
    │   └── mysql_control            // 连接 mysql
    │   └── request_control          // 封装requests请求
    │   └── shell_control            // shell命令
    │   └── yaml_control             // 读取data数据
    ├── Readme.md                     // help
    ├── pytest.ini                     
    ├── run.py                        // 运行入口  
    

## 依赖库


    allure-pytest==2.9.45
    allure-python-commons==2.9.45
    atomicwrites==1.4.0
    attrs==21.2.0
    certifi==2021.10.8
    cffi==1.15.0
    charset-normalizer==2.0.7
    colorama==0.4.4
    colorlog==6.6.0
    cryptography==36.0.0
    DingtalkChatbot==1.5.3
    execnet==1.9.0
    Faker==9.8.3
    idna==3.3
    iniconfig==1.1.1
    jsonpath==0.82
    packaging==21.3
    pluggy==1.0.0
    py==1.11.0
    pycparser==2.21
    PyMySQL==1.0.2
    pyOpenSSL==21.0.0
    pyparsing==3.0.6
    pytest==6.2.5
    pytest-forked==1.3.0
    pytest-xdist==2.4.0
    python-dateutil==2.8.2
    PyYAML==6.0
    requests==2.26.0
    six==1.16.0
    text-unidecode==1.3
    toml==0.10.2
    urllib3==1.26.7
    xlrd==2.0.1
    xlutils==2.0.0
    xlwt==1.3.0

## 安装教程

首先，执行本框架之后，需要搭建好 python、jdk、 allure环境

搭建python教程：[http://c.biancheng.net/view/4161.html](http://c.biancheng.net/view/4161.html)

搭建jdk环境：[https://www.cnblogs.com/zll-wyf/p/15095664.html](https://www.cnblogs.com/zll-wyf/p/15095664.html)

安装allure：[https://blog.csdn.net/m0_49225959/article/details/117194318](https://blog.csdn.net/m0_49225959/article/details/117194318)



如果在安装过程中出现如下 Could not find a version 类似的异常， 不用担心，可能是因为你安装的python环境
版本和我不一致导致的，直接 pip install 库名称，不指定版本安装就可以了。



