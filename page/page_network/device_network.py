# coding=utf-8
"""
Created on 2021-1-28
@author:Shenlei
Project:测试用例--设备配网（文本及按钮测试）
"""
from common.public import Element
from common import log
from page.desired_caps.driver_app import appPage
import time
import random, re, string
import yaml


class adviceNetwork(Element):
    advice_network_button0 = ('com.broadlink.auxair:id/tv_home_manage')  # 未登录按钮,用于判断登录与否
    advice_network_button1 = ("com.broadlink.auxair:id/tb_moreBtn")  # 添加设备按钮
    advice_network_button2 = ("com.broadlink.auxair:id/tv_manual")  # 手动选择型号按钮
    advice_network_button3 = ("KFR-35GW/BpBYA700(A1)")  # 选择一个设备机型按钮
    advice_network_button4 = ("com.broadlink.auxair:id/edit1")  # 输入WiFi密码按钮
    advice_network_button5 = ("com.broadlink.auxair:id/btn_next")  # 配网步骤中点击下一步按钮
    advice_network_button6 = ("com.broadlink.auxair:id/iv_check")  # 勾选上述步骤完成按钮
    advice_network_button7 = ("com.broadlink.auxair:id/btn_eye")  # 显密按钮
    advice_network_button8 = ("com.broadlink.auxair:id/tv_next")  # 配网成功后点击下一步按钮

    login_phone_button1 = ("com.broadlink.auxair:id/tv_next")  # 登录按钮
    login_phone_button2 = ("com.broadlink.auxair:id/edit1")  # 输入手机号按钮
    login_phone_button3 = ("请输入密码")  # 输入密码按钮
    login_phone_button4 = ('com.broadlink.auxair:id/iv_login_change')  # 切换至验证码登录按钮
    login_phone_button5 = ("com.broadlink.auxair:id/iv_select")

    family_list_button1 = ("com.broadlink.auxair:id/sLeftIconId")  # 返回按钮

    def login_y_n(self):  # 用于判断登录与否
        with open('D:/Python/PyCharm Community Edition 2019.2.3/A+6.0 project/page/page_network/network',
                  'r', encoding='utf-8') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
        phone = data['phone']
        password = data['password']
        a = adviceNetwork.get_text(self, self.advice_network_button0)
        print(a)
        if a == '未登录':
            adviceNetwork.get_id(self, self.advice_network_button0).click()
            adviceNetwork.get_id(self, self.login_phone_button4).click()  # 进入登录页面
            adviceNetwork.get_id(self, self.login_phone_button2).send_keys(phone)
            adviceNetwork.get_name(self, self.login_phone_button3).send_keys(password)
            adviceNetwork.get_id(self, self.login_phone_button5).click()
            adviceNetwork.get_id(self, self.login_phone_button1).click()  # 点击登录
            adviceNetwork.get_id(self, self.family_list_button1).click()
        else:
            pass

    def click_button1(self):
        with open('D:/Python/PyCharm Community Edition 2019.2.3/A+6.0 project/page/page_network/network',
                  'r', encoding='utf-8') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
        wifi = data['wifi']
        xing = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜'
        X = random.choice(xing)
        a = random.randint(1, 20)
        adviceNetwork.get_id(self, self.advice_network_button1).click()
        adviceNetwork.get_id(self, self.advice_network_button2).click()
        adviceNetwork.get_name(self, self.advice_network_button3).click()  # 选择一个机型
        adviceNetwork.get_id(self, self.advice_network_button4).send_keys(wifi)  # 输入WiFi密码
        adviceNetwork.get_id(self, self.advice_network_button7).click()
        adviceNetwork.get_id(self, self.advice_network_button5).click()
        adviceNetwork.get_id(self, self.advice_network_button6).click()
        adviceNetwork.get_id(self, self.advice_network_button5).click()
        if adviceNetwork.find_success(self, name="已成功添加设备"):
            adviceNetwork.get_id(self, self.advice_network_button8).click()
            adviceNetwork.get_id(self, self.advice_network_button8).click()
            name = random.sample(string.ascii_letters + string.digits + X, a)
            Name = ''.join(name)
            print('空调设备名称为:', Name)
            adviceNetwork.get_id(self, 'com.broadlink.auxair:id/deviceName').send_keys(name)
            adviceNetwork.get_id(self, self.advice_network_button8).click()
            time.sleep(1)
            adviceNetwork.get_id(self, 'com.broadlink.auxair:id/name').click()
            adviceNetwork.get_name(self, '开关').click()
            adviceNetwork.get_id(self, self.family_list_button1).click()
        else:
            print('\033[4;31m配网失败')


if __name__ == '__main__':
    driver = appPage.driver()
    adviceNetwork(driver).login_y_n()
    adviceNetwork(driver).click_button1()
