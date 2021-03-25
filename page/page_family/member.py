# coding=utf-8
"""
Created on 2021-2-4
@author:Wangwanqin
Project:成员管理
"""

from common.public import Element
from common import log
from page.desired_caps.driver_app import appPage
import time
import random


class memberManage(Element):
    text1 = ('家庭列表')
    text2 = ('新建家庭名称')
    text3 = ('请输入新建家庭名称')
    text5 = ('3个房间 | 0台设备')  # 新建家庭后的房间和设备数
    text6 = ('家庭添加成功')
    text7 = ('家庭设置')
    text8 = ('家庭切换成功')

    basic1 = ("设备")
    family1 = ("com.broadlink.auxair:id/tv_home_manage")  #进入家庭列表页面
    family2 = ("android.widget.ImageView")  # 进入家庭设置页面
    family3 = ("家庭名称")
    family4 = ("房间管理")
    family5 = ("成员管理")

    memberText1 = ("所有成员")
    memberText2 = ("管理员")
    memberText3 = ("我")
    memberText4 = ("删除")
    memberText5 = ("是否删除此成员？")
    memberText6 = ("确定")
    memberText7 = ("取消")
    memberText8 = ("android.widget.LinearLayout")

    def member1(self):  # 进入成员管理页面
        memberManage.get_id(self, self.family1).click()
        time.sleep(1)
        memberManage.get_class2(self, self.family2)[7].click()
        time.sleep(1)
        memberManage.get_name(self, self.family5).click()
        time.sleep(2)
        log.MyLog.info('进入页面pass')

    def member2(self):  # 显示
        memberManage.find_name(self, self.family5)
        memberManage.find_name(self, self.memberText1)
        memberManage.find_name(self, self.memberText2)
        time.sleep(1)
        log.MyLog.info('页面显示pass')

    def swipe_left(self, y):
        window_size = self.get_size()
        width = window_size.get("width")
        self.driver.swipe(width * 3 / 4, y, width / 4, y, 2000)

    def member3(self):  # 显示
        memberManage.swipe_left(self, 600)
        time.sleep(3)
        memberManage.find_name(self, self.memberText4).click()
        memberManage.find_name(self, self.memberText5)
        memberManage.find_name(self, self.memberText7).click()

    def member4(self):  # 显示
        time.sleep(2)
        memberManage.swipe_left(self, 600)
        self.driver.swipe(700, 600, 400, 600)
        time.sleep(3)
        memberManage.find_name(self, self.memberText4).click()
        memberManage.find_name(self, self.memberText5)
        memberManage.find_name(self, self.memberText6).click()

    def member5(self):  # 显示
        if memberManage.get_class2(self, self.memberText8)[1] != False:
            print("有家庭成员")
            return True
        else:
            print("无家庭成员")
            return False

