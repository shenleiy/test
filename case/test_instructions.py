# coding=utf-8
"""
Created on 2021-1-27
@author:
Project:测试用例--产品指南
"""

import pytest
import allure
import os
from page.desired_caps.driver_app import appPage
from page.page_my.instructions import instructions
from common.public import Element


@pytest.fixture(scope='class', autouse=True)
def login():
    global driver
    driver = appPage.driver()
    instructions(driver).login_y_n()

    yield  # 相当于teardown
    driver.quit()


@allure.epic('产品指南')
@allure.feature("产品指南列表")
class TestClass:
    @allure.story('列表页')
    @allure.title('列表显示')
    def test_show1(self):
        instructions(driver).show1()

    @allure.story('页面跳转')
    @allure.title('跳转到电子说明书页')
    def test_show2(self):
        instructions(driver).show2()

    @allure.story('页面跳转')
    @allure.title('跳转到产品使用指南页')
    def test_show3(self):
        instructions(driver).show3()

    @allure.story('页面跳转')
    @allure.title('跳转到拆洗教程页')
    def test_show4(self):
        instructions(driver).show4()


@allure.epic('电子说明书')
@allure.feature("电子说明书")
class TestClass1:
    @allure.story('查找电子说明书')
    @allure.title('通过带W的型号查询说明书')
    def test_search1(self):
        instructions(driver).search1()

    @allure.story('查找电子说明书')
    @allure.title('查看电子说明书')
    def test_open1(self):
        instructions(driver).open1()


@allure.epic('电子说明书')
@allure.feature("电子说明书")
class TestClass2:
    @allure.story('查找电子说明书')
    @allure.title('通过不带W的型号查询说明书')
    def test_search2(self):
        instructions(driver).search2()

    @allure.story('查找电子说明书')
    @allure.title('查看电子说明书')
    def test_open2(self):
        instructions(driver).open1()


@allure.epic('电子说明书')
@allure.feature("电子说明书")
class TestClass3:
    @allure.story('查找电子说明书')
    @allure.title('错误条码')
    def test_search3(self):
        instructions(driver).search3()


@allure.epic('电子说明书')
@allure.feature("电子说明书")
class TestClass4:
    @allure.story('查找电子说明书')
    @allure.title('扫码查询')
    def test_search5(self):
        instructions(driver).search5()


@allure.epic('电子说明书')
@allure.feature("历史查看")
class TestClass5:
    @allure.story('历史记录查看')
    @allure.title('通过历史记录查看')
    def test_search4(self):
        print(instructions(driver).deleter1_2())
        b = instructions(driver).deleter1_2()
        if b == True:
            print("已有历史记录")
        else:
            instructions(driver).deleter1_1()
            print("查询条码，生成记录")
        instructions(driver).search4()


@allure.epic('电子说明书')
@allure.feature("历史查看")
class TestClass6:
    @allure.story('删除历史记录')
    @allure.title('查询是否有历史记录，如无，则新生成一条')
    def test_deleter1(self):
        print(instructions(driver).deleter1())
        b = instructions(driver).deleter1()
        if b == True:
            print("已有历史记录")
        else:
            instructions(driver).deleter1_1()
            print("查询条码，生成记录")

    @allure.story('删除历史记录')
    @allure.title('点击删除')
    def test_deleter2(self):
        instructions(driver).deleter2()

    @allure.story('删除历史记录')
    @allure.title('取消删除')
    def test_deleter3(self):
        instructions(driver).deleter3()

    @allure.story('删除历史记录')
    @allure.title('确认删除')
    def test_deleter3(self):
        instructions(driver).deleter4()


@allure.epic('产品指南')
@allure.feature("产品使用知识")
class TestClass7:
    @allure.story('查看知识库')
    @allure.title('查看知识库')
    def test_search4(self):
        instructions(driver).show_knowledge1()
        instructions(driver).show_knowledge3()


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_instructions.py::TestClass7'])
    # pytest.main(['--alluredir', '../report/result/', '--clean-alluredir', 'test_instructions.py'])
    # split = 'allure serve ../report/result/ -o ../report/html --clean'
    # os.system(split)
