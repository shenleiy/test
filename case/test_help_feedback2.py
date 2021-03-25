# coding=utf-8
"""
Created on 2021-1-18
@author:
Project:测试用例--帮助与反馈
"""

import pytest
import allure
import os
from page.desired_caps.driver_app import appPage
#from page.page_my.login_phone import loginPhone
from page.page_my.help_feedback import helpAndfeedback


@pytest.fixture(scope='class', autouse=True)
def login():
    global driver
    driver = appPage.driver()
    helpAndfeedback(driver).click_help()
    yield
    driver.quit()


@allure.epic('帮助与反馈')
@allure.feature("帮助反馈列表")
class TestClass1:
    @allure.story('列表项核对')
    @allure.title('帮助项展示')
    def test_show(self):
        helpAndfeedback(driver).click_help_show()

    @allure.story('列表项核对')
    @allure.title('账号问题展示')
    def test_show1(self):
        helpAndfeedback(driver).click_help_show1()

    @allure.story('列表项核对')
    @allure.title('设备添加展示')
    def test_show2(self):
        helpAndfeedback(driver).click_help_show2()

    @allure.story('列表项核对')
    @allure.title('设备管理展示')
    def test_show3(self):
        helpAndfeedback(driver).click_help_show3()

    @allure.story('列表项核对')
    @allure.title('功能异常展示')
    def test_show4(self):
        helpAndfeedback(driver).click_help_show4()

    @allure.story('列表项核对')
    @allure.title('场景模式展示')
    def test_show5(self):
        helpAndfeedback(driver).click_help_show5()

    @allure.story('列表项核对')
    @allure.title('其他问题展示')
    def test_show6(self):
        helpAndfeedback(driver).click_help_show6()


@allure.epic('帮助与反馈')
@allure.feature("帮助具体详情")
class TestClass2:
    @allure.story("%s" % helpAndfeedback.help1 +"详情")
    @allure.title("%s" % helpAndfeedback.help1_text1_1 +"详情")
    def test_help1_1(self):
        helpAndfeedback(driver).click_help_open1()
        helpAndfeedback(driver).click_help1_1()
        print("%s" % helpAndfeedback.help1_text1_1 +"详情")

    @allure.story("%s" % helpAndfeedback.help1 + "详情")
    @allure.title("%s" % helpAndfeedback.help1_text2_1 + "详情")
    def test_help1_2(self):
        helpAndfeedback(driver).click_help1_2()

    @allure.story("%s" % helpAndfeedback.help1 + "详情")
    @allure.title("%s" % helpAndfeedback.help1_text3_1 + "详情")
    def test_help1_3(self):
        helpAndfeedback(driver).click_help1_3()

    @allure.story("%s" % helpAndfeedback.help1 + "详情")
    @allure.title("%s" % helpAndfeedback.help1_text4_1 + "详情")
    def test_help1_4(self):
        helpAndfeedback(driver).click_help1_4()

    @allure.story("%s" % helpAndfeedback.help1 + "详情")
    @allure.title("%s" % helpAndfeedback.help1_text5_1 + "详情")
    def test_help1_5(self):
        helpAndfeedback(driver).click_help1_5()

    @allure.story("%s" % helpAndfeedback.help1 + "详情")
    @allure.title("%s" % helpAndfeedback.help1_text6_1 + "详情")
    def test_help1_6(self):
        helpAndfeedback(driver).click_help1_6()


@allure.epic('帮助与反馈')
@allure.feature("帮助具体详情")
class TestClass3:
    @allure.story("%s" % helpAndfeedback.help2 + "详情")
    @allure.title("%s" % helpAndfeedback.help2_text1_1 + "详情")
    def test_help2_1(self):
        helpAndfeedback(driver).click_help_open2()
        helpAndfeedback(driver).click_help2_1()
        print("%s" % helpAndfeedback.help2_text1_1 + "详情")

    @allure.story("%s" % helpAndfeedback.help2 + "详情")
    @allure.title("%s" % helpAndfeedback.help2_text2_1 + "详情")
    def test_help2_2(self):
        helpAndfeedback(driver).click_help2_2()

    @allure.story("%s" % helpAndfeedback.help2 + "详情")
    @allure.title("%s" % helpAndfeedback.help2_text3_1 + "详情")
    def test_help2_3(self):
        helpAndfeedback(driver).click_help2_3()


@allure.epic('帮助与反馈')
@allure.feature("帮助具体详情")
class TestClass4:
    @allure.story("%s" % helpAndfeedback.help3 + "详情")
    @allure.title("%s" % helpAndfeedback.help3_text1_1 + "详情")
    def test_help3_1(self):
        helpAndfeedback(driver).click_help_open3()
        helpAndfeedback(driver).click_help3_1()
        print("%s" % helpAndfeedback.help3_text1_1 + "详情")

    @allure.story("%s" % helpAndfeedback.help3 + "详情")
    @allure.title("%s" % helpAndfeedback.help3_text2_1 + "详情")
    def test_help3_2(self):
        helpAndfeedback(driver).click_help3_2()

    @allure.story("%s" % helpAndfeedback.help3 + "详情")
    @allure.title("%s" % helpAndfeedback.help3_text3_1 + "详情")
    def test_help3_3(self):
        helpAndfeedback(driver).click_help3_3()

    @allure.story("%s" % helpAndfeedback.help3 + "详情")
    @allure.title("%s" % helpAndfeedback.help3_text4_1 + "详情")
    def test_help3_4(self):
        helpAndfeedback(driver).click_help3_4()


@allure.epic('帮助与反馈')
@allure.feature("帮助具体详情")
class TestClass5:
    @allure.story("%s" % helpAndfeedback.help4 + "详情")
    @allure.title("%s" % helpAndfeedback.help4_text1_1 + "详情")
    def test_help4_1(self):
        helpAndfeedback(driver).click_help_open4()
        helpAndfeedback(driver).click_help4_1()
        print("%s" % helpAndfeedback.help4_text1_1 + "详情")

    @allure.story("%s" % helpAndfeedback.help4 + "详情")
    @allure.title("%s" % helpAndfeedback.help4_text2_1 + "详情")
    def test_help4_2(self):
        helpAndfeedback(driver).click_help4_2()

    @allure.story("%s" % helpAndfeedback.help4 + "详情")
    @allure.title("%s" % helpAndfeedback.help4_text3_1 + "详情")
    def test_help4_3(self):
        helpAndfeedback(driver).click_help4_3()

    @allure.story("%s" % helpAndfeedback.help4 + "详情")
    @allure.title("%s" % helpAndfeedback.help4_text4_1 + "详情")
    def test_help4_4(self):
        helpAndfeedback(driver).click_help4_4()

    @allure.story("%s" % helpAndfeedback.help4 + "详情")
    @allure.title("%s" % helpAndfeedback.help4_text5_1 + "详情")
    def test_help4_5(self):
        helpAndfeedback(driver).click_help4_5()


@allure.epic('帮助与反馈')
@allure.feature("帮助具体详情")
class TestClass6:
    @allure.story("%s" % helpAndfeedback.help5 + "详情")
    @allure.title("%s" % helpAndfeedback.help5_text1_1 + "详情")
    def test_help5_1(self):
        helpAndfeedback(driver).click_help_open5()
        helpAndfeedback(driver).click_help5_1()
        print("%s" % helpAndfeedback.help5_text1_1 + "详情")

    @allure.story("%s" % helpAndfeedback.help5 + "详情")
    @allure.title("%s" % helpAndfeedback.help5_text2_1 + "详情")
    def test_help5_2(self):
        helpAndfeedback(driver).click_help5_2()


@allure.epic('帮助与反馈')
@allure.feature("帮助具体详情")
class TestClass7:
    @allure.story("%s" % helpAndfeedback.help6 + "详情")
    @allure.title("%s" % helpAndfeedback.help6_text1_1 + "详情")
    def test_help6_1(self):
        helpAndfeedback(driver).click_help_open6()
        helpAndfeedback(driver).click_help6_1()
        print("%s" % helpAndfeedback.help6_text1_1 + "详情")

    @allure.story("%s" % helpAndfeedback.help6 + "详情")
    @allure.title("%s" % helpAndfeedback.help6_text2_1 + "详情")
    def test_help6_2(self):
        helpAndfeedback(driver).click_help6_2()


@allure.epic('帮助与反馈')
@allure.feature("意见反馈")
class TestClass8:
    @allure.story("进入意见反馈页面")
    @allure.title('通过意见反馈进入反馈页面测试')
    def test_feedback1(self):
        helpAndfeedback(driver).click_feedback1()


@allure.epic('帮助与反馈')
@allure.feature("意见反馈")
class TestClass9:
    @allure.story("进入意见反馈页面")
    @allure.title('通过还没解决问题进入意见反馈测试')
    def test_feedback2(self):
        helpAndfeedback(driver).click_feedback2()


@allure.epic('帮助与反馈')
@allure.feature("反馈页面选项")
class TestClass10:
    @allure.story('显示')
    @allure.title('页面显示')
    def test_feedback1_1(self):
        with allure.step("step1：进入意见反馈页面"):
            helpAndfeedback(driver).click_feedback1()
        with allure.step("step2：查看页面显示"):
            helpAndfeedback(driver).click_feedback1_1()


@allure.epic('帮助与反馈')
@allure.feature("反馈页面选项")
class TestClass11:
    @allure.story('问题类型')
    @allure.title('历遍所有问题类型')
    def test_feedback3(self):
        helpAndfeedback(driver).click_feedback3()


@allure.epic('帮助与反馈')
@allure.feature("反馈页面选项")
class TestClass12:
    @allure.story('提交按钮状态')
    @allure.title('不可点状态：内容未输入')
    def test_feedback4(self):
        helpAndfeedback(driver).click_feedback1()
        helpAndfeedback(driver).click_feedback4()

    @allure.story('提交按钮状态')
    @allure.title('可点状态：内容已填写')
    def test_feedback4_1(self):
        helpAndfeedback(driver).click_feedback4_1()


@allure.epic('帮助与反馈')
@allure.feature("反馈页面选项")
class TestClass13:
    @allure.story('反馈内容')
    @allure.title('字数统计')
    def test_feedback5(self):
        helpAndfeedback(driver).click_feedback1()
        helpAndfeedback(driver).click_feedback5()

    @allure.story('反馈内容')
    @allure.title('字数限制')
    def test_feedback6(self):
        helpAndfeedback(driver).click_feedback6()


@allure.epic('帮助与反馈')
@allure.feature("反馈页面选项")
class TestClass14:
    @allure.story('手机号')
    @allure.title('输入限制')
    def test_feedback7(self):
        helpAndfeedback(driver).click_feedback1()
        helpAndfeedback(driver).click_feedback7()

    @allure.story('手机号')
    @allure.title('清除手机号')
    def test_feedback8(self):
        helpAndfeedback(driver).click_feedback8()


@allure.epic('帮助与反馈')
@allure.feature("提交意见反馈")
class TestClass15:
    @allure.story('提交意见反馈')
    @allure.title('手机号未填')
    def test_feedback9(self):
        with allure.step("step1：进入意见反馈页面"):
            helpAndfeedback(driver).click_feedback1()
        with allure.step("step2：手机号删除"):
            helpAndfeedback(driver).click_feedback8()
        with allure.step("step3：输入内容"):
            helpAndfeedback(driver).click_feedback5()
        with allure.step("step4：提交意见反馈"):
            helpAndfeedback(driver).click_feedback10_1()


@allure.epic('帮助与反馈')
@allure.feature("提交意见反馈")
class TestClass16:
    @allure.story('提交意见反馈')
    @allure.title('内容过长未填')
    def test_feedback10(self):
        with allure.step("step1：进入意见反馈页面"):
            helpAndfeedback(driver).click_feedback1()
        with allure.step("step2：输入过长内容"):
            helpAndfeedback(driver).click_feedback6()
        with allure.step("step3：提交意见反馈"):
            helpAndfeedback(driver).click_feedback10_1()


@allure.epic('帮助与反馈')
@allure.feature("提交意见反馈")
class TestClass17:
    @allure.story('反馈记录')
    @allure.title('查看记录(由于有bug该部分内容还未写)')
    def test_feedback11(self):
        return True
        #helpAndfeedback(driver).click_feedback11()


@allure.epic('帮助与反馈')
@allure.feature("提交意见反馈")
class TestClass18:
    @allure.story('反馈记录')
    @allure.title('再次反馈')
    def test_feedback12(self):
        helpAndfeedback(driver).click_feedback12()


if __name__ == '__main__':
    pytest.main(['-sv', 'test_help_feedback2.py::TestClass4'])
    #pytest.main(['--alluredir', '../report/result/', '--clean-alluredir', 'test_help_feedback2.py'])
    #split = 'allure serve ../report/result/ -o ../report/html --clean'
    #os.system(split)
