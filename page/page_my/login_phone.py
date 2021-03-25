# coding=utf-8
"""
Created on 2021-1-9
@author:Shenlei
Project:手机号登陆页面
"""

from common.public import Element
from common import log
from page.desired_caps.driver_app import appPage
import time


class loginPhone(Element):
    text1 = ("密码登录")
    text2 = ('奥云家')
    text3 = ("获取验证码")
    text4 = ('新注册手机验证后自动登录')
    text6 = ("服务条款")
    text7 = ("奥克斯集团隐私政策")
    text8 = ("未登录")
    text9 = ("请输入手机号")
    text10 = ("账号密码错误")
    text11 = ("忘记密码")
    text12 = ("登录成功")
    text13 = ("请先阅读并同意《用户协议》和《隐私政策》")

    login_phone_button1 = ("com.broadlink.auxair:id/tv_next")  # 登录按钮
    login_phone_button2 = ("com.broadlink.auxair:id/edit1")  # 输入手机号按钮
    login_phone_button3 = ("请输入密码")  # 输入密码按钮
    login_phone_button4 = ("com.broadlink.auxair:id/btn_eye")  # 显密按钮
    login_phone_button5 = ("com.broadlink.auxair:id/tv_forget_pwd")  # 忘记密码按钮
    login_phone_button6 = ('com.broadlink.auxair:id/iv_login_change')  # 切换至验证码登录按钮
    login_phone_button7 = ("com.broadlink.auxair:id/tv_user_agreement")  # 用户协议按钮
    login_phone_button8 = ("com.broadlink.auxair:id/tv_privacy_policy")  # 隐私政策按钮
    login_phone_button9 = ("com.broadlink.auxair:id/iv_back")  # 返回键按钮
    login_phone_button10 = ("com.broadlink.auxair:id/btn_clear")  # 清除X按钮
    login_phone_button11 = ('com.broadlink.auxair:id/tv_home_manage')  # 未登录按钮,用于判断登录与否
    login_phone_button12 = ("com.broadlink.auxair:id/iv_select")

    login_out1 = ("我的")  # 我的按钮
    login_out2 = ("设置")  # 设置按钮
    login_out3 = ("com.broadlink.auxair:id/tv_out")  # 退出登录按钮
    login_out4 = ("确定")  # 确定退出按钮

    def login_y_n(self):  # 用于判断登录与否
        global a
        a = loginPhone.get_text(self, self.login_phone_button11)
        print(a)
        if a == '未登录':
            loginPhone.get_id(self, self.login_phone_button11).click()
            loginPhone.get_id(self, self.login_phone_button6).click()  # 进入登录页面
        else:
            loginPhone.get_name(self, self.login_out1).click()
            loginPhone.get_name(self, self.login_out2).click()
            loginPhone.get_id(self, self.login_out3).click()
            loginPhone.get_name(self, self.login_out4).click()  # 退出登录
            loginPhone.get_id(self, self.login_phone_button6).click()

    def click_button1(self):
        loginPhone.get_id(self, self.login_phone_button6).click()  # 点击切换至验证码登录
        loginPhone.find_name(self, self.text1)
        loginPhone.find_name(self, self.text2)
        loginPhone.find_name(self, self.text3)
        loginPhone.find_name(self, self.text4)
        time.sleep(1)
        log.MyLog.info('点击切换至验证码登录pass')

    def click_button2(self):
        if loginPhone.get_text(self, self.login_phone_button2) == '请输入手机号':
            loginPhone.get_id(self, self.login_phone_button5).click()  # 点击忘记密码
            loginPhone.find_toast(self, self.text9)
            time.sleep(1)
        else:
            loginPhone.get_id(self, self.login_phone_button2).click()
            loginPhone.get_id(self, self.login_phone_button10).click()
            loginPhone.get_id(self, self.login_phone_button5).click()  # 点击忘记密码
            loginPhone.find_toast(self, self.text9)
            time.sleep(1)
        log.MyLog.info('未输入手机号时点击忘记密码pass')

    def click_button02(self):
        if loginPhone.get_text(self, self.login_phone_button2) == '请输入手机号':
            loginPhone.get_id(self, self.login_phone_button2).send_keys("12312312312")
            loginPhone.get_id(self, self.login_phone_button5).click()  # 点击忘记密码
            loginPhone.find_name(self, self.text11)
            time.sleep(1)
        else:
            loginPhone.get_id(self, self.login_phone_button5).click()  # 点击忘记密码
            loginPhone.find_name(self, self.text11)
            time.sleep(1)
        log.MyLog.info('输入手机号时点击忘记密码pass')

    def click_button3(self):
        loginPhone.get_id(self, self.login_phone_button2).send_keys("12312312312")
        loginPhone.get_id(self, self.login_phone_button2).click()
        loginPhone.get_id(self, self.login_phone_button10).click()  # 清除手机号
        loginPhone.find_name(self, self.text9)
        time.sleep(1)
        log.MyLog.info('清除手机号pass')

    def click_button4(self):
        loginPhone.get_id(self, self.login_phone_button7).click()  # 点击用户协议
        loginPhone.find_name(self, self.text6)
        time.sleep(1)
        log.MyLog.info('点击用户协议pass')

    def click_button5(self):
        loginPhone.get_id(self, self.login_phone_button8).click()  # 点击隐私政策
        loginPhone.find_name(self, self.text7)
        time.sleep(1)
        log.MyLog.info('点击隐私政策pass')

    def click_button6(self):
        loginPhone.get_id(self, self.login_phone_button2).send_keys("12312312312")
        loginPhone.get_name(self, self.login_phone_button3).send_keys("12312312")
        loginPhone.get_id(self, self.login_phone_button1).click()
        loginPhone.find_toast(self, self.text10)
        time.sleep(1)
        log.MyLog.info('错误账号密码登录pass')

    def click_button7(self):
        loginPhone.get_id(self, self.login_phone_button2).send_keys("12312312312")
        loginPhone.get_name(self, self.login_phone_button3).send_keys('12312312')
        loginPhone.get_id(self, self.login_phone_button4).click()
        loginPhone.find_name(self, '12312312')
        time.sleep(1)
        log.MyLog.info('输入密码点击显密pass')

    def click_button8(self):
        loginPhone.get_id(self, self.login_phone_button4).click()  # 点击显密按键
        time.sleep(1)
        log.MyLog.info('未输入密码是点击显密按键pass')

    def click_button9(self):
        loginPhone.get_id(self, self.login_phone_button9).click()  # 点击返回按键
        loginPhone.find_name(self, self.text8)
        time.sleep(1)
        log.MyLog.info('返回键pass')

    def click_button10(self):
        loginPhone.get_id(self, self.login_phone_button2).send_keys("13456140816")
        loginPhone.get_name(self, self.login_phone_button3).send_keys("Aa123456")
        loginPhone.get_id(self, self.login_phone_button1).click()
        time.sleep(1)
        log.MyLog.info('正确账号密码登录pass')

    def click_button11(self):
        loginPhone.get_id(self, self.login_phone_button12).click()
        time.sleep(1)
        log.MyLog.info('勾选同意隐私政策pass')

    def click_button12(self):
        loginPhone.find_toast(self, self.text13)
        time.sleep(1)
        log.MyLog.info('未勾选同意隐私政策pass')


if __name__ == '__main__':
    driver = appPage.driver()
    loginPhone(driver).login_y_n()
    loginPhone(driver).click_button1()
