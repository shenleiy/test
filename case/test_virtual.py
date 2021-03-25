# coding=utf-8
"""
Created on 2021-1-23
@author:Shenlei
Project:测试用例--虚拟体验（文本及按钮测试）
"""
import pytest
import allure
import os
from page.desired_caps.driver_app import appPage
from page.page_device.device_virtual import virtualProject


@pytest.fixture(scope='function', autouse=True)
def test():
    global driver
    driver = appPage.driver()
    virtualProject(driver).login_y_n()

    yield  # 相当于teardow
    driver.quit()


@allure.epic('设备列表页')
@allure.feature("虚拟体验")
class TestClass:
    @allure.story('虚拟体验UI')
    @allure.title('虚拟体验UI显示文本测试')
    def test1(self):
        virtualProject(driver).virtual_text()

    @allure.story('制冷模式')
    @allure.title('制冷模式下点击舒风')
    def test2(self):
        virtualProject(driver).click_button1()

    @allure.story('制冷模式')
    @allure.title('制冷模式下点击电加热')
    def test3(self):
        virtualProject(driver).click_button8()

    # @allure.story('制热模式')
    # @allure.title('制热模式下点击ECO')
    # def test4(self):
    #     virtualProject(driver).click_button2()
    #     virtualProject(driver).click_button6()

    @allure.story('制热模式')
    @allure.title('制热模式下点击舒风')
    def test5(self):
        virtualProject(driver).click_button2()
        virtualProject(driver).click_button7()

    # @allure.story('除湿模式')
    # @allure.title('除湿模式下点击ECO')
    # def test6(self):
    #     virtualProject(driver).click_button3()
    #     virtualProject(driver).click_button6()

    @allure.story('除湿模式')
    @allure.title('除湿模式下点击舒风')
    def test7(self):
        virtualProject(driver).click_button3()
        virtualProject(driver).click_button7()

    @allure.story('除湿模式')
    @allure.title('除湿模式下点击电加热')
    def test8(self):
        virtualProject(driver).click_button3()
        virtualProject(driver).click_button8()

    # @allure.story('送风模式')
    # @allure.title('送风模式下点击ECO')
    # def test9(self):
    #     virtualProject(driver).click_button4()
    #     virtualProject(driver).click_button6()

    @allure.story('送风模式')
    @allure.title('送风模式下点击舒风')
    def test10(self):
        virtualProject(driver).click_button4()
        virtualProject(driver).click_button7()

    @allure.story('送风模式')
    @allure.title('送风模式下点击电加热')
    def test11(self):
        virtualProject(driver).click_button4()
        virtualProject(driver).click_button8()

    @allure.story('送风模式')
    @allure.title('送风模式下点击电加热')
    def test12(self):
        virtualProject(driver).click_button4()
        virtualProject(driver).click_button9()

    # @allure.story('自动模式')
    # @allure.title('自动模式下点击ECO')
    # def test13(self):
    #     virtualProject(driver).click_button5()
    #     virtualProject(driver).click_button6()

    @allure.story('自动模式')
    @allure.title('自动模式下点击舒风')
    def test14(self):
        virtualProject(driver).click_button5()
        virtualProject(driver).click_button7()

    @allure.story('自动模式')
    @allure.title('自动模式下点击电加热')
    def test15(self):
        virtualProject(driver).click_button5()
        virtualProject(driver).click_button8()

    @allure.story('高阶功能')
    @allure.title('开机状态下点击睡眠diy功能')
    def test16(self):
        virtualProject(driver).click_button11()

    @allure.story('高阶功能')
    @allure.title('开机状态下点击定时功能')
    def test17(self):
        virtualProject(driver).click_button12()

    @allure.story('高阶功能')
    @allure.title('开机状态下点击设备运行日志功能')
    def test18(self):
        virtualProject(driver).click_button13()

    @allure.story('高阶功能')
    @allure.title('开机状态下点击清洁功能')
    def test19(self):
        virtualProject(driver).click_button15()

    @allure.story('高阶功能')
    @allure.title('开机状态下点击智能省电功能')
    def test20(self):
        virtualProject(driver).click_button16()

    @allure.story('高阶功能')
    @allure.title('关机状态下点击定时功能')
    def test21(self):
        virtualProject(driver).click_button14()
        virtualProject(driver).click_button12()

    @allure.story('高阶功能')
    @allure.title('关机状态下点击设备运行日志功能')
    def test22(self):
        virtualProject(driver).click_button14()
        virtualProject(driver).click_button13()

    @allure.story('高阶功能')
    @allure.title('关机状态下点击清洁功能')
    def test23(self):
        virtualProject(driver).click_button14()
        virtualProject(driver).click_button15()

    @allure.story('高阶功能')
    @allure.title('关机状态下点击智能省电功能')
    def test24(self):
        virtualProject(driver).click_button14()
        virtualProject(driver).click_button16()

    @allure.story('童锁功能')
    @allure.title('开启童锁后随即点击任意按钮')
    def test25(self):
        virtualProject(driver).click_button10()


if __name__ == '__main__':
    pytest.main(['--alluredir', '../report/result/', '--clean-alluredir', 'test_virtual.py'])
    split = 'allure generate ../report/result/ -o ../report/html --clean'
    os.system(split)
