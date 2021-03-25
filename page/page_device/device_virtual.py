# coding=utf-8
"""
Created on 2021-1-8
@author:Shenlei
Project:虚拟体验页面
"""

from common.public import Element
from common import log
import time
from page.desired_caps.driver_app import appPage
import random


class virtualProject(Element):
    text1 = ("虚拟体验")
    text2 = ('制冷')
    text3 = ("低档")
    text4 = ('27')
    text5 = ('上下')
    text6 = ('左右')
    text7 = ('仅制热模式有效')
    text8 = ('自动')
    text9 = ('仅制冷模式有效')
    text10 = ('送风模式下无效')
    text11 = ('当前温度')
    text12 = ('26')
    text13 = ('24')
    text14 = ('空调处于锁定状态,解锁之后才能进行相应操作')
    text15 = ('虚拟体验下不可使用该功能')
    text16 = ('已关机')
    virtual_button1 = ("com.broadlink.auxair:id/virtual_experience")  # 虚拟体验按钮
    virtual_button2 = ("com.broadlink.auxair:id/status_pane")  # 图标按钮
    virtual_button3 = ("com.broadlink.auxair:id/go_virtual_device")  # 虚拟体验按钮
    virtual_button4 = ("com.broadlink.auxair:id/tv_temp")  # 温度
    device_button1 = ('com.broadlink.auxair:id/tv_home_manage')  # 未登录按钮
    device_button2 = ("我的")  # 我的按钮

    def login_y_n(self):  # 用于判断登录与否
        a = virtualProject.get_text(self, self.device_button1)
        print(a)
        if a == '未登录':
            virtualProject.get_id(self, self.virtual_button3).click()  # 进入虚拟体验
        else:
            virtualProject.get_name(self, self.device_button2).click()
            virtualProject.get_id(self, self.virtual_button1).click()  # 进入虚拟体验

    def virtual_text(self):
        virtualProject.find_name(self, self.text1)
        virtualProject.find_name(self, self.text2)
        virtualProject.find_name(self, self.text3)
        virtualProject.find_name(self, self.text4)
        virtualProject.find_name(self, self.text5)
        virtualProject.find_name(self, self.text6)
        assert virtualProject.get_text(self, self.virtual_button4) == '27'
        log.MyLog.info('点击虚拟体验pass')

    def click_button1(self):
        virtualProject.get_name(self, '舒风').click()  # 制冷模式下点击舒风
        virtualProject.find_name(self, self.text8)  # 风速切换成自动风
        log.MyLog.info('制冷模式下点击舒风pass')

    # 制冷模式

    def click_button2(self):
        virtualProject.get_name(self, '模式').click()
        virtualProject.get_name(self, '制热').click()  # 切换成制热模式
        time.sleep(1)
        log.MyLog.info('切换成制热模式pass')

    # 制热模式

    def click_button3(self):
        virtualProject.get_name(self, '模式').click()
        virtualProject.get_name(self, '除湿').click()  # 切换成除湿模式
        time.sleep(1)
        log.MyLog.info('切换成除湿模式pass')

    # 除湿模式
    def click_button4(self):
        virtualProject.get_name(self, '模式').click()
        virtualProject.get_name(self, '送风').click()  # 切换成送风模式
        virtualProject.find_name(self, self.text11)
        virtualProject.find_name(self, self.text12)
        assert virtualProject.get_text(self, self.virtual_button4) == '26'
        time.sleep(1)
        log.MyLog.info('切换成送风模式pass')

    # 送风模式

    def click_button5(self):
        virtualProject.get_name(self, '模式').click()
        virtualProject.get_name(self, '自动').click()  # 切换成自动模式
        virtualProject.find_name(self, self.text13)
        assert virtualProject.get_text(self, self.virtual_button4) == '24'
        time.sleep(1)
        log.MyLog.info('切换成自动模式pass')

    # 自动模式

    # def click_button6(self):
    #     virtualProject.get_name(self, 'ECO').click()  # 非制冷模式下点击ECO
    #     virtualProject.find_toast(self, self.text9)
    #     time.sleep(1)
    #     log.MyLog.info('非制冷模式下点击ECO功能pass')

    def click_button7(self):
        virtualProject.get_name(self, '舒风').click()  # 非制冷模式下点击舒风
        virtualProject.find_toast(self, self.text9)
        time.sleep(1)
        log.MyLog.info('非制冷模式下点击舒风pass')

    def click_button8(self):
        virtualProject.get_name(self, '电加热').click()  # 非制热模式下点击电加热
        virtualProject.find_toast(self, self.text7)
        time.sleep(1)
        log.MyLog.info('非制热模式下点击电加热pass')

    def click_button9(self):
        virtualProject.get_name(self, '睡眠').click()  # 送风模式下点击睡眠
        virtualProject.find_toast(self, self.text10)
        time.sleep(1)
        log.MyLog.info('送风模式下点击睡眠pass')

    # 互斥功能弹框判断

    def click_button10(self):
        virtualProject.get_name(self, '童锁').click()  # 开启童锁
        text = ['开关', '风速', '模式', '上下摆风', '左右摆风', '屏显', '电加热', '健康', '舒风', '睡眠']
        for i in range(10):
            a = random.choice(text)
            text.remove(a)
            print('童锁状态下点击:', a)
            virtualProject.get_name(self, a).click()
            virtualProject.find_toast(self, self.text14)
            time.sleep(2)
        log.MyLog.info('童锁下点击任意按钮pass')

    # 童锁功能弹框判断

    def click_button11(self):
        virtualProject.swipe_up(self, '舒睡静眠')  # 点击睡眠diy
        virtualProject.find_toast(self, self.text15)
        time.sleep(1)
        log.MyLog.info('点击舒睡静眠按钮pass')

    def click_button12(self):
        virtualProject.swipe_up(self, '定时')  # 点击定时
        virtualProject.find_toast(self, self.text15)
        time.sleep(1)
        log.MyLog.info('点击定时按钮pass')

    def click_button13(self):
        virtualProject.swipe_up(self, '设备运行日志')  # 点击设备运行日志
        virtualProject.find_toast(self, self.text15)
        time.sleep(1)
        log.MyLog.info('点击设备运行日志按钮pass')

    # 不可使用功能弹框判断

    def click_button14(self):
        virtualProject.swipe_up(self, '开关')  # 点击开关
        virtualProject.find_name(self, '已关机')
        time.sleep(1)
        log.MyLog.info('点击关机按钮pass')

    def click_button15(self):
        virtualProject.swipe_up(self, '清洁')  # 点击清洁
        virtualProject.find_toast(self, self.text15)
        time.sleep(1)
        log.MyLog.info('点击设备运行日志按钮pass')

    def click_button16(self):
        virtualProject.swipe_up(self, '智能省电（ECO）')  # 点击智能省电
        virtualProject.find_toast(self, self.text15)
        time.sleep(1)
        log.MyLog.info('点击设备运行日志按钮pass')


if __name__ == '__main__':
    driver = appPage.driver()
    virtualProject(driver).login_y_n()
    virtualProject(driver).click_button10()
