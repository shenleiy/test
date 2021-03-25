# coding=utf-8
"""
Created on 2021-2-3
@author:Wangwanqin
Project:房间管理，缺改名称后的比对、设备列表及后续操作
"""

from common.public import Element
from common import log
from page.desired_caps.driver_app import appPage
import time
import random


class roomList(Element):
    basic1 = ("设备")
    family1 = ("com.broadlink.auxair:id/tv_home_manage")  # 进入家庭列表页面
    family2 = ("android.widget.ImageView")  # 进入家庭设置页面
    family3 = ("家庭名称")
    family4 = ("房间管理")
    family5 = ("成员管理")

    room0 = ("android.view.ViewGroup")  # 房间
    room1 = ("com.broadlink.auxair:id/tv_room_num")  # 房间数量
    room2 = ("android.widget.ImageView")  # 添加房间按钮
    room3 = ('新建房间名称')
    room4 = ('请输入新建房间名称')
    room5 = ('com.broadlink.auxair:id/tv_input')  # 房间名称输入框
    room6 = ('com.broadlink.auxair:id/iv_delete')  # 房间名称清除按钮
    room7 = ('取消')
    room8 = ('确定')
    room9 = ('房间名称')
    room10 = ('删除房间')
    room11 = ('com.broadlink.auxair:id/sCenterTitleId')  # 房间名称
    room12 = ('是否删除当前房间？')
    room13 = ('com.broadlink.auxair:id/sLeftIconId')  # 返回按钮
    room14 = ('超过可创建房间数量上限')

    device1 = ("设备列表")
    device2 = ("com.broadlink.auxair:id/tv_name")
    device3 = ("设备信息")
    device4 = ("扫码添加设备")

    name1 = ("12345678901234567890")
    name2 = ("奥克斯空调名称字数数量输入测试目前已经够")
    name3 = ("奥克斯空调名称字数数量输入测试已经够二十目前")
    name4 = ("  ")
    name5 = ("！@#￥%")
    name6 = ("asdfghHJKL")
    name7 = ("测试修改房间名称")

    toast1 = ('请输入新建房间名称')
    toast2 = ("新建房间名称不能超过20位")
    toast3 = ("房间添加成功")
    toast4 = ("房间名称修改成功")
    toast5 = ("房间删除成功")

    def room(self):  # 进入房间管理页面
        roomList.get_id(self, self.family1).click()
        time.sleep(1)
        roomList.get_class2(self, self.family2)[3].click()
        time.sleep(2)
        roomList.get_name(self, self.family4).click()
        time.sleep(2)
        log.MyLog.info('进入页面pass')

    def roomName1(self):  # 房间名称，未输入
        roomList.find_name(self, self.family4)
        roomList.get_class2(self, self.room2)[1].click()
        time.sleep(1)
        roomList.get_name(self, self.room8).click()
        roomList.find_toast(self, self.toast1)
        roomList.get_name(self, self.room7).click()
        time.sleep(2)
        log.MyLog.info('未输入名称pass')

    def roomName2(self):  # 房间名称，输入汉字
        roomList.get_class2(self, self.room2)[1].click()
        time.sleep(1)
        roomList.get_id(self, self.room5).send_keys(self.name2)
        time.sleep(1)
        n = roomList.get_id(self, self.room5).text
        assert n == self.name2, "判断字符是否有输入，当前显示%s" % n
        roomList.get_name(self, self.room8).click()
        time.sleep(2)
        log.MyLog.info('输入汉字pass')

    def roomName3(self):  # 房间名称，输入超过20位汉字
        roomList.get_class2(self, self.room2)[1].click()
        time.sleep(1)
        roomList.get_id(self, self.room5).send_keys(self.name3)
        time.sleep(0.5)
        roomList.find_toast(self, self.toast2)
        n = roomList.get_id(self, self.room5).text
        assert n != self.name3, "判断字符是否有输入，当前显示%s" % n
        roomList.get_name(self, self.room8).click()
        time.sleep(2)
        log.MyLog.info('输入20位以上字符pass')

    def roomName4(self):  # 房间名称，输入字符
        roomList.get_class2(self, self.room2)[1].click()
        time.sleep(1)
        roomList.get_id(self, self.room5).send_keys(self.name5)
        n = roomList.get_id(self, self.room5).text
        assert n == self.name5, "判断字符是否有输入，当前显示%s" % n
        roomList.get_name(self, self.room7).click()
        time.sleep(2)

    def roomName5(self):  # 房间名称，输入字母
        roomList.get_class2(self, self.room2)[1].click()
        time.sleep(1)
        roomList.get_id(self, self.room5).send_keys(self.name6)
        time.sleep(1)
        n = roomList.get_text(self, self.room5)
        assert n == self.name6, "判断字符是否有输入，当前显示%s" % n
        roomList.get_name(self, self.room8).click()
        time.sleep(2)
        log.MyLog.info('输入字符pass')

    def roomName6(self):  # 房间名称，输入数字，点击确认
        roomList.get_class2(self, self.room2)[1].click()
        time.sleep(1)
        roomList.get_id(self, self.room5).send_keys(self.name1)
        time.sleep(1)
        n = roomList.get_text(self, self.room5)
        assert n == self.name1, "判断字符是否有输入，当前显示%s" % n
        roomList.get_name(self, self.room8).click()
        roomList.find_toast(self, self.toast3)
        log.MyLog.info('输入数字pass')

    def roomName7(self):  # 房间名称，清空
        roomList.get_class2(self, self.room2)[1].click()
        time.sleep(1)
        roomList.get_id(self, self.room5).send_keys(self.name2)
        time.sleep(1)
        roomList.get_id(self, self.room6).click()

    def roomName8(self):  # 修改房间名称
        roomList.get_class2(self, self.room2)[2].click()
        time.sleep(1)
        roomList.get_name(self, self.room9).click()
        time.sleep(1)
        roomList.get_id(self, self.room5).send_keys(self.name7)
        roomList.get_name(self, self.room8).click()
        time.sleep(0.5)
        roomList.find_toast(self, self.toast4)
        n = roomList.get_text(self, self.room11)
        assert n == self.name7, "判断房间名称是否修改成功，当前显示%s" % n
        log.MyLog.info('修改房间名称pass')

    def roomName9(self):  # 删除房间-取消
        roomList.get_class2(self, self.room2)[2].click()
        time.sleep(1)
        roomList.get_name(self, self.room10).click()
        roomList.find_name(self, self.room12)
        roomList.get_name(self, self.room7).click()
        time.sleep(1)

    def roomName10(self):  # 删除房间-确认
        roomList.get_class2(self, self.room2)[2].click()
        time.sleep(1)
        roomList.get_name(self, self.room10).click()
        roomList.find_name(self, self.room12)
        roomList.get_name(self, self.room8).click()
        time.sleep(1)
        log.MyLog.info('删除房间pass')

    def roomName11(self):  # 判断房间里有无设备
        roomList.get_class2(self, self.room2)[2].click()
        time.sleep(1)
        n = roomList.find_name2(self, self.device1)
        if n == True:
            roomList.get_id(self, self.device2).click()
            time.sleep(1)
            roomList.find_name(self, self.device3)
        else:
            print("该房间下没有设备")

    def roomName12(self):  # 扫码添加设备
        roomList.get_class2(self, self.room2)[2].click()
        time.sleep(1)
        roomList.get_class2(self, self.room2)[1].click()
        time.sleep(1)
        roomList.find_name(self, self.device4)
        roomList.get_id(self, self.room13).click()

    def roomName13(self):  # 添加房间直至最多
        for i in range(1, 36):
            if roomList.find_text(self, self.room14) is None:
                roomList.get_class2(self, self.room2)[1].click()
                time.sleep(1)
                roomList.get_id(self, self.room5).send_keys(random.randint(200, 151212))
                time.sleep(1)
                roomList.get_name(self, self.room8).click()
                print("这是新增的第 %s个房间" % i)
            else:
                print(self.room14)
                time.sleep(1)
                break
        log.MyLog.info('添加房间直至最多pass')

    def roomName14(self):  # 删除房间，直至0
        for i in range(1, 50):
            if roomList.get_class2(self, self.room0):
                roomList.get_class2(self, self.room2)[2].click()
                time.sleep(1)
                roomList.get_name(self, self.room10).click()
                roomList.get_name(self, self.room8).click()
                time.sleep(3)
                print("这是删除的第 %s个房间" % i)
            else:
                print('此时家庭内房间数为0')
                break
        log.MyLog.info('删除房间pass')
