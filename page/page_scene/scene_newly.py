# coding=utf-8
"""
Created on 2021-2-2
@author:Shenlei
Project:测试用例--新增场景（文本及按钮测试）
"""
from common.public import Element
from common import log
from page.desired_caps.driver_app import appPage
import time


class sceneNewly(Element):
    text2 = ("无可添加设备")
    text3 = ("场景")
    text8 = ("新增场景")
    text9 = ("手动触发")
    text10 = ("位置触发")
    text11 = ("时间触发")
    text12 = ("集中控制")
    scene_advice_button0 = ('com.broadlink.auxair:id/tv_home_manage')  # 未登录按钮,用于判断登录与否
    scene_advice_button2 = ("com.broadlink.auxair:id/add_scene")  # 新建场景+按钮
    scene_advice_button12 = ("com.broadlink.auxair:id/btn1")  # 手动触发按钮
    scene_advice_button13 = ("com.broadlink.auxair:id/btn2")  # 位置触发按钮
    scene_advice_button14 = ("com.broadlink.auxair:id/btn3")  # 时间触发按钮
    scene_advice_button15 = ("com.broadlink.auxair:id/btn4")  # 集中控制按钮
    scene_advice_button16 = ("com.broadlink.auxair:id/info")  # 选择设备按钮

    def click_button1(self):
        sceneNewly.get_id(self, self.scene_advice_button2).click()
        sceneNewly.find_name(self, self.text8)
        sceneNewly.find_name(self, self.text9)
        sceneNewly.find_name(self, self.text10)
        sceneNewly.find_name(self, self.text11)
        sceneNewly.find_name(self, self.text12)
        time.sleep(1)
        log.MyLog.info('进入新增场景页pass')

    def click_button2(self):
        sceneNewly.get_id(self, self.scene_advice_button2).click()
        time.sleep(1)
        log.MyLog.info('进入新增场景页pass')

    def click_button3(self):
        sceneNewly.get_id(self, self.scene_advice_button12).click()
        sceneNewly.find_toast(self, self.text2)
        time.sleep(1)
        log.MyLog.info('无设备状态-点击手动触发按钮pass')

    def click_button4(self):
        sceneNewly.get_id(self, self.scene_advice_button12).click()
        sceneNewly.get_id(self, self.scene_advice_button16).click()
        time.sleep(1)
        log.MyLog.info('有设备状态-点击手动触发按钮pass')

    def click_button5(self):
        sceneNewly.get_id(self, self.scene_advice_button13).click()
        sceneNewly.find_toast(self, self.text2)
        time.sleep(1)
        log.MyLog.info('无设备状态-点击位置触发按钮pass')

    def click_button6(self):
        sceneNewly.get_id(self, self.scene_advice_button13).click()
        time.sleep(1)
        log.MyLog.info('有设备状态-点击位置触发按钮pass')

    def click_button7(self):
        sceneNewly.get_id(self, self.scene_advice_button14).click()
        sceneNewly.find_toast(self, self.text2)
        time.sleep(1)
        log.MyLog.info('无设备状态-点击时间触发按钮pass')

    def click_button8(self):
        sceneNewly.get_id(self, self.scene_advice_button14).click()
        time.sleep(1)
        log.MyLog.info('有设备状态-点击时间触发按钮pass')

    def click_button9(self):
        sceneNewly.get_id(self, self.scene_advice_button15).click()
        sceneNewly.find_toast(self, self.text2)
        time.sleep(1)
        log.MyLog.info('无设备状态-点击集中控制按钮pass')

    def click_button10(self):
        sceneNewly.get_id(self, self.scene_advice_button15).click()
        time.sleep(1)
        log.MyLog.info('有设备状态-点击集中控制按钮pass')
