# coding=utf-8
"""
Created on 2021-1-9
@author:Shenlei
Project:测试用例--注册登录页面(文本及按钮测试）
"""
import pytest
import allure
import os
from page.desired_caps.driver_app import appPage
from page.page_my.login_register import loginProject


@pytest.fixture(scope='function', autouse=True)
def test():
    global driver
    driver = appPage.driver()
    loginProject(driver).login_y_n()

    yield  # 相当于teardow
    driver.quit()


@allure.epic('注册页')
@allure.feature("手机号注册")
class TestClass:
    @allure.story('密码登录按钮')
    @allure.title('点击密码登录按钮，切换到密码登录页面测试')
    def test1(self):
        loginProject(driver).click_button1()  # 进入手机号登录页面

    # 点击密码登录

    # def test_two(self):
    #     driver = appPage.driver()
    #     loginProject(driver).login_y_n()
    #     loginProject(driver).click_button2()

    # 点击QQ登录

    # def test_three(self):
    #     driver = appPage.driver()
    #     loginProject(driver).login_y_n()
    #     loginProject(driver).click_button3()

    # 点击微信登录

    @allure.story('用户协议按钮')
    @allure.title('点击用户协议测试')
    def test2(self):
        loginProject(driver).click_button4()

    # 点击用户协议

    @allure.story('隐私政策按钮')
    @allure.title('点击隐私政策测试')
    def test3(self):
        loginProject(driver).click_button5()

    # 点击隐私政策

    @allure.story('注册按钮')
    @allure.title('勾选同意，验证码错误点击注册失败测试')
    def test4(self):
        loginProject(driver).click_button11()
        loginProject(driver).click_button6()
        loginProject(driver).click_button7()
        loginProject(driver).click_button8()

    # 点击注册
    @allure.story('注册按钮')
    @allure.title('未勾选同意，验证码错误点击注册失败测试')
    def test4(self):
        loginProject(driver).click_button6()
        loginProject(driver).click_button7()
        loginProject(driver).click_button12()

    # 点击注册

    @allure.story('返回按钮')
    @allure.title('点击返回键，页面跳转到设备页测试')
    def test5(self):
        loginProject(driver).click_button9()

    # 点击返回


if __name__ == '__main__':
    pytest.main(['--alluredir', '../report/result/', '--clean-alluredir', 'test_login_register.py'])
    split = 'allure generate ../report/result/ -o ../report/html --clean'
    os.system(split)
