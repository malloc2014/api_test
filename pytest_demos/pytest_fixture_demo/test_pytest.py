import pytest

class TestDemo():
    def test_one(self):
        print("开始执行test_one 方法")
        x = 'this'
        assert 'h' in x
        # pytest.assume('h' not in x)
        # pytest.assume(1 == 2)
        # pytest.assume('x' in 'xxx')
        # pytest.assume('hi' not in 'hint')

    def test_twwo(self):
        print("开始执行test_two 方法")
        x = 'hello'
        assert 'e' in x

    def test_three(self):
        print("开始执行test_three 方法")
        a = 'hello'
        b = 'hello world'
        assert a not in b


class TestDemo1():
    def test_a(self):
        print("开始执行test_a 方法")
        x = 'this'
        assert 'h' in x

    def test_b(self):
        print("开始执行test_b 方法")
        x = 'hello'
        assert 'e' in x

    def test_c(self):
        print("开始执行test_c 方法")
        a = 'hello'
        b = 'hello world'
        assert a not in b

if  __name__ == '__main__':
    pytest.main("-v -x TestDemo")