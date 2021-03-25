# coding=utf-8
"""
Created on 2021-1-19
@author:wangwanqin
Project:报装
"""

from common.public import Element
from page.desired_caps.driver_app import appPage
from common import log
import time


class Appointment(Element):
    basic0 = ('com.broadlink.auxair:id/tv_home_manage')  # 未登录按钮,用于判断登录与否
    basic1 = ("我的")
    basic2 = ("售后服务")
    Appointment1 = ("报装")
    Appointment2 = ("报修")
    Appointment3 = ("工单查询")
    Appointment4 = ("服务声明")
    Appointment5 = ("com.broadlink.auxair:id/sLeftIconId")  # 返回按钮
    Appointment6 = ("预约安装")
    Appointment7 = ("预约维修")

    Install_text1 = ("产品线")
    Install_text1_1 = ("家用空调")
    Install_text1_2 = ("中央空调")

    Install_text2 = ("购买单位类型")
    Install_text2_1 = ("电商-京东-商城")

    Install_text3 = ("购买日期")
    Install_text5 = ("预约日期")
    Install_text3_1 = ("取消")
    Install_text3_2 = ("确定")

    Install_text4 = ("物流状态")
    Install_text4_1 = ("货已到需要安装")
    Install_text4_2 = ("货未到预约安装")

    Install_text6 = ("备注")
    Install_text7 = ("提交")
    Install_text8 = ("com.broadlink.auxair:id/addressPane")  # 联系人信息
    Install_text9 = ("添加联系人")  # 添加联系人
    Install_text9_1 = ("android.widget.ImageView")  # 添加联系人

    toast1 = ("请选择产品线")
    toast2 = ("请选择购买单位类型")
    toast3 = ("请选择购买日期")

    contacts_text1 = ("联系人")
    contacts_text2 = ("手机号码")
    contacts_text3 = ("所在地区")
    contacts_text4 = ("详细地址")
    contacts_text5 = ("保存")
    contacts_text6 = ("联系人姓名")
    contacts_text6_1 = ("com.broadlink.auxair:id/xlabel")
    contacts_text7 = ("收货人手机号码")
    contacts_text7_1 = ("android.widget.EditText")
    contacts_text8 = ("选择所在地区")
    contacts_text9 = ("填写门牌号，如1幢101室")
    contacts_text10 = ("com.broadlink.auxair:id/textView")  # 所在地区

    contacts_text11 = ("保存成功")
    contacts_text12 = ("请填写正确的手机号码")
    contacts_text13 = ("删除")
    contacts_text14 = ("取消")
    contacts_text15 = ("确定")
    contacts_text16 = ("是否确定删除该地址？")
    contacts_text17 = ("编辑")
    contacts_text18 = ("com.broadlink.auxair:id/info1")

    text1 = ("改名称")
    text2 = ("12312312311")

    login_phone_button1 = ("com.broadlink.auxair:id/tv_next")  # 登录按钮
    login_phone_button2 = ("com.broadlink.auxair:id/edit1")  # 输入手机号按钮
    login_phone_button3 = ("请输入密码")  # 输入密码按钮
    login_phone_button4 = ('com.broadlink.auxair:id/iv_login_change')  # 切换至验证码登录按钮
    login_phone_button5 = ("com.broadlink.auxair:id/iv_select")

    family_list_button1 = ("com.broadlink.auxair:id/sLeftIconId")  # 返回按钮

    def login_y_n(self):  # 用于判断登录与否
        global a
        a = Appointment.get_text(self, self.basic0)
        print(a)
        if a == '未登录':
            Appointment.get_id(self, self.basic0).click()
            Appointment.get_id(self, self.login_phone_button4).click()  # 进入登录页面
            Appointment.get_id(self, self.login_phone_button2).send_keys("13456140816")
            Appointment.get_name(self, self.login_phone_button3).send_keys("Aa123456")
            Appointment.get_id(self, self.login_phone_button5).click()
            Appointment.get_id(self, self.login_phone_button1).click()  # 点击登录
            Appointment.get_id(self, self.family_list_button1).click()
            Appointment.get_name(self, self.basic1).click()  # 进入我的页面
            Appointment.get_name(self, self.basic2).click()
        else:
            Appointment.get_name(self, self.basic1).click()  # 进入我的页面
            Appointment.get_name(self, self.basic2).click()

    # def after_service(self):
    #     Appointment.get_name(self, self.basic1).click()
    #     Appointment.get_name(self, self.basic2).click()
    #     time.sleep(2)

    def service_list(self):
        Appointment.find_name(self, self.Appointment1)
        Appointment.find_name(self, self.Appointment2)
        Appointment.find_name(self, self.Appointment3)
        Appointment.find_name(self, self.Appointment4)

    def install_show(self):
        Appointment.get_name(self, self.Appointment1).click()
        time.sleep(3)

    def install_show1(self):
        Appointment.get_name(self, self.Appointment1).click()
        time.sleep(3)
        Appointment.get_id(self, self.Appointment5).click()
        time.sleep(1)

    def install_show2(self):  # 报修
        Appointment.get_name(self, self.Appointment2).click()
        time.sleep(3)
        Appointment.get_id(self, self.Appointment5).click()
        time.sleep(1)

    def install_show3(self):  # 工单查询
        Appointment.get_name(self, self.Appointment3).click()
        time.sleep(3)
        Appointment.get_id(self, self.Appointment5).click()
        time.sleep(1)

    def install_show4(self):  # 服务声明
        Appointment.get_name(self, self.Appointment4).click()
        time.sleep(2)
        Appointment.swipe_to_down(self)
        time.sleep(2)
        Appointment.get_id(self, self.Appointment5).click()
        time.sleep(1)

    def install_show1_1(self):  # 报装
        Appointment.find_name(self, self.Install_text1)
        Appointment.find_name(self, self.Install_text2)
        Appointment.find_name(self, self.Install_text3)
        Appointment.find_name(self, self.Install_text4)
        Appointment.find_name(self, self.Install_text5)
        Appointment.find_name(self, self.Install_text6)
        Appointment.find_name(self, self.Install_text7)

    def install_show2_1(self):  # 报修
        Appointment.get_name(self, self.Appointment2).click()
        time.sleep(3)
        Appointment.find_name(self, self.Appointment7)
        Appointment.find_name(self, self.Install_text1)
        Appointment.find_name(self, self.Install_text2)
        Appointment.find_name(self, self.Install_text3)
        Appointment.find_name(self, self.Install_text5)
        Appointment.find_name(self, self.Install_text6)
        Appointment.find_name(self, self.Install_text7)

    def install_click1(self):  # 产品线
        Appointment.get_name(self, self.Install_text1).click()
        Appointment.find_name(self, self.Install_text1_1)
        Appointment.find_name(self, self.Install_text1_2).click()

    def install_click1_1(self):
        Appointment.get_name(self, self.Install_text1).click()
        Appointment.get_name(self, self.Install_text1_1).click()
        time.sleep(1)
        Appointment.find_name(self, self.Install_text1_1).click()
        time.sleep(1)
        Appointment.get_name(self, self.Install_text1_2).click()
        time.sleep(1)
        Appointment.find_name(self, self.Install_text1_2)

    def install_click2(self):
        Appointment.get_name(self, self.Install_text2).click()
        time.sleep(1)
        Appointment.get_name(self, self.Install_text2_1).click()
        time.sleep(1)

    def install_click3(self):  # 购买日期
        Appointment.get_name(self, self.Install_text3).click()
        time.sleep(2)
        Appointment.get_name(self, self.Install_text3_2).click()

    def install_click4(self):  # 物流状态
        Appointment.get_name(self, self.Install_text4).click()
        Appointment.find_name(self, self.Install_text4_1)
        Appointment.find_name(self, self.Install_text4_2)
        Appointment.get_name(self, self.Install_text4_1).click()
        time.sleep(1)
        Appointment.find_name(self, self.Install_text4_1)

    def install_click4_1(self):
        Appointment.get_name(self, self.Install_text4).click()
        Appointment.get_name(self, self.Install_text4_2).click()
        time.sleep(1)
        Appointment.find_name(self, self.Install_text4_2)

    def install_click5(self):  # 预约日期
        Appointment.get_name(self, self.Install_text5).click()
        time.sleep(1)
        Appointment.get_name(self, self.Install_text3_2).click()

    # def install_click6(self):  # 备注
    #     Appointment.get_name(self, self.Install_text6).click()
    #     time.sleep(1)
    #     Appointment.get_name(self, self.Install_text6).send_keys("测试数据提交")

    def install_click7(self):  # 提交
        Appointment.get_name(self, self.Install_text7).click()
        time.sleep(2)

    def install_toast1(self):  # 提交-产品线未填
        Appointment.get_name(self, self.Appointment1).click()
        time.sleep(1)
        Appointment.get_name(self, self.Install_text7).click()
        time.sleep(0.5)
        Appointment.find_toast(self, self.toast1)

    def install_toast2(self):  # 提交-单位类型未选择
        Appointment.get_name(self, self.Appointment1).click()
        time.sleep(1)
        Appointment.install_click1_1(self)
        Appointment.get_name(self, self.Install_text7).click()
        time.sleep(0.5)
        Appointment.find_toast(self, self.toast2)

    def install_toast3(self):  # 提交-购买日期未选择
        Appointment.get_name(self, self.Appointment1).click()
        time.sleep(1)
        Appointment.install_click1(self)
        Appointment.install_click2(self)
        Appointment.get_name(self, self.Install_text7).click()
        time.sleep(0.5)
        Appointment.find_toast(self, self.toast3)

    def install_toast4(self):  # 提交-购买日期未选择
        Appointment.get_name(self, self.Appointment1).click()
        time.sleep(1)
        Appointment.install_click1_1(self)
        Appointment.install_click2(self)
        Appointment.install_click3(self)
        Appointment.get_name(self, self.Install_text7).click()
        time.sleep(0.5)

    def contacts1(self):
        if Appointment.find_text(self, self.Install_text9):
            Appointment.get_name(self, self.Install_text9).click()
        else:
            Appointment.get_id(self, self.Install_text8).click()
            time.sleep(2)
            images = Appointment.get_class2(self, self.Install_text9_1)
            images[1].click()
            time.sleep(2)

    def contacts2(self):
        Appointment.find_name(self, self.contacts_text6)
        Appointment.find_name(self, self.contacts_text7)
        Appointment.find_name(self, self.contacts_text8)
        Appointment.find_name(self, self.contacts_text9)

    def contacts3(self):
        Appointment.get_name(self, self.contacts_text6).send_keys("联系人a")

    def contacts3_1(self):
        Appointment.get_name(self, self.contacts_text6).send_keys("联系人asdfghjkl1234567890")

    def contacts4(self):  # 手机号填写
        Appointment.get_name(self, self.contacts_text7).send_keys("12345678911")

    def contacts4_1(self):  # 手机号填写
        Appointment.get_name(self, self.contacts_text7).send_keys("联系人a")

    def contacts4_2(self):  # 手机号填写
        Appointment.get_name(self, self.contacts_text7).send_keys("12345")

    def contacts5(self):  # 所在地区选择
        Appointment.get_name(self, self.contacts_text8).click()
        time.sleep(1)
        Appointment.get_id(self, self.contacts_text10).click()
        time.sleep(1)
        Appointment.get_id(self, self.contacts_text10).click()
        time.sleep(1)
        Appointment.get_id(self, self.contacts_text10).click()
        time.sleep(1)
        Appointment.get_id(self, self.contacts_text10).click()

    def contacts6(self):  # 详细地址填写
        Appointment.get_name(self, self.contacts_text9).send_keys("地址A-101")

    def contacts7(self):  # 提交-正确
        time.sleep(1)
        Appointment.get_name(self, self.contacts_text5).click()
        time.sleep(1)
        Appointment.find_toast(self, self.contacts_text11)

    def contacts7_1(self):  # 提交-手机号错误
        Appointment.get_name(self, self.contacts_text5).click()
        time.sleep(1)
        Appointment.find_toast(self, self.contacts_text12)

    def contacts7_2(self):  # 提交按钮判断
        send = Appointment.find_name(self, self.contacts_text5)
        print('内容未填，提交按钮返回结果:', send.is_enabled())
        assert send.is_enabled() == False
        time.sleep(1)
        log.MyLog.info('提交按钮不可点状态pass')

    def contacts8(self):  # 删除联系人-取消
        Appointment.get_id(self, self.Install_text8).click()
        Appointment.get_name(self, self.contacts_text13).click()
        time.sleep(1)
        Appointment.find_name(self, self.contacts_text16)
        time.sleep(2)
        Appointment.get_name(self, self.contacts_text14).click()

    def contacts9(self):  # 删除联系人-确认
        Appointment.get_name(self, self.contacts_text13).click()
        time.sleep(2)
        Appointment.get_name(self, self.contacts_text15).click()

    def contacts10(self):  # 编辑联系人
        Appointment.get_id(self, self.Install_text8).click()
        Appointment.get_name(self, self.contacts_text17).click()
        time.sleep(1)

    def contacts11(self):  # 编辑联系人
        Appointment.get_id(self, self.contacts_text6_1).send_keys(self.text1)
        time.sleep(2)
        Appointment.get_class2(self, self.contacts_text7_1)[1].send_keys(self.text2)
        Appointment.get_name(self, self.contacts_text5).click()
        time.sleep(1)
        a = Appointment.get_text(self, self.contacts_text18)
        if self.text1 in a:
            print("联系人名称修改成功：" + self.text1)
        else:
            print("修改错误")
        if self.text2 in a:
            print("手机号修改成功：" + self.text2)
        else:
            print("修改错误")


if __name__ == '__main__':
    driver = appPage.driver()
    Appointment(driver).login_y_n()
    Appointment(driver).install_show()
    Appointment(driver).contacts1()
    Appointment(driver).contacts3()
    Appointment(driver).contacts4()
    Appointment(driver).contacts5()
    Appointment(driver).contacts6()
    Appointment(driver).contacts7()
