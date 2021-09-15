import pytest
import sys

# @pytest.mark.parametrize("test_input, expected", [("3+5", 8), ("2+5", 7), ("4+5", 10)])
# def test_eval(test_input, expected):
#     #eval 将字符串当有效表达式来求值，并返回结果
#     assert eval(test_input) == expected

#参数组合
# @pytest.mark.parametrize("x", [1, 2])
# @pytest.mark.parametrize("y", [8, 9, 10])
# def test_(x, y):
#     print(f"测试数据组合x：{x}, y:{y}")

#方法名称作为参数
test_user_data = ['Tom', 'Jerry']
@pytest.fixture(scope="module")
def login_r(request):
    user = request.param
    print(f"\n 打开首页准备登录，登录用户：{user}")
    return user

# @pytest.mark.skip("这次不执行")
# @pytest.mark.skipif(sys.platform == "win32", reason = "不在mac上运行")
@pytest.mark.xfail
@pytest.mark.webtest
@pytest.mark.parametrize("login_r", test_user_data, indirect=True)
def test_login(login_r):
    a = login_r
    print(f"测试用例中的login的返回值：{a}")
    assert a !=""



if __name__ == "__main__":
    pytest.main("-v")