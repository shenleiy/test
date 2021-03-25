# coding=utf-8
"""
Created on 2021-1-8
@author:Shenlei
Project:手机号注册登陆页面
"""

from common.public import Element
from common import log
from page.desired_caps.driver_app import appPage
from page.page_device.device_nologin import deviceProject
from page.page_my.login_out import loginOut
import time


class loginProject(Element):
    # text1 = ("密码登录")
    # text2 = ('奥云家')
    # text3 = ("获取验证码")
    # text4 = ('新注册手机验证后自动登录')
    # text5 = ("登录即代表阅读并同意")
    text6 = ("验证码登录")
    text7 = ("密码由8-18位英文字母、数字组成")
    text8 = ("忘记密码？")
    text9 = ("登录")
    text10 = ("请输入手机号")
    text11 = ("请输入密码")
    # 6-11密码登录页面文字
    text12 = ("服务条款")
    text13 = ("奥克斯集团隐私政策")
    text14 = ("手机号登录")
    text15 = ("同意")
    text16 = ("请输入验证码")
    text17 = ("注册")
    text18 = ("数据隐私声明")
    text19 = ("无效的验证码")
    text20 = ("未登录")
    text21 = ("请先阅读并同意《用户协议》和《隐私政策》")
    login_button1 = ('com.broadlink.auxair:id/iv_login_change')  # 切换至密码登录按钮
    login_button2 = ('com.broadlink.auxair:id/edit1')  # 输入手机号按钮
    login_button3 = ('com.broadlink.auxair:id/tv_get_code')  # 获取手机验证码按钮
    login_button4 = ("com.broadlink.auxair:id/btn_login_qq")  # QQ登录按钮
    login_button5 = ("com.broadlink.auxair:id/btn_login_wechat")  # 微信登录按钮
    login_button6 = ("com.broadlink.auxair:id/tv_user_agreement")  # 用户协议按钮
    login_button7 = ("com.broadlink.auxair:id/tv_privacy_policy")  # 隐私政策按钮
    login_button8 = ("com.broadlink.auxair:id/iv_back")  # 返回键按钮
    # login_button9 = ("com.broadlink.auxair:id/tv_next")  # 登录按钮
    # login_button10 = ("com.broadlink.auxair:id/edit1")  # 输入手机号按钮
    # login_button11 = ("请输入密码")  # 输入密码按钮
    # login_button12 = ("com.broadlink.auxair:id/btn_eye")  # 显密按钮
    # login_button13 = ("com.broadlink.auxair:id/tv_forget_pwd")  # 忘记密码按钮
    login_button14 = ("com.broadlink.auxair:id/btn_clear")  # 清除按钮
    login_button15 = ("com.broadlink.auxair:id/et_input_code")  # 输入验证码按钮
    login_button16 = ("com.broadlink.auxair:id/tv_next")  # 注册按钮
    login_button17 = ("com.broadlink.auxair:id/btn1")  # 不同意按钮
    login_button18 = ("com.broadlink.auxair:id/btn2")  # 同意按钮
    login_button19 = ('com.broadlink.auxair:id/tv_home_manage')  # 未登录按钮,用于判断登录与否
    login_button20 = ("com.broadlink.auxair:id/iv_select")
    login_out1 = ("我的")  # 我的按钮
    login_out2 = ("设置")  # 设置按钮
    login_out3 = ("com.broadlink.auxair:id/tv_out")  # 退出登录按钮
    login_out4 = ("确定")  # 确定退出按钮

    def login_y_n(self):  # 用于判断登录与否
        global a
        a = loginProject.get_text(self, self.login_button19)
        print(a)
        if a == '未登录':
            loginProject.get_id(self, self.login_button19).click()  # 进入注册页面
        else:
            loginProject.get_name(self, self.login_out1).click()
            loginProject.get_name(self, self.login_out2).click()
            loginProject.get_id(self, self.login_out3).click()
            loginProject.get_name(self, self.login_out4).click()  # 退出登录

    def click_button1(self):
        loginProject.get_id(self, self.login_button1).click()  # 点击密码登录
        loginProject.find_name(self, self.text6)
        loginProject.find_name(self, self.text7)
        loginProject.find_name(self, self.text8)
        loginProject.find_name(self, self.text9)
        loginProject.find_name(self, self.text11)
        time.sleep(1)
        log.MyLog.info('点击密码登录pass')

    def click_button2(self):
        loginProject.get_id(self, self.login_button4).click()  # 点击QQ登录
        loginProject.find_name(self, self.text14)
        time.sleep(1)
        log.MyLog.info('点击QQ登录pass')

    def click_button3(self):
        loginProject.get_id(self, self.login_button5).click()  # 点击微信登录
        loginProject.find_name(self, self.text15)
        time.sleep(1)
        log.MyLog.info('点击微信登录pass')

    def click_button4(self):
        loginProject.get_id(self, self.login_button6).click()  # 点击用户协议
        loginProject.find_name(self, self.text12)
        time.sleep(1)
        log.MyLog.info('点击用户协议pass')

    def click_button5(self):
        loginProject.get_id(self, self.login_button7).click()  # 点击隐私政策
        loginProject.find_name(self, self.text13)
        time.sleep(1)
        log.MyLog.info('点击隐私政策pass')

    def click_button6(self):
        loginProject.get_id(self, self.login_button2).send_keys("12312312312")  # 未注册过的11位手机号获取验证码
        loginProject.get_id(self, self.login_button3).click()
        loginProject.find_name(self, self.text16)
        time.sleep(1)
        log.MyLog.info('11位手机号获取验证码pass')

    def click_button7(self):
        loginProject.get_id(self, self.login_button15).send_keys('123456')  # 输入验证码
        loginProject.find_name(self, self.text17)
        loginProject.get_id(self, self.login_button16).click()  # 点击注册
        time.sleep(1)
        log.MyLog.info('输入验证码注册pass')

    def click_button8(self):
        # loginProject.get_id(self, self.login_button18).click()  # 提示验证码错误
        loginProject.find_toast(self, self.text19)
        time.sleep(1)
        log.MyLog.info('验证码错误pass')

    def click_button9(self):
        loginProject.get_id(self, self.login_button8).click()  # 点击返回按键
        deviceProject.find_name(self, self.text20)
        time.sleep(1)
        log.MyLog.info('返回键pass')

    def click_button10(self):
        loginProject.get_id(self, self.login_button14).click()  # 点击清除按键
        time.sleep(1)
        log.MyLog.info('清除按钮pass')

    def click_button11(self):
        loginProject.get_id(self, self.login_button20).click()
        time.sleep(1)
        log.MyLog.info('勾选同意隐私政策pass')

    def click_button12(self):
        loginProject.find_toast(self, self.text21)
        time.sleep(1)
        log.MyLog.info('未勾选同意隐私政策pass')


if __name__ == '__main__':
    driver = appPage.driver()
    loginProject(driver).login_y_n()
    loginProject(driver).click_button6()
    loginProject(driver).click_button7()
    loginProject(driver).click_button12()
