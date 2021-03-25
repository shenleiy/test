# coding=utf-8
"""
Created on 2021-1-14
@author:
Project:帮助与反馈
"""

from common.public import Element
from common import log
import time



class helpAndfeedback(Element):
    basic1 = ("我的")
    help_feedback1 = ("帮助与反馈")  # 帮助与反馈
    help_feedback2 = ("意见反馈")
    help_button1 = ("com.broadlink.auxair:id/iv_back")  # 返回按钮
    help_button2 = ("com.broadlink.auxair:id/rl_msg")  # 反馈记录按钮
    help_button3 = ("com.broadlink.auxair:id/iv_right")  # 进入反馈内容显示按钮
    help_button4 = ("com.broadlink.auxair:id/iv_send_msg")  # 提交反馈按钮

    feedback1 = ("问题类型")
    feedback2 = ("请描述您要反馈的问题…")
    feedback12 = ("com.broadlink.auxair:id/et_feedback")
    feedback3 = ("添加图片")
    feedback31 = ("选择照片")
    feedback32 = ("从相册选择")
    feedback33 = ("拍照")
    feedback34 = ("取消")

    feedback4 = ("联系电话")
    feedback41 = ("com.broadlink.auxair:id/et_phone")  # 手机号输入框
    feedback42 =("com.broadlink.auxair:id/iv_delete")  # 手机号删除按钮
    feedback43 = ("（选填）便于我们与您取得联系")

    feedback5 = ("留下联系电话我们就能够及时向您反馈解决问题哦！")
    feedback6 = ("提交")
    feedback7 = ("问题类型")
    feedback8 = ("意见反馈成功")
    feedback9 = ("手机号不能超过11位")
    feedback10 = ("com.broadlink.auxair:id/tv_max_num")  # 反馈字数统计
    feedback11 = ("在此输入回复内容…")
    feedback13 = ("com.broadlink.auxair:id/tv_content")  # 反馈记录里具体反馈内容


    help1 = ("账号问题")  # 账号问题
    help2 = ("设备添加")  # 设备添加
    help3 = ("设备管理")  # 设备管理
    help4 = ("功能异常")  # 功能异常
    help5 = ("场景模式")  # 场景模式
    help6 = ("其他问题")  # 场景模式
    help_text = ("还没解决问题？")  # 还没解决问题？

    #账号问题下的帮助内容
    help1_text1 = ("1.账号注册")  # 1.账号注册
    help1_text1_1 = ("账号注册")
    help1_text2 = ("2.账号登录")  # 2.账号登录
    help1_text2_1 = ("账号登录")
    help1_text3 = ("3.忘记密码")  # 3.忘记密码
    help1_text3_1 = ("忘记密码")
    help1_text4 = ("4.第三方账号登录")  # 4.第三方账号登录
    help1_text4_1 = ("第三方账号登录")
    help1_text5 = ("5.修改个人信息")  # 5.修改个人信息
    help1_text5_1 = ("修改个人信息")
    help1_text6 = ("6.修改账号密码")  # 6.修改账号密码
    help1_text6_1 = ("修改账号密码")

    #设备添加下的帮助内容
    help2_text1 = ("1、添加空调设备")  # 1、添加空调设备
    help2_text1_1 = ("添加空调设备")
    help2_text2 = ("2、添加空调设备失败")  # 2、添加空调设备失败
    help2_text2_1 = ("添加空调设备失败")
    help2_text3 = ("3、空调设备复位不成功")  # 3、空调设备复位不成功
    help2_text3_1 = ("空调设备复位不成功")

    #设备管理下的帮助内容
    help3_text1 = ("1、修改空调设备名称")  # 1、修改空调设备名称
    help3_text1_1 = ("修改空调设备名称")
    help3_text2 = ("2、空调设备删除")  # 2、空调设备删除
    help3_text2_1 = ("空调设备删除")
    help3_text3 = ("3、如何设置睡眠DIY")  # 3、如何设置睡眠DIY
    help3_text3_1 = ("如何设置睡眠DIY")
    help3_text4 = ("4、如何分享设备")  # 4、如何分享设备
    help3_text4_1 = ("如何分享设备")

    #功能异常下的帮助内容
    help4_text1 = ("1、空调设备电量功能异常")  # 1、空调设备电量功能异常
    help4_text1_1 = ("空调设备电量功能异常")
    help4_text2 = ("2、设置定时不执行")  # 2、设置定时不执行
    help4_text2_1 = ("设置定时不执行")
    help4_text3 = ("3、显示的控制功能与空调型号不对应")  # 3、显示的控制功能与空调型号不对应
    help4_text3_1 = ("显示的控制功能与空调型号不对应")
    help4_text4 = ("4、设备列表页已经配网的空调设备消失")  # 4、设备列表页已经配网的空调设备消失
    help4_text4_1 = ("设备列表页已经配网的空调设备消失")
    help4_text5 = ("5、设备控制页显示发生故障")  # 5、设备控制页显示发生故障
    help4_text5_1 = ("设备控制页显示发生故障")

    # 场景模式下的帮助内容
    help5_text1 = ("1.如何添加场景模式")  # 1.如何添加场景模式
    help5_text1_1 = ("如何添加场景模式")
    help5_text2 = ("2.场景功能设置未执行")  # 2.场景功能设置未执行
    help5_text2_1 = ("场景功能设置未执行")

    # 其他问题下的帮助内容
    help6_text1 = ("1、空调报装、报修")  # 1、空调报装、报修
    help6_text1_1 = ("空调报装、报修")
    help6_text2 = ("2、空调设备离线")  # 2、空调设备离线
    help6_text2_1 = ("空调设备离线")

    def click_help(self):
        helpAndfeedback.get_name(self, self.basic1).click()
        helpAndfeedback.get_name(self, self.help_feedback1).click()  # 进入帮助反馈页面
        time.sleep(2)

    def click_help_show(self):   # 点击展开账号注册并查看内容
        helpAndfeedback.find_name(self, self.help1)
        helpAndfeedback.find_name(self, self.help2)
        helpAndfeedback.find_name(self, self.help3)
        helpAndfeedback.find_name(self, self.help4)
        helpAndfeedback.find_name(self, self.help5)
        helpAndfeedback.find_name(self, self.help6)

    def click_help_show1(self):   # 点击展开账号注册
        helpAndfeedback.find_name(self, self.help1).click()
        helpAndfeedback.find_name(self, self.help1_text1)
        helpAndfeedback.find_name(self, self.help1_text2)
        helpAndfeedback.find_name(self, self.help1_text3)
        helpAndfeedback.find_name(self, self.help1_text4)
        helpAndfeedback.find_name(self, self.help1_text5)
        helpAndfeedback.find_name(self, self.help1_text6)
        assert helpAndfeedback.find_name(self, self.help1_text1)
        helpAndfeedback.find_name(self, self.help1).click()  # 关闭下拉项
        """
        for语句执行有问题，find_name取不到具体值
                for x1 in range(1,7):
            y1 = "help1_text%d"%(x1)
            print(y1)
            helpAndfeedback.find_name(self, y1)
        """
        time.sleep(2)

    def click_help_show2(self):  # 点击展开设备添加
        helpAndfeedback.find_name(self, self.help2).click()
        helpAndfeedback.find_name(self, self.help2_text1)
        helpAndfeedback.find_name(self, self.help2_text2)
        helpAndfeedback.find_name(self, self.help2_text3)
        assert helpAndfeedback.find_name(self, self.help2_text3)
        helpAndfeedback.find_name(self, self.help2).click()  # 关闭下拉项

    def click_help_show3(self):   # 点击展开设备管理
        helpAndfeedback.find_name(self, self.help3).click()
        helpAndfeedback.find_name(self, self.help3_text1)
        helpAndfeedback.find_name(self, self.help3_text2)
        helpAndfeedback.find_name(self, self.help3_text3)
        helpAndfeedback.find_name(self, self.help3_text4)
        assert helpAndfeedback.find_name(self, self.help3_text3)
        helpAndfeedback.find_name(self, self.help3).click()  # 关闭下拉项

    def click_help_show4(self):   # 点击展开功能异常
        helpAndfeedback.find_name(self, self.help4).click()
        helpAndfeedback.find_name(self, self.help4_text1)
        helpAndfeedback.find_name(self, self.help4_text2)
        helpAndfeedback.find_name(self, self.help4_text3)
        helpAndfeedback.find_name(self, self.help4_text4)
        helpAndfeedback.find_name(self, self.help4_text5)
        assert helpAndfeedback.find_name(self, self.help4_text3)
        helpAndfeedback.find_name(self, self.help4).click()  # 关闭下拉项

    def click_help_show5(self):   # 点击展开场景模式
        helpAndfeedback.find_name(self, self.help5).click()
        helpAndfeedback.find_name(self, self.help5_text1)
        helpAndfeedback.find_name(self, self.help5_text2)
        assert helpAndfeedback.find_name(self, self.help5_text1)
        helpAndfeedback.find_name(self, self.help5).click()  # 关闭下拉项

    def click_help_show6(self):   # 点击展开其他问题
        helpAndfeedback.find_name(self, self.help6).click()
        helpAndfeedback.find_name(self, self.help6_text1)
        helpAndfeedback.find_name(self, self.help6_text2)
        assert helpAndfeedback.find_name(self, self.help6_text1)
        helpAndfeedback.find_name(self, self.help6).click()  # 关闭下拉项

    def click_help_open1(self):
        helpAndfeedback.find_name(self, self.help1).click()
        try:
            assert helpAndfeedback.find_name(self, self.help1_text1)
        except Exception:
            helpAndfeedback.find_name(self, self.help1).click()
        time.sleep(1)

    def click_help_open2(self):
        helpAndfeedback.find_name(self, self.help2).click()
        try:
            assert helpAndfeedback.find_name(self, self.help2_text1)
        except Exception:
            helpAndfeedback.find_name(self, self.help2).click()
        time.sleep(1)

    def click_help_open3(self):
        helpAndfeedback.find_name(self, self.help3).click()
        try:
            assert helpAndfeedback.find_name(self, self.help3_text1)
        except Exception:
            helpAndfeedback.find_name(self, self.help3).click()
        time.sleep(1)

    def click_help_open4(self):
        helpAndfeedback.find_name(self, self.help4).click()
        try:
            assert helpAndfeedback.find_name(self, self.help4_text1)
        except Exception:
            helpAndfeedback.find_name(self, self.help4).click()
        time.sleep(1)

    def click_help_open5(self):
        helpAndfeedback.find_name(self, self.help5).click()
        try:
            assert helpAndfeedback.find_name(self, self.help5_text1)
        except Exception:
            helpAndfeedback.find_name(self, self.help5).click()
        time.sleep(1)

    def click_help_open6(self):
        helpAndfeedback.find_name(self, self.help6).click()
        try:
            assert helpAndfeedback.find_name(self, self.help6_text1)
        except Exception:
            helpAndfeedback.find_name(self, self.help6).click()
        time.sleep(1)


    def click_help1_1(self):   # 查看账号注册详情
        helpAndfeedback.get_name(self, self.help1_text1).click()
        time.sleep(1)
        helpAndfeedback.find_name(self, self.help1)
        helpAndfeedback.find_name(self, self.help1_text1_1)
        helpAndfeedback.get_id(self, self.help_button1).click()
        time.sleep(1)

    def click_help1_2(self):
        helpAndfeedback.get_name(self, self.help1_text2).click()
        time.sleep(1)
        helpAndfeedback.find_name(self, self.help1)
        helpAndfeedback.find_name(self, self.help1_text2_1)
        helpAndfeedback.get_id(self, self.help_button1).click()
        time.sleep(1)

    def click_help1_3(self):
        helpAndfeedback.get_name(self, self.help1_text3).click()
        time.sleep(1)
        helpAndfeedback.find_name(self, self.help1_text3_1)
        helpAndfeedback.find_name(self, self.help1)
        helpAndfeedback.get_id(self, self.help_button1).click()
        time.sleep(1)

    def click_help1_4(self):
        helpAndfeedback.get_name(self, self.help1_text4).click()
        time.sleep(1)
        helpAndfeedback.find_name(self, self.help1).click()
        helpAndfeedback.find_name(self, self.help1_text4_1)
        helpAndfeedback.get_id(self, self.help_button1).click()
        time.sleep(1)

    def click_help1_5(self):
        helpAndfeedback.get_name(self, self.help1_text5).click()
        time.sleep(1)
        helpAndfeedback.find_name(self, self.help1).click()
        helpAndfeedback.find_name(self, self.help1_text5_1).click()
        helpAndfeedback.get_id(self, self.help_button1).click()
        time.sleep(1)

    def click_help1_6(self):
        helpAndfeedback.get_name(self, self.help1_text6).click()
        time.sleep(1)
        helpAndfeedback.find_name(self, self.help1).click()
        helpAndfeedback.find_name(self, self.help1_text6_1).click()
        helpAndfeedback.get_id(self, self.help_button1).click()
        time.sleep(1)
        log.MyLog.info("%s" % helpAndfeedback.help1_text6_1 + "详情")

    def click_help2_1(self):  # 查看账号注册详情
        helpAndfeedback.get_name(self, self.help2_text1).click()
        time.sleep(1)
        helpAndfeedback.find_name(self, self.help2)
        helpAndfeedback.find_name(self, self.help2_text1_1)
        helpAndfeedback.get_id(self, self.help_button1).click()
        time.sleep(1)

    def click_help2_2(self):
        helpAndfeedback.get_name(self, self.help2_text2).click()
        time.sleep(1)
        helpAndfeedback.find_name(self, self.help2)
        helpAndfeedback.find_name(self, self.help2_text2_1)
        helpAndfeedback.get_id(self, self.help_button1).click()
        time.sleep(1)

    def click_help2_3(self):
        helpAndfeedback.get_name(self, self.help2_text3).click()
        time.sleep(1)
        helpAndfeedback.find_name(self, self.help2_text3_1)
        helpAndfeedback.find_name(self, self.help2)
        helpAndfeedback.get_id(self, self.help_button1).click()
        time.sleep(1)

    def click_help3_1(self):  # 查看设备管理详情
        helpAndfeedback.get_name(self, self.help3_text1).click()
        time.sleep(1)
        helpAndfeedback.find_name(self, self.help3)
        helpAndfeedback.find_name(self, self.help3_text1_1)
        helpAndfeedback.get_id(self, self.help_button1).click()
        time.sleep(1)

    def click_help3_2(self):
        helpAndfeedback.get_name(self, self.help3_text2).click()
        time.sleep(1)
        helpAndfeedback.find_name(self, self.help3)
        helpAndfeedback.find_name(self, self.help3_text2_1)
        helpAndfeedback.get_id(self, self.help_button1).click()
        time.sleep(1)

    def click_help3_3(self):
        helpAndfeedback.get_name(self, self.help3_text3).click()
        time.sleep(1)
        helpAndfeedback.find_name(self, self.help3_text3_1)
        helpAndfeedback.find_name(self, self.help3)
        helpAndfeedback.get_id(self, self.help_button1).click()
        time.sleep(1)

    def click_help3_4(self):
        helpAndfeedback.get_name(self, self.help3_text4).click()
        time.sleep(1)
        helpAndfeedback.find_name(self, self.help3).click()
        helpAndfeedback.find_name(self, self.help3_text4_1)
        helpAndfeedback.get_id(self, self.help_button1).click()
        time.sleep(1)

    def click_help4_1(self):  # 查看账号注册详情
        helpAndfeedback.get_name(self, self.help4_text1).click()
        time.sleep(1)
        helpAndfeedback.find_name(self, self.help4)
        helpAndfeedback.find_name(self, self.help4_text1_1)
        helpAndfeedback.get_id(self, self.help_button1).click()
        time.sleep(1)
        log.MyLog.info("%s" % helpAndfeedback.help4_text1_1 + "详情 pass")

    def click_help4_2(self):
        helpAndfeedback.get_name(self, self.help4_text2).click()
        time.sleep(1)
        helpAndfeedback.find_name(self, self.help4)
        helpAndfeedback.find_name(self, self.help4_text2_1)
        helpAndfeedback.get_id(self, self.help_button1).click()
        time.sleep(1)
        log.MyLog.info("%s" % helpAndfeedback.help4_text2_1 + "详情 pass")

    def click_help4_3(self):
        helpAndfeedback.get_name(self, self.help4_text3).click()
        time.sleep(1)
        helpAndfeedback.find_name(self, self.help4_text3_1)
        helpAndfeedback.find_name(self, self.help4)
        helpAndfeedback.get_id(self, self.help_button1).click()
        time.sleep(1)
        log.MyLog.info("%s" % helpAndfeedback.help4_text3_1 + "详情 pass")

    def click_help4_4(self):
        helpAndfeedback.get_name(self, self.help4_text4).click()
        time.sleep(1)
        helpAndfeedback.find_name(self, self.help4).click()
        helpAndfeedback.find_name(self, self.help4_text4_1)
        helpAndfeedback.get_id(self, self.help_button1).click()
        time.sleep(1)
        log.MyLog.info("%s" % helpAndfeedback.help4_text4_1 + "详情 pass")

    def click_help4_5(self):
        helpAndfeedback.get_name(self, self.help4_text5).click()
        time.sleep(1)
        helpAndfeedback.find_name(self, self.help4).click()
        helpAndfeedback.find_name(self, self.help4_text5_1).click()
        helpAndfeedback.get_id(self, self.help_button1).click()
        time.sleep(1)
        log.MyLog.info("%s" % helpAndfeedback.help4_text5_1 + "详情 pass")

    def click_help5_1(self):  # 查看账号注册详情
        helpAndfeedback.get_name(self, self.help5_text1).click()
        time.sleep(1)
        helpAndfeedback.find_name(self, self.help5)
        helpAndfeedback.find_name(self, self.help5_text1_1)
        helpAndfeedback.get_id(self, self.help_button1).click()
        time.sleep(1)
        log.MyLog.info("%s" % helpAndfeedback.help5_text1_1 + "详情 pass")

    def click_help5_2(self):
        helpAndfeedback.get_name(self, self.help5_text2).click()
        time.sleep(1)
        helpAndfeedback.find_name(self, self.help5)
        helpAndfeedback.find_name(self, self.help5_text2_1)
        helpAndfeedback.get_id(self, self.help_button1).click()
        time.sleep(1)
        log.MyLog.info("%s" % helpAndfeedback.help5_text2_1 + "详情 pass")

    def click_help6_1(self):  # 查看账号注册详情
        helpAndfeedback.get_name(self, self.help6_text1).click()
        time.sleep(1)
        helpAndfeedback.find_name(self, self.help6)
        helpAndfeedback.find_name(self, self.help6_text1_1)
        helpAndfeedback.get_id(self, self.help_button1).click()
        time.sleep(1)
        log.MyLog.info("%s" % helpAndfeedback.help6_text1_1 + "详情 pass")

    def click_help6_2(self):
        helpAndfeedback.get_name(self, self.help6_text2).click()
        time.sleep(1)
        helpAndfeedback.find_name(self, self.help6)
        helpAndfeedback.find_name(self, self.help6_text2_1)
        helpAndfeedback.get_id(self, self.help_button1).click()
        time.sleep(1)
        log.MyLog.info("%s" % helpAndfeedback.help6_text2_1 + "详情 pass")
    
    def click_help2(self):  # 点击展开设备添加并查看内容
        helpAndfeedback.get_name(self, self.help2).click()
        helpAndfeedback.find_name(self, self.help2_text1)
        helpAndfeedback.get_name(self, self.help2_text1).click()
        time.sleep(1)
        helpAndfeedback.get_id(self, self.help_button1).click()

        helpAndfeedback.find_name(self, self.help2_text2)
        helpAndfeedback.get_name(self, self.help2_text2).click()
        time.sleep(1)
        helpAndfeedback.get_id(self, self.help_button1).click()

        helpAndfeedback.find_name(self, self.help2_text3)
        helpAndfeedback.get_name(self, self.help2_text3).click()
        time.sleep(1)
        helpAndfeedback.get_id(self, self.help_button1).click()
        log.MyLog.info('设备添加下内容展示pass')

    def click_help3(self):
        helpAndfeedback.get_name(self, self.help3).click()  # 点击展开设备管理
        helpAndfeedback.find_name(self, self.help3_text1)
        helpAndfeedback.get_name(self, self.help3_text1).click()
        time.sleep(1)
        helpAndfeedback.get_id(self, self.help_button1).click()

        helpAndfeedback.find_name(self, self.help3_text2)
        helpAndfeedback.get_name(self, self.help3_text2).click()
        time.sleep(1)
        helpAndfeedback.get_id(self, self.help_button1).click()

        helpAndfeedback.find_name(self, self.help3_text3)
        helpAndfeedback.get_name(self, self.help3_text3).click()
        time.sleep(1)
        helpAndfeedback.get_id(self, self.help_button1).click()

        helpAndfeedback.find_name(self, self.help3_text4)
        helpAndfeedback.get_name(self, self.help3_text4).click()
        time.sleep(1)
        helpAndfeedback.get_id(self, self.help_button1).click()

        log.MyLog.info('设备管理下内容展示pass')

    def click_help4(self):
        helpAndfeedback.get_name(self, self.help4).click()  # 点击展开功能异常
        helpAndfeedback.find_name(self, self.help4_text1)
        helpAndfeedback.get_name(self, self.help4_text1).click()
        time.sleep(1)
        helpAndfeedback.get_id(self, self.help_button1).click()

        helpAndfeedback.find_name(self, self.help4_text2)
        helpAndfeedback.get_name(self, self.help4_text2).click()
        time.sleep(1)
        helpAndfeedback.get_id(self, self.help_button1).click()

        helpAndfeedback.find_name(self, self.help4_text3)
        helpAndfeedback.get_name(self, self.help4_text3).click()
        time.sleep(1)
        helpAndfeedback.get_id(self, self.help_button1).click()

        helpAndfeedback.find_name(self, self.help4_text4)
        helpAndfeedback.get_name(self, self.help4_text4).click()
        time.sleep(1)
        helpAndfeedback.get_id(self, self.help_button1).click()

        helpAndfeedback.find_name(self, self.help4_text5)
        helpAndfeedback.get_name(self, self.help4_text5).click()
        time.sleep(1)
        helpAndfeedback.get_id(self, self.help_button1).click()

        log.MyLog.info('功能异常下内容展示pass')

    def click_help5(self):
        helpAndfeedback.get_name(self, self.help5).click()  # 点击展开场景模式
        helpAndfeedback.find_name(self, self.help5_text1)
        helpAndfeedback.get_name(self, self.help5_text1).click()
        time.sleep(1)
        helpAndfeedback.get_id(self, self.help_button1).click()

        helpAndfeedback.find_name(self, self.help5_text2)
        helpAndfeedback.get_name(self, self.help5_text2).click()
        time.sleep(1)
        helpAndfeedback.get_id(self, self.help_button1).click()

        log.MyLog.info('场景模式下内容展示pass')

    def click_help6(self):
        helpAndfeedback.get_name(self, self.help6).click()  # 点击展开其他问题
        helpAndfeedback.find_name(self, self.help6_text1)
        helpAndfeedback.get_name(self, self.help6_text1).click()
        time.sleep(1)
        helpAndfeedback.get_id(self, self.help_button1).click()

        helpAndfeedback.find_name(self, self.help6_text2)
        helpAndfeedback.get_name(self, self.help6_text2).click()
        time.sleep(1)
        helpAndfeedback.get_id(self, self.help_button1).click()

        log.MyLog.info('其他问题下内容展示pass')

    def click_feedback1(self):      # 进入意见反馈页
        helpAndfeedback.get_name(self, self.help_feedback2).click()
        time.sleep(1)
        helpAndfeedback.get_name(self, self.help2).click()
        time.sleep(1)
        helpAndfeedback.find_name(self, self.help2)
        log.MyLog.info('进入意见反馈页面pass')

    def click_feedback1_1(self):  # 判定意见反馈页显示内容
        helpAndfeedback.find_name(self, self.feedback2)
        helpAndfeedback.find_name(self, self.feedback3)
        helpAndfeedback.find_name(self, self.feedback4)
        helpAndfeedback.find_name(self, self.feedback5)
        helpAndfeedback.find_name(self, self.feedback6)

        log.MyLog.info('意见反馈页面内容展示pass')

    def click_feedback2(self):      # 判定通过还没解决问题进入意见反馈页面
        helpAndfeedback.get_name(self, self.help5).click()  # 点击展开场景模式
        helpAndfeedback.find_name(self, self.help5_text1)
        helpAndfeedback.get_name(self, self.help5_text1).click()
        time.sleep(2)
        helpAndfeedback.find_name(self, self.help_text).click()
        time.sleep(1)
        helpAndfeedback.find_name(self, self.help5)
        helpAndfeedback.find_name(self, self.feedback2)

        log.MyLog.info('进入意见反馈页面pass')

    def click_feedback3(self):      # 问题类型选择
        helpAndfeedback.get_name(self, self.help_feedback2).click()
        helpAndfeedback.find_name(self, self.help1).click()
        time.sleep(1)
        helpAndfeedback.find_name(self, self.help1).click()
        time.sleep(1)

        helpAndfeedback.find_name(self, self.help2).click()
        time.sleep(1)
        helpAndfeedback.find_name(self, self.help2).click()
        time.sleep(1)

        helpAndfeedback.find_name(self, self.help3).click()
        time.sleep(1)
        helpAndfeedback.find_name(self, self.help3).click()
        time.sleep(1)

        helpAndfeedback.find_name(self, self.help4).click()
        time.sleep(1)
        helpAndfeedback.find_name(self, self.help4).click()
        time.sleep(1)

        helpAndfeedback.find_name(self, self.help5).click()
        time.sleep(1)
        helpAndfeedback.find_name(self, self.help5).click()
        time.sleep(1)

        helpAndfeedback.find_name(self, self.help6).click()
        time.sleep(1)
        helpAndfeedback.find_name(self, self.help6)

        log.MyLog.info('问题类型选择pass')

    def click_feedback4(self):      # 提交按钮判断
        send = helpAndfeedback.find_name(self, self.feedback6)
        print('内容未填，提交按钮返回结果:', send.is_enabled())
        assert send.is_enabled() == False
        time.sleep(1)
        log.MyLog.info('提交按钮不可点状态pass')

    def click_feedback4_1(self):  # 提交按钮判断
        send = helpAndfeedback.find_name(self, self.feedback6)
        helpAndfeedback.get_id(self, self.feedback12).send_keys("test")
        time.sleep(1)
        print('内容填写后，提交按钮返回结果:', send.is_enabled())
        assert send.is_enabled()
        time.sleep(1)
        log.MyLog.info('提交按钮可点状态pass')

    def click_feedback5(self):  # 反馈内容字数统计
        helpAndfeedback.get_id(self, self.feedback12).send_keys("测试pytest123")
        time.sleep(2)
        mes1 = helpAndfeedback.get_id(self, self.feedback10).text
        try:
            assert mes1 == u'11/200'
            print('字数统计正确')
        except Exception as e:
            print('字数统计错误')

        log.MyLog.info('反馈内容字数统计pass')

    def click_feedback6(self):  # 反馈内容字数限制
        try:
            sendkey1 = ("对于测试来讲，不管是功能测试，自动化测试，还是单元测试。一般都会预设一个正确的预期结果，而在测试执行的过程中会得到一个实际的结果。测试的成功与否就是拿实际的结果与预期的结果进行比较。这个比的过程实际就是断言（assert）。在unittest单元测试框架中提供了丰富的断言方法，如assertEqual()、、assertTrue()、assertIs()等，而pytest直接使用assert进行断言")
            helpAndfeedback.get_id(self, self.feedback12).send_keys(sendkey1)
            mes2 = helpAndfeedback.get_id(self, self.feedback12).text
            assert mes2 == sendkey1
            print('反馈内容超过200字，fail')
        except Exception:
            print('反馈能容不能超过200字判断正确输入文字：', sendkey1)
            print('实际输入：', mes2)
        log.MyLog.info('反馈内容字数限制pass')

    def click_feedback7(self):  # 手机号输入限制
        helpAndfeedback.get_id(self, self.feedback41).send_keys("111111111111")
        helpAndfeedback.find_toast(self, self.feedback9)
        time.sleep(5)
        log.MyLog.info('手机号输入限制pass')

    def click_feedback8(self):  # 手机号删除
        helpAndfeedback.get_id(self, self.feedback41).click()
        time.sleep(1)
        helpAndfeedback.get_id(self, self.feedback42).click()
        helpAndfeedback.find_name(self, self.feedback43)
        time.sleep(1)
        log.MyLog.info('手机号删除pass')

    def click_feedback9(self):  # 添加图片
        helpAndfeedback.get_name(self, self.feedback3).click()
        time.sleep(1)
        helpAndfeedback.find_name(self, self.feedback31)
        helpAndfeedback.find_name(self, self.feedback32)
        helpAndfeedback.find_name(self, self.feedback33)
        helpAndfeedback.find_name(self, self.feedback34).click()
        log.MyLog.info('添加图片选项pass')

    def click_feedback10_1(self):  # 提交意见反馈
        helpAndfeedback.find_name(self, self.feedback6).click()
        time.sleep(0.5)
        helpAndfeedback.find_toast(self, self.feedback8)
        time.sleep(5)
        log.MyLog.info('提交意见反馈pass')

    def click_feedback10(self):  # 提交意见反馈
        helpAndfeedback.get_name(self, self.help_feedback2).click()
        time.sleep(1)
        helpAndfeedback.find_name(self, self.help2).click()
        time.sleep(2)
        helpAndfeedback.get_id(self, self.feedback12).send_keys("测试pytest123")  # 内容
        helpAndfeedback.get_id(self, self.feedback41).send_keys("12111111111")  # 手机号
        time.sleep(2)
        helpAndfeedback.find_name(self, self.feedback6).click()
        time.sleep(0.5)
        helpAndfeedback.find_toast(self, self.feedback8)
        time.sleep(5)
        log.MyLog.info('提交意见反馈pass')

    def click_feedback11(self):  # 查看提交的意见反馈
        helpAndfeedback.get_id(self, self.help_button1).click()
        time.sleep(1)
        helpAndfeedback.get_id(self, self.help_button2).click()
        time.sleep(1)
        helpAndfeedback.find_name(self, self.help2).click()

    def click_feedback12(self):  # 反馈记录
        helpAndfeedback.get_id(self, self.help_button2).click()
        time.sleep(2)
        helpAndfeedback.get_id(self, self.help_button3).click()
        time.sleep(1)
        helpAndfeedback.find_name(self, self.feedback11).send_keys("再次反馈")
        helpAndfeedback.get_id(self, self.help_button4).click()
        helpAndfeedback.get_text(self, self.feedback13)


























