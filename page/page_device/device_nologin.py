# coding=utf-8
"""
Created on 2021-1-8
@author:Shenlei
Project:未登陆时的设备页面
"""

from common.public import Element
from common import log
from page.desired_caps.driver_app import appPage
from page.page_device.device_virtual import virtualProject
import time


class deviceProject(Element):
    text1 = ("未登录")
    text2 = ('场景控制快捷入口')
    text3 = ("添加设备")
    text4 = ('虚拟体验')
    text5 = ("暂无房间信息")
    text6 = ('奥云家')
    text7 = ('密码登录')
    device_button1 = ('com.broadlink.auxair:id/tv_home_manage')  # 未登录按钮
    device_button2 = ("com.broadlink.auxair:id/ll_scene_quick")  # 场景控制快捷入口按钮
    device_button3 = ("com.broadlink.auxair:id/go_virtual_device")  # 虚拟体验按钮
    device_button4 = ("com.broadlink.auxair:id/add_device")  # 添加设备按钮
    device_button5 = ("com.broadlink.auxair:id/tb_moreBtn")  # 右上角+按钮
    device_button6 = ("我的")  # 我的按钮
    device_button7 = ("设置")  # 设置按钮
    device_button8 = ("com.broadlink.auxair:id/tv_out")  # 退出登录按钮
    device_button9 = ("确定")  # 确定退出按钮
    device_button10 = ("com.broadlink.auxair:id/iv_back")  # 返回键按钮

    def login_y_n(self):  # 用于判断登录与否
        global a
        a = deviceProject.get_text(self, self.device_button1)
        print(a)
        if a == '未登录':
            return  # 进入登录页面
        else:
            deviceProject.get_name(self, self.device_button6).click()
            deviceProject.get_name(self, self.device_button7).click()
            deviceProject.get_id(self, self.device_button8).click()
            deviceProject.get_name(self, self.device_button9).click()  # 退出登录
            deviceProject.get_id(self, self.device_button10).click()

    def click_button1(self):
        deviceProject.get_id(self, self.device_button1).click()  # 点击未登陆
        deviceProject.find_name(self, self.text6)
        deviceProject.find_name(self, self.text7)
        time.sleep(1)
        log.MyLog.info('点击未登陆pass')

    def click_button2(self):
        deviceProject.get_id(self, self.device_button2).click()  # 点击场景控制快捷入口
        deviceProject.find_name(self, self.text6)
        deviceProject.find_name(self, self.text7)
        time.sleep(1)
        log.MyLog.info('点击场景控制快捷入口pass')

    def click_button3(self):
        deviceProject.get_id(self, self.device_button3).click()  # 点击虚拟体验

    def click_button4(self):
        deviceProject.get_id(self, self.device_button4).click()  # 点击添加设备
        deviceProject.find_name(self, self.text6)
        deviceProject.find_name(self, self.text7)
        time.sleep(1)
        log.MyLog.info('点击添加设备pass')

    def click_button5(self):
        deviceProject.get_id(self, self.device_button5).click()  # 点击右上角+
        deviceProject.find_name(self, self.text6)
        deviceProject.find_name(self, self.text7)
        time.sleep(1)
        log.MyLog.info('点击右上角+pass')

    def device_text(self):
        log.MyLog.info('-------开始设备列表页面（未登陆状态）文字测试-------')
        deviceProject.find_name(self, self.text1)
        deviceProject.find_name(self, self.text2)
        deviceProject.find_name(self, self.text3)
        deviceProject.find_name(self, self.text4)
        deviceProject.find_name(self, self.text5)
        time.sleep(1)
        log.MyLog.info('-------结束设备列表页面（未登陆状态）文字测试-------')


if __name__ == '__main__':
    driver = appPage.driver()
    deviceProject(driver).login_y_n()
    deviceProject(driver).device_text()
    deviceProject(driver).click_button3()
    virtualProject(driver).virtual_text()
