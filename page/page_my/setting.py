# coding=utf-8
"""
Created on 2021-1-15
@author:Shenlei
Project:设置页面
"""

from common.public import Element
from common import log
from page.desired_caps.driver_app import appPage
import time


class mySetting(Element):
    text1 = ("设置")
    text2 = ('账号安全')
    text3 = ("消息免打扰")
    text4 = ('设备展示方式')
    text5 = ("深色模式")
    text6 = ("去评价")
    text7 = ("关于奥云家")
    text8 = ('退出登录')
    text9 = ('修改密码')
    text10 = ('账号注销')
    text11 = ('手机号更换')
    text12 = ('第三方平台绑定')
    text13 = ('消息设置')
    text14 = ('列表')
    text15 = ('宫格')
    text16 = ('普通模式')
    text17 = ('深色模式')
    text18 = ('去吐槽')
    text19 = ('给好评')
    text20 = ('数据隐私声明')
    text21 = ('官网')
    text22 = ('服务热线')
    text23 = ('分享奥云家')
    text24 = ('已是最新版本')
    text25 = ('确定要退出登录吗?')
    text26 = ('奥云家')
    text27 = ('奥克斯集团隐私政策')
    text28 = ('奥克斯空调')
    text29 = ('‭4008268268‬')
    text30 = ('QQ')
    text31 = ('朋友圈')
    text32 = ('微信')
    text33 = ('保存二维码')
    text34 = ('复制链接')
    text35 = ('意见反馈')
    text36 = ('设置成功')
    setting_button0 = ('com.broadlink.auxair:id/tv_home_manage')  # 未登录按钮,用于判断登录与否
    setting_button1 = ("我的")  # 我的按钮
    setting_button2 = ("com.broadlink.auxair:id/setting")  # 设置按钮
    setting_button3 = ("com.broadlink.auxair:id/tv_change_pwd")  # 账号安全按钮
    setting_button4 = ("com.broadlink.auxair:id/tv_msg_no")  # 消息免打扰按钮
    setting_button5 = ("com.broadlink.auxair:id/tv_device_show")  # 设置方式展示按钮
    setting_button6 = ("com.broadlink.auxair:id/tv_general")  # 深色模式按钮按钮
    setting_button7 = ("com.broadlink.auxair:id/tv_evaluate")  # 去评价按钮
    setting_button8 = ("com.broadlink.auxair:id/tv_about_aux")  # 关于奥云家按钮
    setting_button9 = ("com.broadlink.auxair:id/privacy")  # 数据隐私声明按钮
    setting_button10 = ("com.broadlink.auxair:id/tv_offical")  # 官网按钮
    setting_button11 = ("com.broadlink.auxair:id/tv_service_number")  # 服务热线按钮
    setting_button12 = ("com.broadlink.auxair:id/tv_share_aks")  # 分享奥云家按钮
    setting_button13 = ("com.broadlink.auxair:id/tv_out")  # 退出登录按钮
    setting_button14 = ("com.broadlink.auxair:id/btn_cancel")  # 取消退出登录按钮/去吐槽按钮
    setting_button15 = ("com.broadlink.auxair:id/btn_ok")  # 确定退出登录按钮/给好评按钮
    setting_button16 = ("com.broadlink.auxair:id/sLeftIconId")  # 返回按钮
    setting_button17 = ("com.broadlink.auxair:id/btn_close")  # 关闭去好评按钮
    setting_button18 = ("com.broadlink.auxair:id/ll_select_common")  # 普通模式按钮
    setting_button19 = ("com.broadlink.auxair:id/ll_select_dark")  # 深色模式按钮
    setting_button20 = ("com.broadlink.auxair:id/titlebar")  # 确定按钮/保持按钮
    setting_button21 = ("com.broadlink.auxair:id/iv_select_list")  # 列表选择按钮
    setting_button22 = ("com.broadlink.auxair:id/iv_select_grid")  # 宫格选择按钮
    setting_button23 = ("com.broadlink.auxair:id/iv_open")  # 开启消息免打扰按钮
    setting_button24 = ("com.broadlink.auxair:id/tv_cancel")  # 取消分享奥云家按钮

    login_phone_button1 = ("com.broadlink.auxair:id/tv_next")  # 登录按钮
    login_phone_button2 = ("com.broadlink.auxair:id/edit1")  # 输入手机号按钮
    login_phone_button3 = ("请输入密码")  # 输入密码按钮
    login_phone_button4 = ('com.broadlink.auxair:id/iv_login_change')  # 切换至验证码登录按钮
    login_phone_button5 = ("com.broadlink.auxair:id/iv_select")

    family_list_button1 = ("com.broadlink.auxair:id/sLeftIconId")  # 返回按钮

    def login_y_n(self):  # 用于判断登录与否
        global a
        a = mySetting.get_text(self, self.setting_button0)
        print(a)
        if a == '未登录':
            mySetting.get_id(self, self.setting_button0).click()
            mySetting.get_id(self, self.login_phone_button4).click()  # 进入登录页面
            mySetting.get_id(self, self.login_phone_button2).send_keys("13456140816")
            mySetting.get_name(self, self.login_phone_button3).send_keys("Aa123456")
            mySetting.get_id(self, self.login_phone_button5).click()
            mySetting.get_id(self, self.login_phone_button1).click()  # 点击登录
            mySetting.get_id(self, self.family_list_button1).click()
            mySetting.get_name(self, self.setting_button1).click()  # 进入我的页面
        else:
            mySetting.get_name(self, self.setting_button1).click()  # 进入我的页面

    def click_button1(self):
        mySetting.get_id(self, self.setting_button2).click()  # 点击设置
        mySetting.find_name(self, self.text1)
        mySetting.find_name(self, self.text2)
        mySetting.find_name(self, self.text3)
        mySetting.find_name(self, self.text4)
        mySetting.find_name(self, self.text5)
        mySetting.find_name(self, self.text6)
        mySetting.find_name(self, self.text7)
        mySetting.find_name(self, self.text8)
        time.sleep(1)
        log.MyLog.info('点击设置pass')

    def click_button01(self):
        mySetting.get_id(self, self.setting_button2).click()  # 点击设置
        time.sleep(1)

    def click_button2(self):
        mySetting.get_id(self, self.setting_button3).click()  # 点击账号安全
        mySetting.find_name(self, self.text9)
        mySetting.find_name(self, self.text10)
        mySetting.find_name(self, self.text11)
        mySetting.find_name(self, self.text12)
        time.sleep(1)
        log.MyLog.info('点击账号安全pass')
        log.MyLog.info('【内部的修改密码、账号注销、手机号更改涉及短信验证，仍保持手动黑盒测试】')

    # 消账号安全

    def click_button3(self):
        i = 0
        while i < 2:
            b = mySetting.get_xpath_text(self, self.setting_button4)  # 确认当前消息免打扰状态
            print('当前为', b)
            if b == '关闭':
                mySetting.get_id(self, self.setting_button4).click()  # 点击消息免打扰
                mySetting.find_name(self, self.text13)
                mySetting.get_id(self, self.setting_button23).click()  # 开启消息免打扰
                mySetting.get_xpath_TextView(self, self.setting_button20).click()  # 点击保持
                mySetting.find_toast(self, self.text36)  # 显示设置成功的弹框
                time.sleep(1)
                log.MyLog.info('开启消息免打扰pass')
            else:
                mySetting.get_id(self, self.setting_button4).click()  # 点击消息免打扰
                mySetting.find_name(self, self.text13)
                mySetting.get_id(self, self.setting_button23).click()  # 关闭消息免打扰
                mySetting.get_xpath_TextView(self, self.setting_button20).click()  # 点击保持
                mySetting.find_toast(self, self.text36)  # 显示设置成功的弹框
                assert mySetting.get_xpath_text(self, self.setting_button4) == '关闭'  # 断言切换是否成功
                time.sleep(1)
                log.MyLog.info('关闭消息免打扰pass')
            i += 1

    # 消息免打扰

    def click_button4(self):
        i = 0
        while i < 2:
            b = mySetting.get_xpath_text(self, self.setting_button5)  # 确认当前设备展示方式状态
            print('当前为', b)
            if b == '列表':
                mySetting.get_id(self, self.setting_button5).click()  # 点击设备展示方式
                mySetting.find_name(self, self.text14)
                mySetting.find_name(self, self.text15)
                mySetting.get_id(self, self.setting_button22).click()  # 点击宫格选择按钮
                mySetting.get_id(self, self.setting_button16).click()  # 返回设置页
                assert mySetting.get_xpath_text(self, self.setting_button5) == '宫格'  # 断言切换是否成功
                time.sleep(1)
                log.MyLog.info('切换成宫格模式pass')
            else:
                mySetting.get_id(self, self.setting_button5).click()  # 点击设备展示方式
                mySetting.find_name(self, self.text14)
                mySetting.find_name(self, self.text15)
                mySetting.get_id(self, self.setting_button21).click()  # 点击列表选择按钮
                mySetting.get_id(self, self.setting_button16).click()  # 返回设置页
                assert mySetting.get_xpath_text(self, self.setting_button5) == '列表'  # 断言切换是否成功
                time.sleep(1)
                log.MyLog.info('切换成列表模式pass')
            i += 1

    # 设备展示方式

    def click_button5(self):
        i = 0
        while i < 2:
            b = mySetting.get_xpath_text(self, self.setting_button6)  # 确认当前深色模式状态
            print('当前为', b)
            if b == '普通模式':
                mySetting.get_id(self, self.setting_button6).click()
                mySetting.find_name(self, self.text16)
                mySetting.find_name(self, self.text17)
                mySetting.get_id(self, self.setting_button19).click()  # 切换至深色模式
                mySetting.get_xpath_TextView(self, self.setting_button20).click()  # 点击确定
                assert mySetting.get_xpath_text(self, self.setting_button6) == '深色模式'  # 断言切换是否成功
                time.sleep(1)
                log.MyLog.info('切换成深色模式pass')
            else:
                mySetting.get_id(self, self.setting_button6).click()
                mySetting.find_name(self, self.text16)
                mySetting.find_name(self, self.text17)
                mySetting.get_id(self, self.setting_button18).click()  # 切换至普通模式
                mySetting.get_xpath_TextView(self, self.setting_button20).click()  # 点击确定
                assert mySetting.get_xpath_text(self, self.setting_button6) == '普通模式'  # 断言切换是否成功
                time.sleep(1)
                log.MyLog.info('切换成普通模式pass')
            i += 1

    # 深色模式

    def click_button6(self):
        mySetting.get_id(self, self.setting_button7).click()  # 点击去评价
        mySetting.find_name(self, self.text18)
        mySetting.find_name(self, self.text19)
        mySetting.get_id(self, self.setting_button14).click()  # 点击去吐槽
        mySetting.find_name(self, self.text35)  # 跳转到意见反馈页面
        time.sleep(1)
        log.MyLog.info('点击去吐槽pass')

    def click_button7(self):
        mySetting.get_id(self, self.setting_button7).click()  # 点击去评价
        mySetting.find_name(self, self.text18)
        mySetting.find_name(self, self.text19)
        mySetting.get_id(self, self.setting_button17).click()  # 点击取消
        mySetting.find_name(self, self.text6)  # 保持在设置页面
        time.sleep(1)
        log.MyLog.info('点击取消pass')

    # def click_button8(self):
    #     mySetting.get_id(self, self.setting_button7).click()  # 点击去评价
    #     mySetting.find_name(self, self.text18)
    #     mySetting.find_name(self, self.text19)
    #     mySetting.get_id(self, self.setting_button15).click()  # 点击给好评
    #     mySetting.find_name(self, self.text35)
    #     time.sleep(1)
    #     log.MyLog.info('点击给好评pass')
    # 给好评页面跳转不易断言，仍保持手动黑盒测试
    # 去评价

    def click_button9(self):
        mySetting.get_id(self, self.setting_button8).click()  # 点击关于奥云家
        mySetting.find_name(self, self.text20)
        mySetting.find_name(self, self.text21)
        mySetting.find_name(self, self.text22)
        mySetting.find_name(self, self.text23)
        mySetting.find_name(self, self.text24)
        time.sleep(1)

    def click_button10(self):
        mySetting.get_id(self, self.setting_button8).click()  # 点击关于奥云家
        mySetting.get_id(self, self.setting_button9).click()  # 点击数据隐私声明
        mySetting.find_name(self, self.text27)
        time.sleep(1)
        log.MyLog.info('点击数据隐私声明pass')

    def click_button11(self):
        mySetting.get_id(self, self.setting_button8).click()  # 点击关于奥云家
        mySetting.get_id(self, self.setting_button10).click()  # 点击官网
        mySetting.find_name(self, self.text28)
        time.sleep(1)
        log.MyLog.info('点击官网pass')

    def click_button12(self):
        mySetting.get_id(self, self.setting_button8).click()  # 点击关于奥云家
        mySetting.get_id(self, self.setting_button11).click()  # 点击服务热线
        mySetting.find_name(self, self.text29)
        time.sleep(1)
        log.MyLog.info('点击服务热线pass')

    def click_button13(self):
        mySetting.get_id(self, self.setting_button8).click()  # 点击关于奥云家
        mySetting.get_id(self, self.setting_button12).click()  # 点击分享奥云家
        mySetting.find_name(self, self.text30)
        mySetting.find_name(self, self.text31)
        mySetting.find_name(self, self.text32)
        mySetting.find_name(self, self.text33)
        mySetting.find_name(self, self.text34)
        mySetting.get_id(self, self.setting_button24).click()  # 取消分享奥云家
        time.sleep(1)
        log.MyLog.info('点击分享奥云家pass')

    # 关于奥云家

    def click_button14(self):
        mySetting.get_id(self, self.setting_button13).click()  # 点击退出登录
        mySetting.find_toast(self, self.text25)
        mySetting.get_id(self, self.setting_button14).click()  # 点击取消
        mySetting.find_name(self, self.text8)
        time.sleep(1)
        log.MyLog.info('取消退出登录pass')

    def click_button15(self):
        mySetting.get_id(self, self.setting_button13).click()  # 点击退出登录
        mySetting.find_toast(self, self.text25)
        mySetting.get_id(self, self.setting_button15).click()  # 点击确定
        mySetting.find_name(self, self.text26)
        time.sleep(1)
        log.MyLog.info('确定退出登录pass')

    # 退出登录


if __name__ == '__main__':
    driver = appPage.driver()
    mySetting(driver).login_y_n()
    mySetting(driver).click_button01()
    mySetting(driver).click_button3()
