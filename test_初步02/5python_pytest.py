# # # 测试文件
# # 1.test_*.py
# # 2.*_test.py
# # 用例识别
# Test*包含的所有test_*的所有方法（测试类不能带有__init__方法）
# 不在class中的所有test_*方法
# pytest也可以执行unittest框架写的用例和方法
import pytest
class TestDemo():
    def test_one(self):
        print("开始执行 test_one方法")
        x = 'this'
        assert 'h' in x

    def test_two(self):
        print("开始执行 test_two方法")
        x = 'hello'
        assert 'e' in x

    def test_three(self):
        print("开始执行 test_three方法")
        a = 'hello'
        b = 'hello world'
        assert a in b

if __name__ == '__main__':
    # pytest.main("-v -x TestDemo")
    pytest.main(['-v','-s','TestDemo'])