# coding=utf-8
"""
Created on 2021-1-6
@author:Shenlei
Project:App页面启动--不重装App
"""
from appium import webdriver
import yaml
from common import log


class appPage(object):

    def driver():
        with open('D:/Python/PyCharm Community Edition 2019.2.3/A+6.0 project/page/desired_caps/desired',
                  'r', encoding='utf-8') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
        desired_caps = {'platformName': data['platformName'],
                        'platformVersion': data['platformVersion'],
                        'deviceName': data['deviceName'],
                        'appPackage': data['appPackage'],
                        'appActivity': data['appActivity'],
                        'unicodeKeyboard': data['unicodeKeyboard'],  # 是否支持unicode的键盘。如果需要输入中文，要设置为“true”
                        'resetKeyboard': data['resetKeyboard'],  # 是否在测试结束后将键盘重轩为系统默认的输入法。
                        'noReset': data['noReset'],  # true:不重新安装APP，false:重新安装app
                        'automationName': 'uiautomator2'}
        log.MyLog.info('start app...')
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        driver.implicitly_wait(50)  # 隐形等待最长50s
        return driver


# appPage().get_driver()
if __name__ == '__main__':
    appPage.driver()
