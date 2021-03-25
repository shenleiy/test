#coding=utf-8
"""
Created on 2021-2-2
@author:Wangwanqin
Project:设备信息
"""

from common.public import Element
from common import log
import time



class information(Element):
    basic1 = ("设备")
    basic2 = ("我的设备")

    device1 = ("android.view.ViewGroup")
    device2 = ("离线")
    device3 = ("已离线")
    device4 = ("查看离线原因？")
    device5 = ("android.widget.ImageView")  # 进入设备信息页

    information1 = ("设备名称")
    information2 = ("设备SN码")
    information3 = ("Mac地址")
    information4 = ("固件版本")
    information5 = ("历史故障信息")
    information6 = ("移动设备")

    devicename1 = ("com.broadlink.auxair:id/sCenterTitleId")
    devicename2 = ("com.broadlink.auxair:id/tv_input")
    devicename3 = ("android.widget.TextView")
    name1 = ("12345678901234567890")
    name2 = ("奥克斯空调名称字数数量输入测试目前已经够")
    name3 = ("奥克斯空调名称字数数量输入测试已经够二十目前")
    name4 = ("  ")
    name5 = ("！@#￥%")
    name6 = ("asdfghHJKL")

    text1 = ("将设备移动至家庭：")
    text2 = ("完成")
    text3 = ("android.widget.TextView")  # 家庭
    text4 = ("次卧")
    text5 = ("设备移动成功")

    sn1 = ("请输入设备SN码")
    sn2 = ("com.broadlink.auxair:id/tv_input")  # SN输入框
    sn3 = ("com.broadlink.auxair:id/icon_scan")  # SN扫描按钮
    sn4 = ("二维码/条码")
    sn5 = ("确定SN码正确吗？SN码一旦上传将不可修改。")

    button1 = ("取消")
    button2 = ("确定")
    button3 = ("com.broadlink.auxair:id/iv_delete")  # 清除输入信息
    button4 = ("com.broadlink.auxair:id/sLeftIconId")  # 返回上一页
    button5 = ("删除设备")

    toast1 = ("请输入设备名称")
    toast2 = ("设备名称不能超过20位")
    toast3 = ("请输入SN码")

    def open(self):
        information.get_name(self, self.basic1).click()
        information.get_name(self, self.basic2).click()
        information.get_class(self, self.device1).click()
        time.sleep(2)
        information.get_class2(self, self.device5)[1].click()
        time.sleep(2)

    def showdevice(self):  # 有历史故障
        information.find_name(self, self.information1)
        information.find_name(self, self.information2)
        information.find_name(self, self.information3)
        information.find_name(self, self.information4)
        information.find_name(self, self.information5)
        information.find_name(self, self.information6)

    def showdevice_member(self):  # 有历史故障
        information.find_name(self, self.information1)
        information.find_name(self, self.information2)
        information.find_name(self, self.information3)
        information.find_name(self, self.information4)
        information.find_name(self, self.information5)

    def showdevice1(self):  # 无历史故障
        information.find_name(self, self.information1)
        information.find_name(self, self.information2)
        information.find_name(self, self.information3)
        information.find_name(self, self.information4)
        information.find_name(self, self.information6)

    def showdevice1_member(self):  # 无历史故障
        information.find_name(self, self.information1)
        information.find_name(self, self.information2)
        information.find_name(self, self.information3)
        information.find_name(self, self.information4)

    def changename1(self):  # 改设备名，20个数字
        information.find_name(self, self.information1).click()
        time.sleep(1)
        information.get_id(self, self.button3).click()
        information.get_id(self, self.devicename2).send_keys(self.name1)
        information.get_name(self, self.button2).click()
        a = information.get_class2(self, self.devicename3)[2].text
        if self.name1 == a:
            print("名称修改成功")
        else:
            print("修改后显示：", a)
            print("name1为：", self.name1)

    def changename2(self):  # 改设备名，20个汉字
        information.find_name(self, self.information1).click()
        information.get_id(self, self.button3).click()
        information.get_id(self, self.devicename2).send_keys(self.name2)
        information.get_name(self, self.button2).click()
        a = information.get_class2(self, self.devicename3)[2].text
        if a in self.name1:
            print("名称修改成功")
        else:
            print("修改后显示：", a)
            print("name1为：", self.name1)

    def changename3(self):  # 改设备名，22个汉字
        information.find_name(self, self.information1).click()
        information.get_id(self, self.button3).click()
        information.get_id(self, self.devicename2).send_keys(self.name3)
        information.find_toast(self, self.toast2)
        information.get_name(self, self.button2).click()
        time.sleep(1)

    def changename4(self):  # 改设备名，空格
        information.find_name(self, self.information1).click()
        information.get_id(self, self.button3).click()
        information.get_id(self, self.devicename2).send_keys(self.name4)
        information.get_name(self, self.button2).click()
        information.find_toast(self, self.toast1)
        information.get_name(self, self.button1).click()
        time.sleep(1)

    def changename5(self):  # 改设备名，字符
        information.find_name(self, self.information1).click()
        time.sleep(1)
        information.get_id(self, self.button3).click()
        information.get_id(self, self.devicename2).send_keys(self.name5)
        information.get_name(self, self.button2).click()
        a = information.get_class2(self, self.devicename3)[2].text
        if self.name5 == a:
            print("名称修改成功")
        else:
            print("修改后显示：", a)
            print("name1为：", self.name5)

    def changename6(self):  # 改设备名，字母
        information.find_name(self, self.information1).click()
        time.sleep(1)
        information.get_id(self, self.button3).click()
        information.get_id(self, self.devicename2).send_keys(self.name6)
        information.get_name(self, self.button2).click()
        a = information.get_class2(self, self.devicename3)[2].text
        if self.name6 == a:
            print("名称修改成功")
        else:
            print("修改后显示：", a)
            print("name1为：", self.name6)

    def addsn1(self):  # 设备SN码，空的
        information.find_name(self, self.information2).click()
        information.find_name(self, self.sn1)
        information.get_name(self, self.button2).click()
        information.find_toast(self, self.toast3)
        information.get_name(self, self.button1).click()
        time.sleep(1)

    def addsn2(self):  # 设备SN码，输入汉字
        information.find_name(self, self.information2).click()
        information.get_id(self, self.sn2).send_keys(self.name2)
        time.sleep(1)
        n = information.get_text(self, self.sn2)
        assert n == self.sn1, "判断字符是否有输入，当前显示%s" % n

    def addsn3(self):  # 设备SN码，输入字符
        information.find_name(self, self.information2).click()
        information.get_id(self, self.sn2).send_keys(self.name5)
        time.sleep(1)
        n = information.get_text(self, self.sn2)
        assert n == self.sn2, "判断字符是否有输入，当前显示%s" % n

    def addsn4(self):  # 设备SN码，输入字母
        information.find_name(self, self.information2).click()
        information.get_id(self, self.sn2).send_keys(self.name6)
        time.sleep(1)
        n = information.get_text(self, self.sn2)
        assert n == self.name6, "判断字符是否有输入，当前显示%s" % n

    def addsn5(self):  # 设备SN码，输入数字
        information.find_name(self, self.information2).click()
        information.get_id(self, self.sn2).send_keys(self.name1)
        time.sleep(1)
        n = information.get_text(self, self.sn2)
        assert n == self.name1, "判断字符是否有输入，当前显示%s" % n

    def addsn6(self):  # 设备SN码，扫码添加
        information.find_name(self, self.information2).click()
        information.get_id(self, self.sn3).click()
        time.sleep(1)
        information.find_name(self, self.sn4)
        information.get_id(self, self.button4).click()
        time.sleep(1)

    def addsn7(self):  # 设备SN码，取消操作
        information.find_name(self, self.information2).click()
        information.get_id(self, self.sn2).send_keys(self.name1)
        time.sleep(1)
        information.get_name(self, self.button1).click()

    def addsn8(self):  # 设备SN码，再次确认-取消
        information.find_name(self, self.information2).click()
        information.get_id(self, self.sn2).send_keys(self.name1)
        time.sleep(1)
        information.get_name(self, self.button2).click()
        information.find_name(self, self.sn5)
        time.sleep(1)
        information.get_name(self, self.button1).click()

    def addsn9(self):  # 设备SN码，再次确认-确认
        information.find_name(self, self.information2).click()
        information.get_id(self, self.sn2).send_keys(self.name1)
        time.sleep(1)
        information.get_name(self, self.button2).click()
        information.find_name(self, self.sn5)
        time.sleep(0.5)
        information.get_name(self, self.button2).click()

    def history(self):  # 历史故障信息查看
        information.get_name(self, self.information5).click()
        time.sleep(1)
        information.find_name(self, self.information5)
        information.get_name(self, self.button1).click()

    def move1(self):  # 移动设备
        information.get_name(self, self.information6).click()
        time.sleep(1)
        information.find_name(self, self.text1)
        information.get_id(self, self.button4).click()

    def move2(self):  # 移动设备
        information.get_name(self, self.information6).click()
        time.sleep(1)
        information.get_class2(self, self.text3)[7].click()
        time.sleep(1)
        information.get_name(self, self.text4).click()
        information.get_name(self, self.text2).click()
        information.find_name(self, self.text5)

    def check1(self):  # 设备SN码是否需要输入
        a = information.get_class2(self, self.devicename3)[4].text
        if a == "待完善":
            print("sn码未输入", a)
            return a
        else:
            print("sn码已添加", a)
            return 1

    def check2(self):
        a = information.get_class2(self, self.devicename3)[8].text
        print(a)
        if a == 10027:
            print("旧设备无历史故障")
            return False
        elif a == 10031:
            print("旧设备无历史故障")
            return False
        else:
            print("有历史故障")
            return True

