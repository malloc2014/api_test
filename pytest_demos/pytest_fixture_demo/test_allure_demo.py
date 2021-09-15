# encoding: utf-8
"""
@File    : test_allure_demo.py
@Author  : Renlb
@Time    : 2020/4/13 5:05 PM
@Desc    :
"""
import pytest
import allure

@allure.step("步骤1：打开百度")
def step_1():
    print("111")


@allure.step("步骤2：输入关键字")
def step_2():
    print("222")


@allure.feature("搜索")
class TestEditPage():
    @allure.story("百度搜索")
    def test_1(self):
        '''这是测试百度搜索'''
        step_1()
        step_2()
        print("百度一下，你就知道")

    @allure.story("谷歌搜索")
    def test_2(self):
        '''这是测试谷歌搜索'''
        assert 1 == 2, "搜索失败"

if __name__ == "__main__":
    # pytest.main()
    # pytest.main(['--alluredir', 'report/result', 'test_allure_demo.py'])
    pytest.main(['-vs', './test_allure_demo.py', '--alluredir', './report/xml'])



