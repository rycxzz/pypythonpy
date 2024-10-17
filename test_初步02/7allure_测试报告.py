# 安装 allure-pytest
# 运行：
#     在测试执行期间收集结果：
#     pytest 测试文件 -s -q --alluredir=./result/* (--alluredir用于指定存储测试结果的路径)
#     查看测试报告：
#         方式一：测试完成后成查看实际报告，在线看报告，会直接打开默认浏览器展示当前报告
#             allure serve ./result/*
#         方式二：从结果生成报告，这是一个启动tomcat的服务，生成报告、打开报告
#             生成报告：
#                 allure generate ./result/* -o ./report/ --clean(注意，覆盖路径加--clean)
#             打开报告：
#                 allure open -h 127.0.0.1 -p 8883 ./report/*

import pytest

def test_success():
    """this test succeeds"""
    assert True

def test_failure():
    """this test fails"""
    assert False

def test_skip():
    """this test is shipped"""
    pytest.skip('for a reason!')

def test_broken():
    raise Exception('oops')

# 生成测试数据：
    # pytest 7allure_测试报告.py --alluredir=./test_初步02/1
# 生成测试html报告：
#     allure serve ./test_初步02/1
# 生成报告：
#     allure generate ./test_初步02/1 -o ./test_初步02/report/  --clean
# 打开报告：
#     allure open ./test_初步02/report/
#     allure open -h 127.0.0.1 -p 8883 ./test_初步02/report/