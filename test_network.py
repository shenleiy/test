# coding=utf-8
"""
Created on 2021-1-28
@author:Shenlei
Project:测试用例--一键配网（文本及按钮测试）
"""

import pytest
import allure
import os
from page.desired_caps.driver_app import appPage
from page.page_network.device_network import adviceNetwork
import time


@allure.epic('配网')
@allure.feature("一键配网")
class TestClass:
    @allure.story('设备一键配网')
    @allure.title('输入配网次数进行配网测试')
    def test1(self):
        runTimes = input("请输入您要执行的次数：")
        # runTimes = 1
        i = 0
        while i < int(runTimes):
            driver = appPage.driver()
            adviceNetwork(driver).login_y_n()
            adviceNetwork(driver).click_button1()
            driver.quit()
            i = i + 1
            now = time.time()
            now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now))  # 当前时间
            print('\033[4;34m配网执行第%d次\033[0m' % i, now_time)


if __name__ == '__main__':
    pytest.main(['--alluredir', '../report/result/', '--clean-alluredir', 'test_network.py', '-v', '-s'])
    split = 'allure generate ../report/result/ -o ../report/html --clean'
    os.system(split)
