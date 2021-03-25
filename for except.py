# coding=utf-8
"""
Created on 2021-1-6
@author:Shenlei
Project:微信app自动化测试
"""
from appium import webdriver
import yaml
from common import log
from common.public import Element


class appPage(object):

    def driver():
        with open('D:/Python/PyCharm Community Edition 2019.2.3/A+6.0 project/page/desired_caps/desired',
                  'r', encoding='utf-8') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
        desired_caps = {'platformName': data['platformName'],
                        'platformVersion': data['platformVersion'],
                        'deviceName': data['deviceName'],
                        'appPackage': 'com.tencent.mm',
                        'appActivity': 'ui.LauncherUI',
                        'unicodeKeyboard': data['unicodeKeyboard'],  # 是否支持unicode的键盘。如果需要输入中文，要设置为“true”
                        'resetKeyboard': data['resetKeyboard'],  # 是否在测试结束后将键盘重轩为系统默认的输入法。
                        'noReset': 'true',  # true:不重新安装APP，false:重新安装app
                        'automationName': 'uiautomator2'}
        log.MyLog.info('start app...')
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        driver.implicitly_wait(50)  # 隐形等待最长50s
        return driver


class weixin(Element):
    button1 = ('com.tencent.mm:id/b4r')
    button2 = ('com.tencent.mm:id/ala')
    button3 = ('com.tencent.mm:id/iy0')

    def click_button1(self):
        weixin.get_id(self, self.button1).click()
        while True:
            weixin.get_id(self, self.button3).send_keys("[烟花]")
            weixin.get_name(self, '发送').click()


# appPage().get_driver()
if __name__ == '__main__':
    driver = appPage.driver()
    weixin(driver).click_button1()
