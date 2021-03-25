# coding=utf-8
"""
Created on 2021-1-18
@author:Shenlei
Project:测试用例--设置页面(文本及按钮测试）
"""
import pytest
import allure
import os
from page.desired_caps.driver_app import appPage
from page.page_my.setting import mySetting


@pytest.fixture(scope='function', autouse=True)
def test():
    global driver
    driver = appPage.driver()
    mySetting(driver).login_y_n()

    yield  # 相当于teardow
    driver.quit()


@allure.epic('设置页')
@allure.feature("界面")
class TestClass1:
    @allure.story('设置页UI')
    @allure.title('设置页UI显示文本测试')
    def test1(self):
        mySetting(driver).click_button1()


@allure.epic('设置页')
@allure.feature("账号安全")
class TestClass2:
    @allure.story('账号安全UI')
    @allure.title('账号安全UI显示文本测试')
    def test1(self):
        mySetting(driver).click_button01()
        mySetting(driver).click_button2()


@allure.epic('设置页')
@allure.feature("消息免打扰")
class TestClass3:
    @allure.story('免打扰开关按钮')
    @allure.title('消息免打扰开启和关闭切换测试')
    def test1(self):
        mySetting(driver).click_button01()
        mySetting(driver).click_button3()


@allure.epic('设置页')
@allure.feature("设备展示方式")
class TestClass4:
    @allure.story('设备展示按钮')
    @allure.title('列表模式和宫格模式切换测试')
    def test1(self):
        mySetting(driver).click_button01()
        mySetting(driver).click_button4()


@allure.epic('设置页')
@allure.feature("深色模式")
class TestClass5:
    @allure.story('深色模式按钮')
    @allure.title('普通模式和深色模式切换测试')
    def test1(self):
        mySetting(driver).click_button01()
        mySetting(driver).click_button5()


@allure.epic('设置页')
@allure.feature("去评价")
class TestClass6:
    @allure.story('去吐槽按钮')
    @allure.title('点击去吐槽按钮，切换到意见反馈页面测试')
    def test1(self):
        mySetting(driver).click_button01()
        mySetting(driver).click_button6()

    @allure.story('取消按钮')
    @allure.title('点击取消按钮，关闭去评价弹框测试')
    def test2(self):
        mySetting(driver).click_button01()
        mySetting(driver).click_button7()


@allure.epic('设置页')
@allure.feature("关于奥云家")
class TestClass7:
    @allure.story('关于奥云家UI')
    @allure.title('关于奥云家UI显示文本测试')
    def test1(self):
        mySetting(driver).click_button01()
        mySetting(driver).click_button9()

    @allure.story('数据隐私声明按钮')
    @allure.title('点击数据隐私声明按钮，切换到奥克斯集团隐私政策页面测试')
    def test2(self):
        mySetting(driver).click_button01()
        mySetting(driver).click_button10()

    @allure.story('官网按钮')
    @allure.title('点击官网按钮，切换到奥克斯空调官网页面测试')
    def test3(self):
        mySetting(driver).click_button01()
        mySetting(driver).click_button11()

    @allure.story('服务热线按钮')
    @allure.title('点击服务热线按钮，切换到手机号拨打页面测试')
    def test4(self):
        mySetting(driver).click_button01()
        mySetting(driver).click_button12()

    @allure.story('分享奥云家按钮')
    @allure.title('点击分享奥云家按钮，显示奥云家分享方式测试')
    def test5(self):
        mySetting(driver).click_button01()
        mySetting(driver).click_button13()


@allure.epic('设置页')
@allure.feature("退出登录")
class TestClass8:
    @allure.story('取消按钮')
    @allure.title('点击取消按钮，关闭退出登录弹框测试')
    def test1(self):
        mySetting(driver).click_button01()
        mySetting(driver).click_button14()

    @allure.story('确定按钮')
    @allure.title('点击确定按钮，账号退出登录测试')
    def test2(self):
        mySetting(driver).click_button01()
        mySetting(driver).click_button15()


if __name__ == '__main__':
    pytest.main(['--alluredir', '../report/result/', '--clean-alluredir', 'test_setting.py', '-v'])
    split = 'allure generate ../report/result/ -o ../report/html --clean'
    os.system(split)
