# coding=utf-8
"""
Created on 2021-1-6
@author:Shenlei
Project:方法公共类
"""
from selenium.webdriver.common.by import By
from common import log
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random, re, string
import time


class Element(object):
    def __init__(self, driver):
        self.driver = driver

    def get_text(self, id):
        try:
            return self.driver.find_element_by_id(id).text
        except Exception as e:
            log.MyLog.info('未找到{0}'.format(e))
            raise

            # id文本获取

    def get_xpath_text(self, id):
        try:
            return self.driver.find_element(by=By.XPATH,
                                            value="//*[@resource-id='%s']/android.widget.TextView[2]" % id).text
        except Exception as e:
            log.MyLog.info('未找到{0}'.format(e))
            raise

    # xpath文本获取

    def get_id(self, id):
        self.driver.implicitly_wait(5)
        try:
            return self.driver.find_element_by_id(id)
        except Exception as e:
            log.MyLog.info('未找到{0}'.format(e))
            raise

    # id定位

    def get_name(self, name):
        self.driver.implicitly_wait(5)
        try:
            return self.driver.find_element(by=By.XPATH, value="//*[@text='%s']" % name)
        except Exception as e:
            log.MyLog.info('未找到{0}'.format(e))
            raise

    # name定位
    def get_class(self, classname):
        self.driver.implicitly_wait(5)
        try:
            return self.driver.find_element(by=By.XPATH, value="//*[@class='%s']" % classname)
        except Exception as e:
            log.MyLog.info('未找到{0}'.format(e))
            return

    def get_class2(self, classname):
        self.driver.implicitly_wait(5)
        try:
            return self.driver.find_elements_by_class_name(classname)
        except Exception as e:
            log.MyLog.info('未找到{0}'.format(e))
            return

    def get_xpath_TextView(self, id):
        self.driver.implicitly_wait(5)
        try:
            return self.driver.find_element(by=By.XPATH,
                                            value="//*[@resource-id='%s']/android.widget.TextView[2]" % id)
        except Exception as e:
            log.MyLog.info('未找到{0}'.format(e))
            raise

    # xpath之TextView定位

    def get_xpath(self, id):
        self.driver.implicitly_wait(5)
        try:
            return self.driver.find_element(by=By.XPATH,
                                            value="//*[@resource-id='%s']/android.widget.ImageView[2]" % id)
        except Exception as e:
            log.MyLog.info('未找到{0}'.format(e))
            raise

    # xpath之ImageView定位

    def get_size(self):
        size = self.driver.get_window_size()
        return size

    # 获取手机屏幕尺寸

    def swipe_to_up(self):
        self.driver.implicitly_wait(3)
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 2000)

    # 上滑

    def swipe_to_down(self):
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, 2000)

    # 下滑

    def swipe_to_left(self):
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 4, height / 2, width * 3 / 4, height / 2, 2000)

    # 左滑

    def swipe_to_right(self):
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width * 9 / 10, height / 2, width / 20, height / 2, 2000)

    # 右滑引导页

    def swipe_right(self):
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width * 9 / 10, height / 4, width / 4, height / 4, 2000)

    # 右滑删除场景

    def find_name(self, name):
        self.driver.implicitly_wait(10)  # 隐形等待最长10
        try:
            element = self.driver.find_element(by=By.XPATH, value="//*[@text='%s']" % name)
            print('\033[4;32m页面搜索到判定词：', name, "PASS")
            return element
        except Exception as e:
            log.MyLog.info('未找到{0}'.format(e))
            raise

    # 页面文字判定

    def find_text(self, name):
        self.driver.implicitly_wait(3)  # 隐形等待最长3
        try:
            element = self.driver.find_element(by=By.XPATH, value="//*[@text='%s']" % name)
            print('\033[4;32m页面搜索到判定词：', name, "PASS")
            return element
        except Exception as e:
            pass

    # 页面文字判定

    def find_toast(self, text):
        try:
            toast_loc = (By.XPATH, "//*[contains(@text,'" + text + "')]")
            ele = WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(toast_loc))
            print('\033[4;32m页面搜索到toast词：', text, "PASS")
            return ele.text
        except Exception as e:
            log.MyLog.info('未找到{0}'.format(e))
            raise

    # toast提示框判定

    def find_success(self, name):
        self.driver.implicitly_wait(60)  # 隐形等待最长60
        try:
            element = self.driver.find_element(by=By.XPATH, value="//*[@text='%s']" % name)
            print('\033[4;32m页面搜索到判定词：', name, "PASS")
            return element
        except Exception as e:
            log.MyLog.info('设备配网失败')

    # 配网是否成功判定

    def random_text(self):
        xing = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜'
        X = random.choice(xing)
        a = random.randint(1, 20)
        name = random.sample(string.ascii_letters + string.digits + X, a)
        Name = ''.join(name)
        return Name

    # 随机输入1~20个字符的文本

    def swipe_up(self, name):
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        i = 0
        while i < 5:
            try:
                self.driver.implicitly_wait(1)
                self.driver.find_element(by=By.XPATH, value="//*[@text='%s']" % name).click()  # 尝试点击元素
                return
            except Exception as e:
                self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 2000)
                print("未搜索到元素:", name, ",页面上滑")
                i = i + 1

    # 未搜索到元素，则页面上滑

    def swipe_down(self, name):
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.implicitly_wait(1)
        i = 0
        while i < 5:
            try:
                self.driver.find_element_by_xpath("//*[@text='%s']" % name).click()  # 尝试点击元素
                break
            except Exception as e:
                self.driver.swipe(width / 2, height * 3 / 5, width / 2, height * 19 / 20, 2000)
                print("未搜索到元素:", name, ",页面下滑")
                i = i + 1

    # 未搜索到元素，则页面下滑

    def find_name2(self, name):
        self.driver.implicitly_wait(10)  # 隐形等待最长10
        try:
            element = self.driver.find_element(by=By.XPATH, value="//*[@text='%s']" % name)
            print('\033[4;32m页面搜索到判定词：', name, "PASS")
            return True
        except Exception:
            print("\033[4;31m页面未搜索到判定词：", name, "FAIL")
            return
