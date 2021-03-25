# coding=utf-8
"""
Created on 2021-1-14
@author:Shenlei
Project:个人资料页面
"""

from common.public import Element
from common import log
from page.desired_caps.driver_app import appPage
import time


class myPerson(Element):
    text1 = ("个人资料")
    text2 = ('头像')
    text3 = ('登录手机号')
    text4 = ('昵称')
    text5 = ('姓名')
    text6 = ('性别')
    text7 = ('出生日期')
    text8 = ('所在地区')
    text9 = ('请输入昵称')  # 空昵称断言
    text10 = ('请输入姓名')  # 空姓名断言
    text11 = ('修改成功')  # 修改成功断言
    text12 = ('选择照片')
    text13 = ('编辑个人资料')
    text14 = ('台湾省')
    text15 = ('香港特别行政区')
    text16 = ('昵称不能超过20位')
    text17 = ('姓名不能超过20位')
    my_person_button0 = ('com.broadlink.auxair:id/tv_home_manage')  # 未登录按钮,用于判断登录与否
    my_person_button1 = ("我的")  # 我的按钮
    my_person_button2 = ("com.broadlink.auxair:id/edit")  # 编辑个人资料按钮
    my_person_button3 = ("com.broadlink.auxair:id/iv_user_head")  # 头像按钮
    my_person_button4 = ("com.broadlink.auxair:id/tv_nike_name")  # 昵称按钮
    my_person_button5 = ("com.broadlink.auxair:id/tv_name")  # 姓名按钮
    my_person_button6 = ("com.broadlink.auxair:id/tv_sex")  # 性别按钮
    my_person_button7 = ("com.broadlink.auxair:id/tv_birth_day")  # 出生日期按钮
    my_person_button8 = ("com.broadlink.auxair:id/tv_address")  # 所在地区按钮

    my_person_button9 = ("com.broadlink.auxair:id/tv_input")  # 输入按钮
    my_person_button10 = ("com.broadlink.auxair:id/iv_delete")  # 清除按钮
    my_person_button11 = ("com.broadlink.auxair:id/btn_ok")  # 确定按钮
    my_person_button12 = ("com.broadlink.auxair:id/btn_cancel")  # 取消按钮
    my_person_button13 = ("com.broadlink.auxair:id/rl_man")  # 性别男按钮
    my_person_button14 = ("com.broadlink.auxair:id/rl_women")  # 性别女按钮
    my_person_button15 = ("com.broadlink.auxair:id/dialog_select_cancel_tv")  # 出生日期取消按钮
    my_person_button16 = ("com.broadlink.auxair:id/dialog_select_sure_tv")  # 出生日期确认按钮
    my_person_button17 = ("com.broadlink.auxair:id/tv_cancle")  # 头像取消按钮

    login_phone_button1 = ("com.broadlink.auxair:id/tv_next")  # 登录按钮
    login_phone_button2 = ("com.broadlink.auxair:id/edit1")  # 输入手机号按钮
    login_phone_button3 = ("请输入密码")  # 输入密码按钮
    login_phone_button4 = ('com.broadlink.auxair:id/iv_login_change')  # 切换至验证码登录按钮
    login_phone_button5 = ("com.broadlink.auxair:id/iv_select")

    family_list_button1 = ("com.broadlink.auxair:id/sLeftIconId")  # 返回按钮

    def login_y_n(self):  # 用于判断登录与否
        global a
        a = myPerson.get_text(self, self.my_person_button0)
        print(a)
        if a == '未登录':
            myPerson.get_id(self, self.my_person_button0).click()
            myPerson.get_id(self, self.login_phone_button4).click()  # 进入登录页面
            myPerson.get_id(self, self.login_phone_button2).send_keys("13456140816")
            myPerson.get_name(self, self.login_phone_button3).send_keys("Aa123456")
            myPerson.get_id(self, self.login_phone_button5).click()
            myPerson.get_id(self, self.login_phone_button1).click()  # 点击登录
            myPerson.get_id(self, self.family_list_button1).click()
            myPerson.get_name(self, self.my_person_button1).click()  # 进入我的页面
        else:
            myPerson.get_name(self, self.my_person_button1).click()  # 进入我的页面

    def click_button0(self):
        myPerson.get_id(self, self.my_person_button2).click()  # 进入个人资料页面
        myPerson.find_name(self, self.text1)
        time.sleep(1)
        log.MyLog.info('个人资料页文本显示pass')

    def click_button1(self):
        myPerson.get_id(self, self.my_person_button3).click()
        myPerson.find_name(self, self.text12)
        myPerson.get_id(self, self.my_person_button17).click()
        time.sleep(1)
        log.MyLog.info('头像按钮pass')

    def click_button2(self):
        myPerson.get_id(self, self.family_list_button1).click()
        myPerson.find_name(self, self.text13)
        time.sleep(1)
        log.MyLog.info('返回按钮pass')

    def click_button3(self):
        myPerson.get_id(self, self.my_person_button4).click()
        log.MyLog.info('昵称输入按钮pass')

    def click_button03(self):
        text = myPerson.random_text(self)
        myPerson.get_id(self, self.my_person_button9).send_keys(text)
        myPerson.find_name(self, text)
        myPerson.get_id(self, self.my_person_button11).click()
        myPerson.find_toast(self, self.text11)
        time.sleep(1)
        assert myPerson.get_xpath_text(self, self.my_person_button4) == text
        log.MyLog.info('修改昵称1-20位pass')

    def click_button003(self):
        myPerson.get_id(self, self.my_person_button9).send_keys('123456789012345678901')
        myPerson.find_toast(self, self.text16)
        time.sleep(1)
        log.MyLog.info('修改昵称超20位pass')

    def click_button04(self):
        myPerson.get_id(self, self.my_person_button12).click()
        myPerson.find_name(self, self.text1)
        time.sleep(1)
        log.MyLog.info('取消按钮pass')

    def click_button4(self):
        text = myPerson.random_text(self)
        myPerson.get_id(self, self.my_person_button9).send_keys(text)
        myPerson.find_name(self, text)
        myPerson.get_id(self, self.my_person_button12).click()
        myPerson.find_name(self, self.text1)
        time.sleep(1)
        log.MyLog.info('取消按钮pass')

    def click_button5(self):
        myPerson.get_id(self, self.my_person_button11).click()
        myPerson.find_toast(self, self.text9)
        time.sleep(1)
        log.MyLog.info('清除昵称点击确认pass')

    # def click_button6(self):
    #     myPerson.get_id(self, self.my_person_button11).click()
    #     myPerson.find_toast(self, self.text11)
    #     time.sleep(1)
    #     log.MyLog.info('修改后点击确认pass')

    def click_button7(self):
        myPerson.get_id(self, self.my_person_button11).click()
        time.sleep(1)
        log.MyLog.info('未修改点击确认pass')

    def click_button8(self):
        myPerson.get_id(self, self.my_person_button10).click()
        myPerson.find_name(self, self.text9)
        time.sleep(1)
        log.MyLog.info('清除昵称按钮pass')

    def click_button9(self):
        myPerson.get_id(self, self.my_person_button5).click()
        log.MyLog.info('姓名输入按钮pass')

    def click_button09(self):
        text = myPerson.random_text(self)
        myPerson.get_id(self, self.my_person_button9).send_keys(text)
        myPerson.find_name(self, text)
        myPerson.get_id(self, self.my_person_button11).click()
        myPerson.find_toast(self, self.text11)
        time.sleep(1)
        assert myPerson.get_xpath_text(self, self.my_person_button5) == text
        log.MyLog.info('修改姓名1-20位pass')

    def click_button009(self):
        myPerson.get_id(self, self.my_person_button9).send_keys('123456789012345678901')
        myPerson.find_toast(self, self.text17)
        time.sleep(1)
        log.MyLog.info('修改昵称超20位pass')

    def click_button10(self):
        myPerson.get_id(self, self.my_person_button11).click()
        myPerson.find_toast(self, self.text10)
        time.sleep(1)
        log.MyLog.info('清除姓名点击确认pass')

    def click_button11(self):
        myPerson.get_id(self, self.my_person_button10).click()
        myPerson.find_name(self, self.text10)
        time.sleep(1)
        log.MyLog.info('清除姓名按钮pass')

    def click_button12(self):
        myPerson.get_id(self, self.my_person_button6).click()
        myPerson.get_id(self, self.my_person_button13).click()
        myPerson.find_toast(self, self.text11)
        time.sleep(1)
        assert myPerson.get_xpath_text(self, self.my_person_button6) == '男'
        log.MyLog.info('点击性别男按钮pass')

    def click_button13(self):
        myPerson.get_id(self, self.my_person_button6).click()
        myPerson.get_id(self, self.my_person_button14).click()
        myPerson.find_toast(self, self.text11)
        time.sleep(1)
        assert myPerson.get_xpath_text(self, self.my_person_button6) == '女'
        log.MyLog.info('点击性别女按钮pass')

    def click_button14(self):
        myPerson.get_id(self, self.my_person_button7).click()
        myPerson.get_id(self, self.my_person_button16).click()
        myPerson.find_toast(self, self.text11)
        time.sleep(1)
        log.MyLog.info('出生日期点击确定pass')

    def click_button15(self):
        myPerson.get_id(self, self.my_person_button7).click()
        myPerson.get_id(self, self.my_person_button15).click()
        myPerson.find_name(self, self.text1)
        time.sleep(1)
        log.MyLog.info('出生日期点击取消pass')

    def click_button16(self):
        i = 0
        while i < 2:
            a = myPerson.get_xpath_text(self, self.my_person_button8)
            print(a)
            if myPerson.get_xpath_text(self, self.my_person_button8) == '台湾省 ':
                myPerson.get_id(self, self.my_person_button8).click()
                myPerson.swipe_up(self, self.text15)
                myPerson.find_toast(self, self.text11)
                time.sleep(1)
                assert myPerson.get_xpath_text(self, self.my_person_button8) == '香港特别行政区 '
                log.MyLog.info('上滑动选择所在地区pass')
            else:
                myPerson.get_id(self, self.my_person_button8).click()
                myPerson.swipe_down(self, self.text14)
                myPerson.find_toast(self, self.text11)
                time.sleep(1)
                assert myPerson.get_xpath_text(self, self.my_person_button8) == '台湾省 '
                log.MyLog.info('下滑动选择所在地区pass')
            i += 1


if __name__ == '__main__':
    driver = appPage.driver()
    myPerson(driver).login_y_n()
    myPerson(driver).click_button0()
    myPerson(driver).click_button3()
    myPerson(driver).click_button04()
