# 1.import pytest类似的setup，teardown同样灵活
#     模块级(setup_module/teardown_module)模块始末，全局的（优先最高）
#     函数级(setup_function/teardown_function)只对函数用例生效（不在类中），在外部方法执行前执行setup，外部方法执行后执行teardown
#     类级(setup_class/teardown_class)只在类中前后运行一次（在类中）
#     方法级(setup_method/teardown_method)开始于方法始末（在类中）
#     类里面的(setup/teardown)运行在调用方法的前后
import sys

import pytest

# def setup_module():
#     print("这是setup_module 方法")
#
# def teardown_module():
#     print("这是teardown_module 方法")
#
# def setup_function():
#     print("这是setup_function 方法")
#
# def teardown_function():
#     print("这是teardown_function 方法")
#
# def test_login():
#     print("这是一个外部的方法")
#
# class TestDemo():
#     def setup_class(self):
#         print("setup_class")
#
#     def setup_method(self):
#         print("setup_method")
#
#     def setup(self):
#         print("setup")
#
#     def teardown_class(self):
#         print("teardown_class")
#
#     def teardown_method(self):
#         print("teardown_method")
#
#     def teardown(self):
#         print("teardown")
#
#     def test_one(self):
#         print("开始执行 test_one方法")
#         x = 'this'
#         assert 'h' in x
#
#     def test_two(self):
#         print("开始执行 test_two方法")
#         x = 'hello'
#         assert 'e' in x
#
#     def test_three(self):
#         print("开始执行 test_three方法")
#         a = 'hello'
#         b = 'hello world'
#         assert a in b
#
# if __name__ == '__main__':
#     # pytest.main("-v -x TestDemo")
#     # pytest.main(['-v','-s','TestDemo'])
#     pytest.main()

# 在conftest.py文件中自动查找并调用
# @pytest.fixture()
# def login():
#     print("这是个登录方法")

# def test_case1(login):
#     print("test_case1 需要登录")
#     pass
#
# def test_case2():
#     print("test_case2 不需要登录")
#     pass
#
# def test_case3(login):
#     print("test_case3 需要登录")
#     pass
#
# if __name__ ==  '__main__':
#     pytest.main()

# 场景：
#     已经将测试方法前要执行的或依赖的解决了，测试方法后销毁清除数据的要如何进行？如模块级别，类似setupClass
# 解决：
#     通过在同一模块中加入yield关键字，yield是调佣第一次返回结果，第二次执行它下面的语句返回。
# 步骤：
#     在@pytest.fixture(scope=module)
#     在登录的方法中加yield，之后加销毁清除的步骤，注意，这种方式没有返回值，如要返回值使用addfinalizer
# @pytest.fixture(scope="module")
# def open():
#     print("打开浏览器")
#     yield
#
#     print("执行teardown ！")
#     print("最后关闭浏览器")
#
# def test_search(open):
#     print("test_search")
#     raise NameError
#     pass
#
# def test_search2(open):
#     print("test_search2")
#     pass
#
# def test_search3(open):
#     print("test_search3")
#     pass
#
# if __name__ == '__main__':
#     pytest.main()

# 场景：
#     不想原测试方法有任何改动，或全部都自动实现自动应用，没特例，也都不需要返回值时可以选择自动应用
# 解决：
#     使用fixture中参数autouse=True实现
# 步骤：
#     在方法上面加@pytest.fixture(autouse=True)
#     在测试方法上加@pytest.mark.usefixtures("start")
# @pytest.fixture(autouse=True)
# def open():
#     print("打开浏览器")
#
# def test_search1():
#     print("test_search1")
#     raise NameError
#     pass
#
# def test_search2():
#     print("test_search2")
#     pass
#
# def test_search3():
#     print("test_search3")
#     pass
#
# if __name__ == '__main__':
#     pytest.main()

# 场景：
#     测试离不开数据，为了数据灵活，一般数据都是通过参数传递的
# 解决：
#     fixture通过固定参数request传递
# 步骤：
#     在fixture中增加@pytest.fixture(params=[1,2,3,'linda'])在方法参数写request
# @pytest.fixture(params=[1,2,3,'linda'])
# def test_data(request):
#     return request.param

# """参数化，前两个变量，后面是对应的数据
# 3+5->test_input 9->expect"""
# @pytest.mark.parametrize("test_input,expected",[("3+5",8),("2+5",7),("7*5",30)])
# def test_eval(test_input,expected):
#     """eval 将字符串str当成有效的表达式求值，并返回结果"""
#     assert eval(test_input) == expected

# 参数组合
# @pytest.mark.parametrize("x",[1,2])
# @pytest.mark.parametrize("y",[8,10,11])
# def test_foo(x,y):
#     print(f"测试数据组合x:{x},y:{y}")

# 方法名作为参数
test_user_data = ['Tome','Jerry']
@pytest.fixture(scope="module")
def login_r(request):
    """这是接收并传入的参数"""
    user = request.param
    print(f"\n 打开首页准备登录，登录用户名：{user}")
    return user

# """ indirect=True,可以把传过来的参数当函数来执行 """
# @pytest.mark.parametrize("login_r",test_user_data,indirect=True)
# def test_login(login_r):
#     a = login_r
#     print(f"测试用例中login的返回值；{a}")
#     assert a != ""

# skip 表示此次不执行的用例
# @pytest.mark.skip("此次测试不执行登录")
# """@pytest.mark.skipif(sys.platform == "darwin",reason="不在macos上执行")"""
# """@pytest.mark.xfail (不执行但标注成xpass)"""
@pytest.mark.parametrize("login_r",test_user_data,indirect=True)
def test_login(login_r):
    a = login_r
    print(f"测试用例中login的返回值；{a}")
    assert a != ""

if __name__ == '__main__':
    pytest.main('-v')

# Skip使用场景：
#     调试时不想运行这个用例
#     标记无法在某些平台上运行的测试功能
#     在某些版本中执行，其他版本中跳过
#     当前的外部资源夏不可用时跳过（如果测试数据是从数据库中取到的，连接数据库的功能如果未成功就跳过，因为执行也都报错）
# 解决：
#     @pytest.mark.skip跳过这个测试用例，可以加条件skipif，在满足某些条件下才希望通过，否则跳过这个测试
# Xfail场景：
#     功能测试尚未实施或者尚未修复的错误，当测试通过时尽管预计会失败（标记为pytest.mark.xfail），它是一个xpass，在测试摘要中报告
#     你希望测试由于某种情况而就应该失败
# 解决：
#     @pytest.mark.xfail

# 使用自定义标记mark只执行某部分用例
# 场景：
#     只执行符合要求的某一部分用例，可以把一个web项目划分多个模块，然后指定模块名称执行
#     app自动化时，如果想Android和ios公用一套代码时，可以使用标记功能，运行代码时指定mark名称运行
# 解决：
#     在测试用例方法上加@pytests.mark.webtest
# 执行：
#     -s参数：输出所有测试用例的print信息
#     -m：执行自定义标记的相关用例 pytest -s test_mark_zi_01.py    pytest -s test_mark_zi_09.py -m=webtest
#     pytest -s test_mark_zi_09.py -m apptest
#     pytest -s test_mark_zi_09.py -m "not ios"
# @pytest.mark.search
# def test_search():
#     print("test_search")
#     raise NameError
#     pass
#
# @pytest.mark.login
# def test_login():
#     print("test_login")
#     pass
# 在terminal里执行

# 多线程并行与分布式执行
# 场景：
#     测试用例1000条，一个用例执行1分钟，一个测试人员执行需要1000分钟，通常我们会用人力成本换取时间成本，加几个人一起执行，
#     时间就会缩短，如果10人一起执行需要100分钟，这就是一种并行测试，分布式场景
# 解决：
#     pytest分布式执行插件：pytest-xdist,多个CPU或主机执行，前提：用例之间都是独立的，没有先后顺序，随机都能执行，
#     可重复裕兴不影响其他用例
#     直接加-n 3是并行数量：pytest -n 3，如： pytest 文件.py -n 3

# pytest-html生成报告
# 生成报告：
#     pytest -v -s --heml=report.html - -self-contained-html



