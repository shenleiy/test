# coding=utf-8
"""
Created on 2021-1-25
@author:Shenlei
Project:测试用例--场景无设备（文本及按钮测试）
"""

import pytest
import allure
import os
from page.desired_caps.driver_app import appPage
from page.page_scene.scene_recommend import sceneRecommend
from page.page_scene.scene_newly import sceneNewly


@pytest.fixture(scope='function', autouse=True)  # 相当于setup
def test():
    global driver
    driver = appPage.driver()
    sceneRecommend(driver).login_y_n()

    yield  # 相当于teardown
    driver.quit()


@allure.epic('场景推荐页')
@allure.feature("回家(手动)")
class TestClass:
    @allure.story('无设备状态')
    @allure.title('点击继续添加设备按钮测试')
    def test1(self):
        sceneRecommend(driver).click_button1()
        sceneRecommend(driver).click_button5()

    @allure.story('无设备状态')
    @allure.title('点击选择设备按钮测试')
    def test2(self):
        sceneRecommend(driver).click_button1()
        sceneRecommend(driver).click_button7()

    @allure.story('未添加设备')
    @allure.title('点击确定按钮测试')
    def test3(self):
        sceneRecommend(driver).click_button1()
        sceneRecommend(driver).click_button4()

    @allure.story('未添加设备')
    @allure.title('点击返回按钮测试')
    def test4(self):
        sceneRecommend(driver).click_button1()
        sceneRecommend(driver).click_button10()


@allure.epic('场景推荐页')
@allure.feature("离家(手动)")
class TestClass1:
    @allure.story('无设备状态')
    @allure.title('点击继续添加设备按钮测试')
    def test1(self):
        sceneRecommend(driver).click_button2()
        sceneRecommend(driver).click_button5()

    @allure.story('无设备状态')
    @allure.title('点击选择设备按钮测试')
    def test2(self):
        sceneRecommend(driver).click_button2()
        sceneRecommend(driver).click_button7()

    @allure.story('未添加设备')
    @allure.title('点击确定按钮测试')
    def test3(self):
        sceneRecommend(driver).click_button2()
        sceneRecommend(driver).click_button4()

    @allure.story('未添加设备')
    @allure.title('点击返回按钮测试')
    def test4(self):
        sceneRecommend(driver).click_button2()
        sceneRecommend(driver).click_button10()


@allure.epic('场景推荐页')
@allure.feature("多设备快捷控制")
class TestClass2:
    @allure.story('无设备状态')
    @allure.title('点击多设备快捷控制按钮测试')
    def test1(self):
        sceneRecommend(driver).click_button3()


@allure.epic('新增场景页')
@allure.feature("手动触发")
class TestClass3:
    @allure.story('无设备状态')
    @allure.title('点击手动触发按钮测试')
    def test1(self):
        sceneNewly(driver).click_button2()
        sceneNewly(driver).click_button3()


@allure.epic('新增场景页')
@allure.feature("位置触发")
class TestClass4:
    @allure.story('无设备状态')
    @allure.title('点击手动触发按钮测试')
    def test1(self):
        sceneNewly(driver).click_button2()
        sceneNewly(driver).click_button5()


@allure.epic('新增场景页')
@allure.feature("时间触发")
class TestClass5:
    @allure.story('无设备状态')
    @allure.title('点击手动触发按钮测试')
    def test1(self):
        sceneNewly(driver).click_button2()
        sceneNewly(driver).click_button7()


@allure.epic('新增场景页')
@allure.feature("集中控制")
class TestClass6:
    @allure.story('无设备状态')
    @allure.title('点击手动触发按钮测试')
    def test1(self):
        sceneNewly(driver).click_button2()
        sceneNewly(driver).click_button6()


@allure.epic('场景我的页')
@allure.feature("默认场景")
class TestClass6:
    @allure.story('无设备状态')
    @allure.title('删除离家回家场景测试')
    def test1(self):
        sceneRecommend(driver).click_button9()


if __name__ == '__main__':
    pytest.main(['test_scene_no.py::TestClass4', '-v', '-s'])
# if __name__ == '__main__':
#     pytest.main(['--alluredir', '../report/result/', '--clean-alluredir', 'test_scene_no.py', '-v', '-s'])
#     split = 'allure generate ../report/result/ -o ../report/html --clean'
#     os.system(split)
