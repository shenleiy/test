# coding=utf-8
"""
Created on 2021-1-15
@author:Shenlei
Project:测试用例--个人资料页面（文本及按钮测试）
"""
import pytest
import allure
import os
from page.desired_caps.driver_app import appPage
from page.page_my.person import myPerson


@pytest.fixture(scope='function', autouse=True)
def test():
    global driver
    driver = appPage.driver()
    myPerson(driver).login_y_n()
    myPerson(driver).click_button0()

    yield  # 相当于teardow
    driver.quit()


@allure.epic('个人资料页')
@allure.feature('头像')
class TestClass1:
    @allure.story('修改头像')
    @allure.title('修改头像点击取消按钮测试')
    def test_1(self):
        myPerson(driver).click_button1()


@allure.epic('个人资料页')
@allure.feature('昵称')
class TestClass2:
    @allure.story('默认昵称')
    @allure.title('默认昵称点击取消按钮测试')
    def test_1(self):
        myPerson(driver).click_button3()
        myPerson(driver).click_button04()

    @allure.story('默认昵称')
    @allure.title('默认昵称点击确认按钮测试')
    def test_2(self):
        myPerson(driver).click_button3()
        myPerson(driver).click_button7()

    @allure.story('昵称未空')
    @allure.title('昵称未空点击取消按钮测试')
    def test_3(self):
        myPerson(driver).click_button3()
        myPerson(driver).click_button8()
        myPerson(driver).click_button4()

    @allure.story('昵称未空')
    @allure.title('昵称未空点击确认按钮测试')
    def test_4(self):
        myPerson(driver).click_button3()
        myPerson(driver).click_button8()
        myPerson(driver).click_button5()

    @allure.story('1-20位昵称')
    @allure.title('1-20位昵称点击取消按钮测试')
    def test_5(self):
        myPerson(driver).click_button3()
        myPerson(driver).click_button4()

    @allure.story('1-20位昵称')
    @allure.title('1-20位昵称点击确认按钮测试')
    def test_6(self):
        myPerson(driver).click_button3()
        myPerson(driver).click_button03()

    @allure.story('超20位昵称')
    @allure.title('输入超20位昵称测试')
    def test_7(self):
        myPerson(driver).click_button3()
        myPerson(driver).click_button003()


@allure.epic('个人资料页')
@allure.feature('姓名')
class TestClass3:
    @allure.story('默认姓名')
    @allure.title('默认姓名点击取消按钮测试')
    def test_1(self):
        myPerson(driver).click_button9()
        myPerson(driver).click_button04()

    @allure.story('默认姓名')
    @allure.title('默认姓名点击确认按钮测试')
    def test_2(self):
        myPerson(driver).click_button9()
        myPerson(driver).click_button7()

    @allure.story('姓名为空')
    @allure.title('姓名为空点击取消按钮测试')
    def test_3(self):
        myPerson(driver).click_button9()
        myPerson(driver).click_button11()
        myPerson(driver).click_button4()

    @allure.story('姓名为空')
    @allure.title('姓名为空点击确认按钮测试')
    def test_4(self):
        myPerson(driver).click_button9()
        myPerson(driver).click_button11()
        myPerson(driver).click_button10()

    @allure.story('1-20位姓名')
    @allure.title('1-20位姓名点击取消按钮测试')
    def test_5(self):
        myPerson(driver).click_button9()
        myPerson(driver).click_button4()

    @allure.story('1-20位姓名')
    @allure.title('1-20位姓名点击确认按钮测试')
    def test_6(self):
        myPerson(driver).click_button9()
        myPerson(driver).click_button09()

    @allure.story('超20位姓名')
    @allure.title('输入超20位姓名测试')
    def test_7(self):
        myPerson(driver).click_button9()
        myPerson(driver).click_button009()


@allure.epic('个人资料页')
@allure.feature('性别')
class TestClass4:
    @allure.story('性别男')
    @allure.title('点击性别男按钮测试')
    def test_1(self):
        myPerson(driver).click_button12()

    @allure.story('性别女')
    @allure.title('点击性别女按钮测试')
    def test_2(self):
        myPerson(driver).click_button13()


@allure.epic('个人资料页')
@allure.feature('出生日期')
class TestClass5:
    @allure.story('默认当前日期')
    @allure.title('当前日期点击确定测试')
    def test_1(self):
        myPerson(driver).click_button14()

    @allure.story('默认当前日期')
    @allure.title('当前日期点击取消测试')
    def test_2(self):
        myPerson(driver).click_button15()


@allure.epic('个人资料页')
@allure.feature('所在地区')
class TestClass6:
    @allure.story('选择所在地区')
    @allure.title('上下滑动选择所在地区测试')
    def test_1(self):
        myPerson(driver).click_button16()


@allure.epic('个人资料页')
@allure.feature('返回')
class TestClass7:
    @allure.story('返回按钮')
    @allure.title('点击返回按钮，跳转至我的页面测试')
    def test_1(self):
        myPerson(driver).click_button2()


if __name__ == '__main__':
    pytest.main(['--alluredir', '../report/result/', '--clean-alluredir', 'test_person.py', '-v', '-s'])
    split = 'allure generate ../report/result/ -o ../report/html --clean'
    os.system(split)
