# coding=utf-8
"""
Created on 2021-1-11
@author:Shenlei
Project:家庭列表页面
"""

from common.public import Element
from common import log
from page.desired_caps.driver_app import appPage
import time


class familyList(Element):
    text1 = ('家庭列表')
    text2 = ('新建家庭名称')
    text3 = ('请输入新建家庭名称')
    text5 = ('3个房间 | 0台设备')  # 新建家庭后的房间和设备数
    text6 = ('家庭添加成功')
    text7 = ('家庭设置')
    text8 = ('家庭切换成功')
    text9 = ('新建家庭名称不能超过20位')
    family_list_button1 = ("com.broadlink.auxair:id/sLeftIconId")  # 返回按钮
    family_list_button2 = ("com.broadlink.auxair:id/tv_input")  # 输入家庭名称按钮
    family_list_button3 = ("com.broadlink.auxair:id/btn_cancel")  # 家庭名称取消按钮
    family_list_button4 = ("com.broadlink.auxair:id/btn_ok")  # 家庭名称确认按钮
    family_list_button5 = ("com.broadlink.auxair:id/iv_delete")  # 名称清除按钮
    family_list_button6 = ("com.broadlink.auxair:id/tv_family_info")  # 房间设备按钮，点击后进入家庭设置页
    family_list_button7 = ("com.broadlink.auxair:id/iv_select")  # 家庭选择按钮，点击后进入设备列表页
    family_list_button8 = ("com.broadlink.auxair:id/tv_family_name")  # 家庭按钮，点击后进入家庭设置页
    family_list_button9 = ("com.broadlink.auxair:id/titlebar")  # 新建家庭+按钮
    family_list_button10 = ('com.broadlink.auxair:id/tv_home_manage')  # 未登录按钮,用于判断登录与否

    login_phone_button1 = ("com.broadlink.auxair:id/tv_next")  # 登录按钮
    login_phone_button2 = ("com.broadlink.auxair:id/edit1")  # 输入手机号按钮
    login_phone_button3 = ("请输入密码")  # 输入密码按钮
    login_phone_button4 = ('com.broadlink.auxair:id/iv_login_change')  # 切换至验证码登录按钮
    login_phone_button5 = ("com.broadlink.auxair:id/iv_select")

    def login_y_n(self):  # 用于判断登录与否
        global a
        a = familyList.get_text(self, self.family_list_button10)
        print(a)
        if a == '未登录':
            familyList.get_id(self, self.family_list_button10).click()
            familyList.get_id(self, self.login_phone_button4).click()  # 进入登录页面
            familyList.get_id(self, self.login_phone_button2).send_keys("13456140816")
            familyList.get_name(self, self.login_phone_button3).send_keys("Aa123456")
            familyList.get_id(self, self.login_phone_button5).click()
            familyList.get_id(self, self.login_phone_button1).click()  # 点击登录
        else:
            familyList.get_id(self, self.family_list_button10).click()  # 进入家庭列表

    def click_button1(self):
        familyList.get_id(self, self.family_list_button1).click()
        time.sleep(1)
        log.MyLog.info('返回按钮pass')

    def click_button2(self):
        global text
        text = familyList.random_text(self)
        familyList.get_id(self, self.family_list_button2).send_keys(text)
        familyList.find_name(self, text)
        time.sleep(1)
        log.MyLog.info('输入家庭名称pass')

    def click_button3(self):
        familyList.get_id(self, self.family_list_button3).click()
        familyList.find_name(self, self.text1)
        time.sleep(1)
        log.MyLog.info('取消家庭名称pass')

    def click_button4(self):
        familyList.get_id(self, self.family_list_button4).click()
        familyList.find_toast(self, self.text3)
        time.sleep(1)
        log.MyLog.info('未输入家庭名称点击确认pass')

    def click_button5(self):
        familyList.get_id(self, self.family_list_button4).click()
        familyList.find_toast(self, self.text6)
        familyList.find_name(self, text)
        time.sleep(1)
        log.MyLog.info('输入家庭名称点击确认pass')

    def click_button6(self):
        familyList.get_id(self, self.family_list_button5).click()
        familyList.find_name(self, self.text3)
        time.sleep(1)
        log.MyLog.info('清除家庭名称pass')

    def click_button7(self):
        familyList.get_id(self, self.family_list_button6).click()
        familyList.find_name(self, self.text7)
        time.sleep(1)
        log.MyLog.info('点击房间设备按钮pass')

    def click_button8(self):
        familyList.get_id(self, self.family_list_button7).click()
        familyList.find_toast(self, self.text8)
        time.sleep(1)
        log.MyLog.info('家庭切换pass')

    def click_button9(self):
        familyList.get_xpath(self, self.family_list_button9).click()
        familyList.find_name(self, self.text2)
        time.sleep(1)
        log.MyLog.info('新建家庭pass')

    def click_button10(self):
        familyList.get_id(self, self.family_list_button2).send_keys('123456789012345678901')
        familyList.find_toast(self, self.text9)
        time.sleep(1)
        log.MyLog.info('输入家庭名称超20位pass')


if __name__ == '__main__':
    driver = appPage.driver()
    familyList(driver).login_y_n()
    familyList(driver).click_button9()
    familyList(driver).click_button2()
    familyList(driver).click_button5()
