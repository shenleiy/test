# coding=utf-8
"""
Created on 2021-2-2
@author:
Project:测试用例--设备信息（家庭管理员）
"""

import pytest
import allure
import os
from page.desired_caps.driver_app import appPage
from page.page_device.device_information import information
from common.public import Element


@pytest.fixture(scope='class', autouse=True)
def login():
    global driver
    driver = appPage.driver()
    information(driver).open()
    information(driver).check1()

    yield  # 相当于teardown
    driver.quit()


@allure.epic('设备信息')
@allure.feature("页面展示")
class TestClass:
    @allure.story('页面展示')
    @allure.title('页面展示')
    def test_show1(self):
        with allure.step("step1：判断新旧设备"):
            information(driver).check2()
        with allure.step("step1：根据新旧设备判断页面数据（有无历史故障）"):
            if information(driver).check2() == True:
                information(driver).showdevice()
            else:
                information(driver).showdevice1()


@allure.epic('设备信息')
@allure.feature("设备名称")
class TestClass2:
    @allure.story('修改设备名称')
    @allure.title('20个数字')
    def test_show1(self):
        information(driver).changename1()

    @allure.story('修改设备名称')
    @allure.title('20个汉字')
    def test_show2(self):
        information(driver).changename2()

    @allure.story('修改设备名称')
    @allure.title('22个汉字')
    def test_show3(self):
        information(driver).changename3()

    @allure.story('修改设备名称')
    @allure.title('空格')
    def test_show4(self):
        information(driver).changename4()

    @allure.story('修改设备名称')
    @allure.title('字符')
    def test_show5(self):
        information(driver).changename5()


@allure.epic('设备信息')
@allure.feature("设备SN码")
#@pytest.mark.skipif(information(driver).check1() == 1, reason="SN码已添加")
class TestClass3:
    @allure.story('设置设备SN码')
    @allure.title('空的')
    def test_addsn1(self):
        information(driver).addsn1()

    @allure.story('修改设备名称')
    @allure.title('输入汉字')
    def test_addsn2(self):
        information(driver).addsn2()

    @allure.story('设置设备SN码')
    @allure.title('输入字符')
    def test_addsn3(self):
        information(driver).addsn3()

    @allure.story('设置设备SN码')
    @allure.title('输入字母')
    def test_addsn4(self):
        information(driver).addsn4()

    @allure.story('设置设备SN码')
    @allure.title('输入数字')
    def test_addsn5(self):
        information(driver).addsn5()


@allure.epic('设备信息')
@allure.feature("设备SN码")
class TestClass4:
    @allure.story('设置设备SN码')
    @allure.title('扫码添加')
    def test_addsn6(self):
        information(driver).addsn6()

    @allure.story('设置设备SN码')
    @allure.title('取消操作')
    def test_addsn7(self):
        information(driver).addsn7()


@allure.epic('设备信息')
@allure.feature("设备SN码")
class TestClass5:
    @allure.story('设置设备SN码')
    @allure.title('再次确认-取消')
    def test_addsn8(self):
        information(driver).addsn8()

    @allure.story('设置设备SN码')
    @allure.title('再次确认-确认')
    @pytest.mark.skip(reason="一台设备sn码只能提交一次")
    def test_addsn9(self):
        information(driver).addsn9()


@allure.epic('设备信息')
@allure.feature("历史故障信息")
class TestClass6:
    @allure.title('历史故障信息查看')
    def test_history(self):
        with allure.step("step1：判断新旧设备"):
            information(driver).check2()
        with allure.step("step1：根据新旧设备判断页面数据（有无历史故障）"):
            if information(driver).check2() == True:
                information(driver).history()
            else:
                print("无故障")


@allure.epic('设备信息')
@allure.feature("移动设备")
class TestClass7:
    @allure.story('移动设备')
    @allure.title('移动设备页查看')
    def test_move1(self):
        information(driver).move1()


@allure.epic('设备信息')
@allure.feature("移动设备")
class TestClass8:
    @allure.story('移动设备')
    @allure.title('移动')
    def test_move1(self):
        information(driver).move2()


if __name__ == '__main__':
    pytest.main(['-s', 'test_device_information.py::TestClass3'])
