# coding=utf-8
"""
Created on 2021-1-8
@author:Shenlei
Project:测试用例--设备列表页面未登陆状态（文本及按钮测试）
"""
import pytest
import allure
import os
from page.desired_caps.driver_app import appPage
from page.page_device.device_nologin import deviceProject
from page.page_device.device_virtual import virtualProject


@pytest.fixture(scope='function', autouse=True)
def test():
    global driver
    driver = appPage.driver()
    deviceProject(driver).login_y_n()
    deviceProject(driver).device_text()

    yield  # 相当于teardow
    driver.quit()

@allure.epic('设备列表页')
@allure.feature("设备列表页--未登陆状态")
class TestClass:

    @allure.story('未登录按钮')
    @allure.title('点击未登录按钮测试')
    def test_one(self):
        deviceProject(driver).click_button1()

    # 点击未登陆

    @allure.story('场景控制快捷入口按钮')
    @allure.title('点击场景控制快捷入口按钮测试')
    def test_two(self):
        deviceProject(driver).click_button2()

    # 点击场景控制快捷入口

    @allure.story('虚拟体验按钮')
    @allure.title('点击虚拟体验按钮测试')
    def test_three(self):
        deviceProject(driver).click_button3()
        virtualProject(driver).virtual_text()

    # 点击虚拟体验

    @allure.story('添加设备按钮')
    @allure.title('点击添加设备按钮测试')
    def test_four(self):
        deviceProject(driver).click_button4()

    # 点击添加设备

    @allure.story('右上角+按钮')
    @allure.title('点击右上角+按钮测试')
    def test_five(self):
        deviceProject(driver).click_button5()

    # 点击右上角+


if __name__ == '__main__':
    pytest.main(['--alluredir', '../report/result/', '--clean-alluredir', 'test_device_nologin.py'])
    split = 'allure generate ../report/result/ -o ../report/html --clean'
    os.system(split)
