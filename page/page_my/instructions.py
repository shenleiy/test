# coding=utf-8
"""
Created on 2021-1-26
@author:Wangwanqin
Project:产品指南(缺扫码查询)
"""

from common.public import Element
from page.desired_caps.driver_app import appPage
from common import log
import time


class instructions(Element):
    basic0 = ('com.broadlink.auxair:id/tv_home_manage')  # 未登录按钮,用于判断登录与否
    basic1 = ("我的")
    basic2 = ("产品指南")
    instruction1 = ("电子说明书")
    instruction2 = ("产品使用知识")
    instruction3 = ("奥克斯机芯可拆洗空调拆洗教程")
    instruction4 = ("com.broadlink.auxair:id/sLeftIconId")  # 返回

    sn1 = ("请输入设备型号")
    sn2 = ("KFR-35GW/BpR3GYA1+1")
    sn3 = ("KFR-35G/BpUF700(A1)")
    sn4 = ("com.broadlink.auxair:id/model")  # 搜索到的第一条型号
    sn5 = ("1111")
    sn6 = ("取消")
    sn7 = ("扫码查询")
    sn8 = ("com.broadlink.auxair:id/rv_search_result")  # 历史记录
    sn9 = ("android.widget.LinearLayout")  # 查看某条历史记录
    sn10 = ("历史查看")

    deleter_text1 = ("com.broadlink.auxair:id/iv_search_clear")  # 删除历史记录
    deleter_text2 = ("是否确定删除历史查看？")
    deleter_text3 = ("取消")
    deleter_text4 = ("确定")

    knowledge1 = ("知识库")
    knowledge2 = ("2.空调运行的电压范围")
    knowledge3 = ("android.view.View")
    login_phone_button1 = ("com.broadlink.auxair:id/tv_next")  # 登录按钮
    login_phone_button2 = ("com.broadlink.auxair:id/edit1")  # 输入手机号按钮
    login_phone_button3 = ("请输入密码")  # 输入密码按钮
    login_phone_button4 = ('com.broadlink.auxair:id/iv_login_change')  # 切换至验证码登录按钮
    login_phone_button5 = ("com.broadlink.auxair:id/iv_select")

    family_list_button1 = ("com.broadlink.auxair:id/sLeftIconId")  # 返回按钮

    def login_y_n(self):  # 用于判断登录与否
        global a
        a = instructions.get_text(self, self.basic0)
        print(a)
        if a == '未登录':
            instructions.get_id(self, self.basic0).click()
            instructions.get_id(self, self.login_phone_button4).click()  # 进入登录页面
            instructions.get_id(self, self.login_phone_button2).send_keys("13456140816")
            instructions.get_name(self, self.login_phone_button3).send_keys("Aa123456")
            instructions.get_id(self, self.login_phone_button5).click()
            instructions.get_id(self, self.login_phone_button1).click()  # 点击登录
            instructions.get_id(self, self.family_list_button1).click()
            instructions.get_name(self, self.basic1).click()  # 进入我的页面
            instructions.get_name(self, self.basic2).click()
        else:
            instructions.get_name(self, self.basic1).click()  # 进入我的页面
            instructions.get_name(self, self.basic2).click()  # 进入产品指南页面

    # def open(self):
    #     instructions.get_name(self, self.basic1).click()
    #     instructions.get_name(self, self.basic2).click()
    #     time.sleep(2)

    def show1(self):
        instructions.find_name(self, self.instruction1)
        instructions.find_name(self, self.instruction2)
        instructions.find_name(self, self.instruction3)
        time.sleep(1)

    def show2(self):
        instructions.get_name(self, self.instruction1).click()
        time.sleep(1)
        instructions.get_id(self, self.instruction4).click()

    def show3(self):
        instructions.get_name(self, self.instruction2).click()
        time.sleep(1)
        instructions.get_id(self, self.instruction4).click()

    def show4(self):
        instructions.get_name(self, self.instruction3).click()
        time.sleep(1)
        instructions.get_id(self, self.instruction4).click()

    def search1(self):  # 通过带W的型号查询说明书
        instructions.get_name(self, self.instruction1).click()
        time.sleep(1)
        instructions.get_name(self, self.sn1).click()
        time.sleep(1)
        instructions.get_name(self, self.sn1).send_keys(self.sn2)
        time.sleep(1)
        a = instructions.get_text(self, self.sn4)
        assert self.sn2 == a
        print("型号sn2：", self.sn2)
        print("\n型号a：", a)

    def open1(self):  # 通过带W的型号查询说明书
        instructions.get_id(self, self.sn4).click()
        time.sleep(8)
        instructions.swipe_to_up(self)
        time.sleep(5)

    def search2(self):  # 通过不带W的型号查询说明书
        instructions.get_name(self, self.instruction1).click()
        time.sleep(1)
        instructions.get_name(self, self.sn1).click()
        time.sleep(1)
        instructions.get_name(self, self.sn1).send_keys(self.sn3)
        time.sleep(1)

    def search3(self):  # 无对应型号
        instructions.get_name(self, self.instruction1).click()
        time.sleep(1)
        instructions.get_name(self, self.sn1).click()
        time.sleep(1)
        instructions.get_name(self, self.sn1).send_keys(self.sn5)

    def search4(self):  # 通过历史记录查看
        instructions.get_name(self, self.instruction1).click()
        time.sleep(1)
        instructions.get_name(self, self.sn2).click()
        time.sleep(5)

    def search5(self):  # 扫码查询
        instructions.get_name(self, self.instruction1).click()
        time.sleep(1)
        instructions.get_name(self, self.sn7).click()
        time.sleep(1)
        instructions.get_id(self, self.instruction4)

    def deleter1(self):  # 存在一些问题，使用 deleter1_2
        instructions.get_name(self, self.instruction1).click()
        time.sleep(2)
        # noinspection PyBroadException
        try:
            instructions.find_name(self, self.sn10)
            return True
        except Exception:
            return False

    def deleter1_2(self):
        instructions.get_name(self, self.instruction1).click()
        time.sleep(2)
        # instructions.find_name2(self, self.sn10)
        return instructions.find_name2(self, self.sn10)

    def deleter1_1(self):
        instructions.search1(self)
        instructions.get_id(self, self.sn4).click()
        time.sleep(5)
        instructions.get_id(self, self.instruction4).click()
        time.sleep(2)
        instructions.get_name(self, self.sn6).click()

    def deleter2(self):  # 删除
        instructions.get_name(self, self.instruction1).click()
        instructions.find_name(self, self.sn10)
        time.sleep(1)
        instructions.get_id(self, self.deleter_text1).click()
        time.sleep(1)
        instructions.find_name(self, self.deleter_text2)
        instructions.get_name(self, self.deleter_text3).click()

    def deleter3(self):  # 取消删除
        instructions.get_id(self, self.deleter_text1).click()
        time.sleep(1)
        instructions.get_name(self, self.deleter_text3).click()

    def deleter4(self):  # 确认删除
        instructions.get_id(self, self.deleter_text1).click()
        time.sleep(1)
        instructions.get_name(self, self.deleter_text4).click()

    def show_knowledge1(self):
        instructions.get_name(self, self.instruction2).click()
        instructions.find_name(self, self.knowledge1)
        time.sleep(2)
        # instructions.swipe_to_up(self)

    def show_knowledge2(self):
        instructions.get_name(self, self.knowledge2).click()
        time.sleep(1)
        instructions.swipe_to_up(self)
        time.sleep(5)

    def show_knowledge3(self):
        for n in range(0, 6):
            for i in range(0, 8):
                instructions.get_class2(self, self.knowledge3)[(i * 2 + 1)].click()
                time.sleep(1)
                instructions.get_class2(self, self.knowledge3)[(i * 2 + 1)].click()
                print('第', n, '页，', '第', i, '条')
            instructions.swipe_to_up(self)
            time.sleep(3)

    # def show_knowledge3(self):
    #     for n in range(0, 5):
    #         i = 1
    #         while i < 38:
    #             instructions.get_class2(self, self.knowledge3)[3].click()
    #             print('打开第', i + 1, '条')
    #             time.sleep(10)
    #             instructions.get_class2(self, self.knowledge3)[3].click()
    #             print('关闭第', i + 1, '条')
    #             time.sleep(10)
    #             i = i + 1
    #         instructions.swipe_to_up(self)
    #         time.sleep(3)


if __name__ == '__main__':
    driver = appPage.driver()
    instructions(driver).login_y_n()
    instructions(driver).show_knowledge1()
    instructions(driver).show_knowledge3()
