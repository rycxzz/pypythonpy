# 场景：
#     你与其他测试工程师合作一起开发时，公共模块要在不同文件中，要在大家都访问到的地方
# 解决：
#     conftest.py这个文件进行数据共享，并且他可以放在不同位置起着不同的范围共享作用
# 执行：
#     系统执行到参数login时，线从本文件中查找是否有这个名字的变量，之后再conftest.py中找是否有
# 步骤：
#     将登录模块带@pytest.fixture()写在conftest.py文件中

# 配置注意事项
# conftest.py文件名是不能换的
# conftest.py与运行的用例要在同一个package夏，并且由__init__.py文件
# 不许要import conftest.py，pytest用例会自动查找
# 全局的位置和前期工作都可以写在这里，放在某个包下，就是这个包数据共享的地方

import pytest

@pytest.fixture()
def login():
    print("这是个登录方法")

"""用于自定义名称，防止报预警找不到自定义的名称"""
def pytest_configure(config):
    marker_list = ["search","login"]
    for markers in marker_list:
        config.addinivalue_line("markers",markers)