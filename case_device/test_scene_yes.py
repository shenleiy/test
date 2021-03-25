# coding=utf-8
"""
Created on 2021-1-29
@author:Shenlei
Project:测试用例--场景有设备（文本及按钮测试）
"""

import pytest
import allure
import os
from page.desired_caps.driver_app import appPage
from page.page_scene.scene_recommend import sceneRecommend
from page.page_scene.scene_newly import sceneNewly


@pytest.fixture(scope='function', autouse=True)  # 相当于setup
def start():
    global driver
    driver = appPage.driver()
    sceneRecommend(driver).login_y_n()

    yield  # 相当于teardown
    sceneRecommend(driver).click_button18()
    sceneRecommend(driver).click_button19()  # 执行场景后删除新增的场景
    driver.quit()


@allure.epic('场景推荐页')
@allure.feature("回家(手动)")
class TestClass:
    @allure.story('有设备状态')
    @allure.title('点击继续添加设备创建关机场景测试')
    def test1(self):
        sceneRecommend(driver).click_button1()
        sceneRecommend(driver).click_button6()
        sceneRecommend(driver).click_button11()
        sceneRecommend(driver).click_button17()

    @allure.story('有设备状态')
    @allure.title('点击继续添加设备创建开机制冷场景测试')
    def test2(self):
        sceneRecommend(driver).click_button1()
        sceneRecommend(driver).click_button6()
        sceneRecommend(driver).click_button12()
        sceneRecommend(driver).click_button17()

    @allure.story('有设备状态')
    @allure.title('点击继续添加设备创建开机制热场景测试')
    def test3(self):
        sceneRecommend(driver).click_button1()
        sceneRecommend(driver).click_button6()
        sceneRecommend(driver).click_button13()
        sceneRecommend(driver).click_button17()

    @allure.story('有设备状态')
    @allure.title('点击继续添加设备创建开机除湿场景测试')
    def test4(self):
        sceneRecommend(driver).click_button1()
        sceneRecommend(driver).click_button6()
        sceneRecommend(driver).click_button14()
        sceneRecommend(driver).click_button17()

    @allure.story('有设备状态')
    @allure.title('点击继续添加设备创建开机送风场景测试')
    def test5(self):
        sceneRecommend(driver).click_button1()
        sceneRecommend(driver).click_button6()
        sceneRecommend(driver).click_button15()
        sceneRecommend(driver).click_button17()

    @allure.story('有设备状态')
    @allure.title('点击继续添加设备创建开机自动场景测试')
    def test6(self):
        sceneRecommend(driver).click_button1()
        sceneRecommend(driver).click_button6()
        sceneRecommend(driver).click_button16()
        sceneRecommend(driver).click_button17()

    @allure.story('有设备状态')
    @allure.title('点击选择设备创建关机场景测试')
    def test7(self):
        sceneRecommend(driver).click_button1()
        sceneRecommend(driver).click_button8()
        sceneRecommend(driver).click_button11()
        sceneRecommend(driver).click_button17()

    @allure.story('有设备状态')
    @allure.title('点击选择设备创建开机制冷场景测试')
    def test8(self):
        sceneRecommend(driver).click_button1()
        sceneRecommend(driver).click_button8()
        sceneRecommend(driver).click_button12()
        sceneRecommend(driver).click_button17()

    @allure.story('有设备状态')
    @allure.title('点击选择设备创建开机制热场景测试')
    def test9(self):
        sceneRecommend(driver).click_button1()
        sceneRecommend(driver).click_button8()
        sceneRecommend(driver).click_button13()
        sceneRecommend(driver).click_button17()

    @allure.story('有设备状态')
    @allure.title('点击选择设备创建开机除湿场景测试')
    def test10(self):
        sceneRecommend(driver).click_button1()
        sceneRecommend(driver).click_button8()
        sceneRecommend(driver).click_button14()
        sceneRecommend(driver).click_button17()

    @allure.story('有设备状态')
    @allure.title('点击选择设备创建开机送风场景测试')
    def test11(self):
        sceneRecommend(driver).click_button1()
        sceneRecommend(driver).click_button8()
        sceneRecommend(driver).click_button15()
        sceneRecommend(driver).click_button17()

    @allure.story('有设备状态')
    @allure.title('点击选择设备创建开机自动场景测试')
    def test12(self):
        sceneRecommend(driver).click_button1()
        sceneRecommend(driver).click_button8()
        sceneRecommend(driver).click_button16()
        sceneRecommend(driver).click_button17()


@allure.epic('场景推荐页')
@allure.feature("离家(手动)")
class TestClass1:
    @allure.story('有设备状态')
    @allure.title('点击继续添加设备创建关机场景测试')
    def test1(self):
        sceneRecommend(driver).click_button2()
        sceneRecommend(driver).click_button6()
        sceneRecommend(driver).click_button11()
        sceneRecommend(driver).click_button17()

    @allure.story('有设备状态')
    @allure.title('点击继续添加设备创建开机制冷场景测试')
    def test2(self):
        sceneRecommend(driver).click_button2()
        sceneRecommend(driver).click_button6()
        sceneRecommend(driver).click_button12()
        sceneRecommend(driver).click_button17()

    @allure.story('有设备状态')
    @allure.title('点击继续添加设备创建开机制热场景测试')
    def test3(self):
        sceneRecommend(driver).click_button2()
        sceneRecommend(driver).click_button6()
        sceneRecommend(driver).click_button13()
        sceneRecommend(driver).click_button17()

    @allure.story('有设备状态')
    @allure.title('点击继续添加设备创建开机除湿场景测试')
    def test4(self):
        sceneRecommend(driver).click_button2()
        sceneRecommend(driver).click_button6()
        sceneRecommend(driver).click_button14()
        sceneRecommend(driver).click_button17()

    @allure.story('有设备状态')
    @allure.title('点击继续添加设备创建开机送风场景测试')
    def test5(self):
        sceneRecommend(driver).click_button2()
        sceneRecommend(driver).click_button6()
        sceneRecommend(driver).click_button15()

    @allure.story('有设备状态')
    @allure.title('点击继续添加设备创建开机自动场景测试')
    def test6(self):
        sceneRecommend(driver).click_button2()
        sceneRecommend(driver).click_button6()
        sceneRecommend(driver).click_button16()
        sceneRecommend(driver).click_button17()

    @allure.story('有设备状态')
    @allure.title('点击选择设备创建关机场景测试')
    def test7(self):
        sceneRecommend(driver).click_button2()
        sceneRecommend(driver).click_button8()
        sceneRecommend(driver).click_button11()
        sceneRecommend(driver).click_button17()

    @allure.story('有设备状态')
    @allure.title('点击选择设备创建开机制冷场景测试')
    def test8(self):
        sceneRecommend(driver).click_button2()
        sceneRecommend(driver).click_button8()
        sceneRecommend(driver).click_button12()
        sceneRecommend(driver).click_button17()

    @allure.story('有设备状态')
    @allure.title('点击选择设备创建开机制热场景测试')
    def test9(self):
        sceneRecommend(driver).click_button2()
        sceneRecommend(driver).click_button8()
        sceneRecommend(driver).click_button13()
        sceneRecommend(driver).click_button17()

    @allure.story('有设备状态')
    @allure.title('点击选择设备创建开机除湿场景测试')
    def test10(self):
        sceneRecommend(driver).click_button2()
        sceneRecommend(driver).click_button8()
        sceneRecommend(driver).click_button14()
        sceneRecommend(driver).click_button17()

    @allure.story('有设备状态')
    @allure.title('点击选择设备创建开机送风场景测试')
    def test11(self):
        sceneRecommend(driver).click_button2()
        sceneRecommend(driver).click_button8()
        sceneRecommend(driver).click_button15()
        sceneRecommend(driver).click_button17()

    @allure.story('有设备状态')
    @allure.title('点击选择设备创建开机自动场景测试')
    def test12(self):
        sceneRecommend(driver).click_button2()
        sceneRecommend(driver).click_button8()
        sceneRecommend(driver).click_button16()
        sceneRecommend(driver).click_button17()


@allure.epic('场景推荐页')
@allure.feature("多设备快捷控制")
class TestClass2:
    @allure.story('有设备状态')
    @allure.title('点击多设备快捷控制按钮测试')
    def test1(self):
        sceneRecommend(driver).click_button20()
        sceneRecommend(driver).click_button21()
        sceneRecommend(driver).click_button22()


@allure.epic('新增场景页')
@allure.feature("手动触发")
class TestClass3:
    @allure.story('有设备状态')
    @allure.title('点击手动触发按钮创建关机场景测试')
    def test1(self):
        sceneNewly(driver).click_button2()
        sceneNewly(driver).click_button4()
        sceneRecommend(driver).click_button11()
        sceneRecommend(driver).click_button17()

    @allure.story('有设备状态')
    @allure.title('点击手动触发按钮创建开机制冷场景测试')
    def test2(self):
        sceneNewly(driver).click_button2()
        sceneNewly(driver).click_button4()
        sceneRecommend(driver).click_button12()
        sceneRecommend(driver).click_button17()

    @allure.story('有设备状态')
    @allure.title('点击手动触发按钮创建开机制热场景测试')
    def test3(self):
        sceneNewly(driver).click_button2()
        sceneNewly(driver).click_button4()
        sceneRecommend(driver).click_button13()
        sceneRecommend(driver).click_button17()

    @allure.story('有设备状态')
    @allure.title('点击手动触发按钮创建开机除湿场景测试')
    def test4(self):
        sceneNewly(driver).click_button2()
        sceneNewly(driver).click_button4()
        sceneRecommend(driver).click_button14()
        sceneRecommend(driver).click_button17()

    @allure.story('有设备状态')
    @allure.title('点击手动触发按钮创建开机送风场景测试')
    def test5(self):
        sceneNewly(driver).click_button2()
        sceneNewly(driver).click_button4()
        sceneRecommend(driver).click_button15()
        sceneRecommend(driver).click_button17()

    @allure.story('有设备状态')
    @allure.title('点击手动触发按钮创建开机自动场景测试')
    def test6(self):
        sceneNewly(driver).click_button2()
        sceneNewly(driver).click_button4()
        sceneRecommend(driver).click_button16()
        sceneRecommend(driver).click_button17()


# @allure.epic('新增场景页')
# @allure.feature("位置触发")
# class TestClass4:
#     @allure.story('有设备状态')
#     @allure.title('点击手动触发按钮测试')
#     def test1(self):
#         sceneNewly(driver).click_button2()
#         sceneNewly(driver).click_button4()
#
#
# @allure.epic('新增场景页')
# @allure.feature("时间触发")
# class TestClass5:
#     @allure.story('无设备状态')
#     @allure.title('点击手动触发按钮测试')
#     def test1(self):
#         sceneNewly(driver).click_button2()
#         sceneNewly(driver).click_button5()


@allure.epic('新增场景页')
@allure.feature("集中控制")
class TestClass6:
    @allure.story('有设备状态')
    @allure.title('点击集中控制按钮测试')
    def test1(self):
        sceneNewly(driver).click_button2()
        sceneNewly(driver).click_button10()
        sceneRecommend(driver).click_button21()
        sceneRecommend(driver).click_button22()


if __name__ == '__main__':
    pytest.main(['--alluredir', '../report/result/', '--clean-alluredir', 'test_scene_yes.py', '-s', '-v'])
    split = 'allure generate ../report/result/ -o ../report/html --clean'
    os.system(split)
