# coding=utf-8
"""
Created on 2021-1-6
@author:Shenlei
Project:测试用例--启动引导页和隐私声明（文本及按钮测试）
"""
import pytest
import allure
import os
from page.desired_caps.driver_app2 import appPage
from page.desired_caps import boot


@pytest.fixture(scope='function', autouse=True)
def test():
    global driver
    driver = appPage.driver()

    yield  # 相当于teardow
    driver.quit()


@allure.epic('引导页')
@allure.feature("隐私声明")
class TestClass:

    @allure.story('不同意按钮')
    @allure.title('点击不同意隐私声明按钮测试')
    def test_one(self):
        boot.BootProject(driver).click_button3()

    @allure.story('同意按钮')
    @allure.title('点击同意隐私声明按钮测试')
    def test_two(self):
        boot.BootProject(driver).click_button2()
        boot.BootProject(driver).boot()
        boot.BootProject(driver).click_button4()


if __name__ == '__main__':
    pytest.main(['--alluredir', '../report/result/', '--clean-alluredir', '-v', 'test_boot.py'])
    split = 'allure generate ../report/result/ -o ../report/html --clean'
    os.system(split)
