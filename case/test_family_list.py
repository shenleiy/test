# coding=utf-8
"""
Created on 2021-1-12
@author:Shenlei
Project:测试用例--家庭列表页面(文本及按钮测试）
"""

import pytest
import allure
import os
from page.desired_caps.driver_app import appPage
from page.page_family.family_list import familyList


@pytest.fixture(scope='function', autouse=True)
def test():
    global driver
    driver = appPage.driver()
    familyList(driver).login_y_n()

    yield  # 相当于teardow
    driver.quit()


@allure.epic('家庭列表页')
@allure.feature("返回")
class TestClass1:
    @allure.story('返回按钮')
    @allure.title('点击返回键，页面跳转到设备页测试')
    def test1(self):
        familyList(driver).click_button1()

    # 点击返回


@allure.epic('家庭列表页')
@allure.feature("家庭名称")
class TestClass2:
    @allure.story('家庭名称为空')
    @allure.title('未输入家庭名称点击确认测试')
    def test1(self):
        familyList(driver).click_button9()
        familyList(driver).click_button4()

    # 未输入家庭名称点击确认

    @allure.story('家庭名称为空')
    @allure.title('未输入家庭名称点击取消测试')
    def test2(self):
        familyList(driver).click_button9()
        familyList(driver).click_button3()

    # 未输入家庭名称点击取消

    @allure.story('1-20位家庭名称')
    @allure.title('1-20位家庭名称点击确认测试')
    def test3(self):
        familyList(driver).click_button9()
        familyList(driver).click_button2()
        familyList(driver).click_button5()

    # 输入家庭名称点击确认

    @allure.story('1-20位家庭名称')
    @allure.title('1-20位家庭名称点击取消测试')
    def test4(self):
        familyList(driver).click_button9()
        familyList(driver).click_button2()
        familyList(driver).click_button3()

    # 输入家庭名称点击取消

    @allure.story('超20位家庭名称')
    @allure.title('输入超20位家庭名称测试')
    def test5(self):
        familyList(driver).click_button9()
        familyList(driver).click_button10()

    # 输入家庭名称点击取消

    @allure.story('清除家庭名称')
    @allure.title('输入家庭名称点击清除测试')
    def test6(self):
        familyList(driver).click_button9()
        familyList(driver).click_button2()
        familyList(driver).click_button6()

    # 清除家庭名称

@allure.epic('家庭列表页')
@allure.feature("选择家庭")
class TestClass3:
    @allure.story('页面跳转')
    @allure.title('点击家庭名称，进入家庭设置页测试')
    def test1(self):
        familyList(driver).click_button7()

    # 进入家庭设置页

    @allure.story('页面跳转')
    @allure.title('勾选家庭，进入设备列表页测试')
    def test2(self):
        familyList(driver).click_button8()

    # 进入设备列表页


if __name__ == '__main__':
    pytest.main(['-s', 'test_family_list.py'])
