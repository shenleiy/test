# coding=utf-8
"""
Created on 2021-2-3
@author:Wangwanqin
Project:测试用例--房间管理
"""

import pytest
import allure
import os
from page.desired_caps.driver_app import appPage
from page.page_family.room_list import roomList
from common.public import Element


@pytest.fixture(scope='class', autouse=True)
def login():
    global driver
    driver = appPage.driver()
    roomList(driver).room()
    yield
    driver.quit()


@allure.epic('房间管理')
@allure.feature("新增房间")
class TestClass:
    @allure.story('房间名称')
    @allure.title('房间名称，未输入')
    def test_room1(self):
        roomList(driver).roomName1()

    @allure.story('房间名称')
    @allure.title('输入汉字')
    def test_room2(self):
        roomList(driver).roomName2()

    @allure.story('房间名称')
    @allure.title('输入超过20位汉字')
    def test_room3(self):
        roomList(driver).roomName3()

    @allure.story('房间名称')
    @allure.title('输入字符')
    def test_room4(self):
        roomList(driver).roomName4()

    @allure.story('房间名称')
    @allure.title('输入字母')
    def test_room5(self):
        roomList(driver).roomName5()

    @allure.story('房间名称')
    @allure.title('输入数字')
    def test_room6(self):
        roomList(driver).roomName6()


@allure.epic('房间管理')
@allure.feature("具体房间")
class TestClass2:
    @allure.story('修改房间名称')
    @allure.title('修改房间名称')
    def test_roomName8(self):
        roomList(driver).roomName8()


@allure.epic('房间管理')
@allure.feature("具体房间")
class TestClass3:
    @allure.story('删除房间')
    @allure.title('取消删除')
    def test_roomName9(self):
        roomList(driver).roomName9()


@allure.epic('房间管理')
@allure.feature("具体房间")
class TestClass4:
    @allure.story('删除房间')
    @allure.title('确认删除')
    def test_roomName10(self):
        roomList(driver).roomName10()


@allure.epic('房间管理')
@allure.feature("具体房间")
class TestClass5:
    @allure.story('设备')
    @allure.title('查看设备[仅查看有无设备]')
    def test_roomName11(self):
        roomList(driver).roomName11()


@allure.epic('房间管理')
@allure.feature("具体房间")
class TestClass6:
    @allure.story('设备')
    @allure.title('添加设备')
    def test_roomName12(self):
        roomList(driver).roomName12()


@allure.epic('房间管理')
@allure.feature("新增房间")
class TestClass7:
    @allure.story('房间数量')
    @allure.title('不断新增')
    def test_roomName13(self):
        roomList(driver).roomName13()


@allure.epic('房间管理')
@allure.feature("具体房间")
class TestClass8:
    @allure.story('删除房间')
    @allure.title('不断删除房间直至全部删除')
    def test_roomName14(self):
        roomList(driver).roomName14()


if __name__ == '__main__':
    pytest.main(['-s', 'test_room_list.py::TestClass8'])
    #pytest.main(['--alluredir', '../report/result/', '--clean-alluredir', 'test_room_list.py'])
    #split = 'allure serve ../report/result/ -o ../report/html --clean'
    #os.system(split)
