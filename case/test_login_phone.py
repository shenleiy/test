# coding=utf-8
"""
Created on 2021-1-9
@author:Shenlei
Project:测试用例--手机号登录页面(文本及按钮测试）
"""

import pytest
import allure
import os
from page.desired_caps.driver_app import appPage
from page.page_my.login_phone import loginPhone


@pytest.fixture(scope='function', autouse=True)
def test():
    global driver
    driver = appPage.driver()
    loginPhone(driver).login_y_n()

    yield  # 相当于teardow
    driver.quit()


@allure.epic('登录页')
@allure.feature("手机号登录")
class TestClass:
    @allure.story('验证码登录按钮')
    @allure.title('点击验证码登录按钮，切换到验证码登录页面测试')
    def test1(self):
        loginPhone(driver).click_button1()

    # 点击验证码登录

    @allure.story('忘记密码按钮')
    @allure.title('未输入手机号时点击忘记密码按钮测试')
    def test2(self):
        loginPhone(driver).click_button2()

    # 未输入手机号时点击忘记密码

    @allure.story('忘记密码按钮')
    @allure.title('输入手机号时点击忘记密码按钮测试')
    def test3(self):
        loginPhone(driver).click_button02()

    # 输入手机号时点击忘记密码

    @allure.story('清除按钮')
    @allure.title('输入手机号时点击清除按钮测试')
    def test4(self):
        loginPhone(driver).click_button3()

    # 点击清除手机号

    @allure.story('用户协议按钮')
    @allure.title('点击用户协议测试')
    def test5(self):
        loginPhone(driver).click_button4()

    # 点击用户协议

    @allure.story('隐私政策按钮')
    @allure.title('点击隐私政策测试')
    def test6(self):
        loginPhone(driver).click_button5()

    # 点击隐私政策

    @allure.story('手机账号登录--勾选同意')
    @allure.title('正确账号密码点击登录测试')
    def test7(self):
        loginPhone(driver).click_button11()
        loginPhone(driver).click_button10()

    # 正确账号密码点击登录

    @allure.story('手机账号登录--勾选同意')
    @allure.title('错误账号密码点击登录测试')
    def test8(self):
        loginPhone(driver).click_button11()
        loginPhone(driver).click_button6()

    # 错误账号密码点击登录

    @allure.story('手机账号登录--未勾选同意')
    @allure.title('正确账号密码点击登录测试')
    def test9(self):
        loginPhone(driver).click_button10()
        loginPhone(driver).click_button12()

    # 正确账号密码点击登录

    @allure.story('显密按钮')
    @allure.title('输入账号密码点击显密测试')
    def test10(self):
        loginPhone(driver).click_button7()

    # 输入密码点击显密

    @allure.story('显密按钮')
    @allure.title('未输入账号密码点击显密测试')
    def test11(self):
        loginPhone(driver).click_button8()

    # 未输入密码是点击显密

    @allure.story('返回按钮')
    @allure.title('点击返回键，页面跳转到设备页测试')
    def test12(self):
        loginPhone(driver).click_button9()

    # 点击返回键


if __name__ == '__main__':
    pytest.main(['-s', 'test_login_phone.py'])
