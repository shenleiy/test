# coding=utf-8
"""
Created on 2021-1-8
@author:Shenlei
Project:未登陆时的设备页面
"""

from common.public import Element
from common import log
import time


class loginOut(Element):
    login_out1 = ("我的")  # 我的按钮
    login_out2 = ("设置")  # 设置按钮
    login_out3 = ("com.broadlink.auxair:id/tv_out")  # 退出登录按钮
    login_out4 = ("确定")  # 确定退出按钮

    def login_out(self):
        loginOut.get_name(self, self.login_out1).click()
        loginOut.get_name(self, self.login_out2).click()
        loginOut.get_id(self, self.login_out3).click()
        loginOut.get_name(self, self.login_out4).click()  # 退出登录
        log.MyLog.info('退出登录pass')
