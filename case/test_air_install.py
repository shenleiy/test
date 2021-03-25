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
# from page.page_my.login_phone import loginPhone
from page.page_afterService.Air_install import Appointment


@pytest.fixture(scope='class', autouse=True)
def login():
    global driver
    driver = appPage.driver()
    Appointment(driver).login_y_n()

    yield
    driver.quit()


@allure.epic('售后服务')
@allure.feature("售后服务列表")
class TestClass:
    @allure.story('列表页')
    @allure.title('进入页面')
    def test_show(self):
        Appointment(driver).service_list()

    @allure.story('列表页')
    @allure.title('进入报装页面')
    def test_show1(self):
        Appointment(driver).install_show1()

    @allure.story('列表页')
    @allure.title('进入报修页面')
    def test_show2(self):
        Appointment(driver).install_show2()

    @allure.story('列表页')
    @allure.title('进入工单查询页面')
    def test_show3(self):
        Appointment(driver).install_show3()

    @allure.story('列表页')
    @allure.title('进入服务声明页面')
    def test_show4(self):
        Appointment(driver).install_show4()


@allure.epic('预约安装')
@allure.feature("页面显示")
class TestClass1:
    @allure.story('展示')
    @allure.title('整体展示')
    def test_show1(self):
        Appointment(driver).install_show()
        Appointment(driver).install_show1_1()


@allure.epic('预约安装')
@allure.feature("预约详情")
class TestClass2:
    @allure.story('产品线')
    @allure.title('产品线选项展示')
    def test_click1(self):
        Appointment(driver).install_show()
        Appointment(driver).install_click1()

    @allure.story('产品线')
    @allure.title('产品线选择')
    def test_click1_1(self):
        Appointment(driver).install_click1_1()

    # @allure.story('购买单位类型')
    # @allure.title('购买单位类型选择')
    # def test_click2(self):
    #     Appointment(driver).install_click2()

    @allure.story('购买日期')
    @allure.title('购买日期选择')
    def test_click3(self):
        Appointment(driver).install_click3()

    @allure.story('物流状态')
    @allure.title('物流状态选项展示')
    def test_click4(self):
        Appointment(driver).install_click4()

    @allure.story('物流状态')
    @allure.title('物流状态选择')
    def test_click4_1(self):
        Appointment(driver).install_click4_1()

    @allure.story('预约日期')
    @allure.title('预约日期选择')
    def test_click5(self):
        Appointment(driver).install_click5()

    # @allure.story('备注')
    # @allure.title('填写备注')
    # def test_click6(self):
    #     Appointment(driver).install_click6()


@allure.epic('预约安装')
@allure.feature("提交判断")
class TestClass3:
    @allure.story('数据不全')
    @allure.title('产品线未填')
    def test_toast1(self):
        Appointment(driver).install_toast1()


@allure.epic('预约安装')
@allure.feature("提交判断")
class TestClass4:
    @allure.story('数据不全')
    @allure.title('单位类型未选择')
    def test_toast2(self):
        Appointment(driver).install_toast2()


@allure.epic('预约安装')
@allure.feature("提交判断")
class TestClass5:
    @allure.story('数据不全')
    @allure.title('购买日期未选择')
    def test_toast3(self):
        Appointment(driver).install_toast3()


@allure.epic('预约安装')
@allure.feature("提交判断")
@pytest.mark.skip(reason="由于提交会引起售后电话，故没有点击提交操作")
class TestClass6:
    @allure.story('正确提交')
    @allure.title('正确提交')
    def test_toast4(self):
        Appointment(driver).install_toast4()


@allure.epic('预约维修')
@allure.feature("页面显示")
class TestClass7:
    @allure.story('展示')
    @allure.title('整体展示')
    def test_show2(self):
        Appointment(driver).install_show2_1()


@allure.epic('预约维修')
@allure.feature("预约详情")
class TestClass8:
    @allure.story('产品线')
    @allure.title('产品线选项展示')
    def test_click01(self):
        Appointment(driver).install_show2_1()
        Appointment(driver).install_click1()

    @allure.story('产品线')
    @allure.title('产品线选择')
    def test_click01_1(self):
        Appointment(driver).install_click1_1()

    # @allure.story('购买单位类型')
    # @allure.title('购买单位类型选择')
    # def test_click02(self):
    #     Appointment(driver).install_click2()

    @allure.story('购买日期')
    @allure.title('购买日期选择')
    def test_click03(self):
        Appointment(driver).install_click3()

    @allure.story('预约日期')
    @allure.title('预约日期选择')
    def test_click05(self):
        Appointment(driver).install_click5()

    # @allure.story('备注')
    # @allure.title('填写备注')
    # def test_click06(self):
    #     Appointment(driver).install_click6()
    #     driver.quit()


@allure.epic('预约安装')
@allure.feature("添加联系人")
class TestClass9:
    @allure.story('添加联系人')
    @allure.title('进入页面')
    def test_contacts1(self):
        Appointment(driver).install_show()
        Appointment(driver).contacts1()

    @allure.story('添加联系人')
    @allure.title('页面展示')
    def test_contacts2(self):
        Appointment(driver).contacts2()


@allure.epic('预约安装')
@allure.feature("添加联系人")
class TestClass10:
    @allure.story('提交')
    @allure.title('提交按钮判断')
    def test_contacts3(self):
        Appointment(driver).install_show()
        Appointment(driver).contacts1()
        Appointment(driver).contacts3()
        Appointment(driver).contacts7_2()
        Appointment(driver).contacts4()
        Appointment(driver).contacts7_2()
        Appointment(driver).contacts5()
        Appointment(driver).contacts7_2()
        # Appointment(driver).contacts6()
        # Appointment(driver).contacts7()


@allure.epic('预约安装')
@allure.feature("添加联系人")
class TestClass11:
    @allure.story('提交')
    @allure.title('正确填写保存')
    def test_contacts4(self):
        Appointment(driver).install_show()
        Appointment(driver).contacts1()
        Appointment(driver).contacts3()
        Appointment(driver).contacts4()
        Appointment(driver).contacts5()
        Appointment(driver).contacts6()
        Appointment(driver).contacts7()


@allure.epic('预约安装')
@allure.feature("添加联系人")
class TestClass12:
    @allure.story('提交')
    @allure.title('手机号非纯数字')
    def test_contacts5(self):
        Appointment(driver).install_show()
        Appointment(driver).contacts1()
        Appointment(driver).contacts3()
        Appointment(driver).contacts4_1()
        Appointment(driver).contacts5()
        Appointment(driver).contacts6()
        Appointment(driver).contacts7_1()


@allure.epic('预约安装')
@allure.feature("添加联系人")
class TestClass13:
    @allure.story('提交')
    @allure.title('手机号未满11位')
    def test_contacts6(self):
        Appointment(driver).install_show()
        Appointment(driver).contacts1()
        Appointment(driver).contacts3()
        Appointment(driver).contacts4_2()
        Appointment(driver).contacts5()
        Appointment(driver).contacts6()
        Appointment(driver).contacts7_1()


@allure.epic('预约安装')
@allure.feature("添加联系人")
class TestClass14:
    @allure.story('提交')
    @allure.title('联系人字数过长')
    def test_contacts7(self):
        Appointment(driver).install_show()
        Appointment(driver).contacts1()
        Appointment(driver).contacts3_1()
        Appointment(driver).contacts4()
        Appointment(driver).contacts5()
        Appointment(driver).contacts6()
        Appointment(driver).contacts7()


@allure.epic('预约安装')
@allure.feature("添加联系人")
class TestClass15:
    @allure.story('提交')
    @allure.title('设为默认地址')
    def test_contacts8(self):
        Appointment(driver).install_show()
        Appointment(driver).contacts1()
        Appointment(driver).contacts3()
        Appointment(driver).contacts4()
        Appointment(driver).contacts5()
        Appointment(driver).contacts6()
        Appointment(driver).contacts7()


@allure.epic('预约安装')
@allure.feature("添加联系人")
class TestClass16:
    @allure.story('编辑')
    @allure.title('修改姓名手机号')
    def test_contacts9(self):
        Appointment(driver).install_show()
        Appointment(driver).contacts10()
        Appointment(driver).contacts11()


@allure.epic('预约安装')
@allure.feature("添加联系人")
class TestClass17:
    @allure.story('删除')
    @allure.title('删除联系人-取消')
    def test_contacts10(self):
        Appointment(driver).install_show()
        Appointment(driver).contacts8()

    @allure.story('删除')
    @allure.title('删除联系人-确认')
    def test_contacts11(self):
        Appointment(driver).contacts9()


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_air_install.py'])
    # pytest.main(['--alluredir', '../report/result/', '--clean-alluredir', 'test_air_install.py'])
    # split = 'allure serve ../report/result/ -o ../report/html --clean'
    # os.system(split)
