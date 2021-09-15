import pytest

def test_func():
    print("运行func")

class TestDomo():
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

if __name__ == '__main__':
    pytest.main("-v -x test_pytestdemo")
    # pytest.main(['-v', '-x', 'TestDomo'])
    # pytest.main()