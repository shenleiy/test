# coding=utf-8
"""
Created on 2021-1-20
@author:Shenlei
Project:测试用例--推荐场景（文本及按钮测试）
"""
from common.public import Element
from common import log
from page.desired_caps.driver_app import appPage
import time


class sceneRecommend(Element):
    text1 = ("请选择有效设备")
    text2 = ("无可添加设备")
    text3 = ("场景")
    text4 = ("推荐场景")
    text5 = ("回家（手动）")
    text6 = ("离家（手动）")
    text7 = ("多设备快捷控制")
    text8 = ("场景日志")
    text9 = ("空调设备离线")
    text10 = ("还没解决问题？")
    # text11 = ("时间触发")
    # text12 = ("集中控制")
    text13 = ("保存成功")
    text14 = ("执行成功")
    text15 = ("默认场景不允许删除")
    text16 = ("删除成功")
    scene_advice_button0 = ('com.broadlink.auxair:id/tv_home_manage')  # 未登录按钮,用于判断登录与否
    scene_advice_button1 = ("com.broadlink.auxair:id/scene_log")  # 场景日志按钮
    scene_advice_button2 = ("com.broadlink.auxair:id/iv_back")  # 其他问题页面返回按钮
    scene_advice_button3 = ("com.broadlink.auxair:id/ll_back")  # 回家(手动)按钮
    scene_advice_button4 = ("com.broadlink.auxair:id/ll_out")  # 离家(手动)按钮
    scene_advice_button5 = ("com.broadlink.auxair:id/ll_duo")  # 多设备快捷控制按钮
    scene_advice_button6 = ("com.broadlink.auxair:id/btn1")  # 推荐按钮
    scene_advice_button7 = ("com.broadlink.auxair:id/btn2")  # 我的按钮
    scene_advice_button8 = ("com.broadlink.auxair:id/sLeftIconId")  # 返回按钮
    scene_advice_button9 = ("com.broadlink.auxair:id/titlebar")  # 确定按钮
    scene_advice_button10 = ("com.broadlink.auxair:id/name")  # 继续添加设备按钮
    scene_advice_button11 = ("com.broadlink.auxair:id/tv_device")  # 选择设备按钮
    scene_advice_button12 = ("com.broadlink.auxair:id/iv_all_select")  # 全选按钮
    scene_advice_button13 = ("com.broadlink.auxair:id/tv_offline_reason")  # 查看离线原因按钮
    scene_advice_button14 = ("com.broadlink.auxair:id/tv_name")  # 意见反馈问题类型
    scene_advice_button15 = ("com.broadlink.auxair:id/sCenterTitleId")  # 集中控制名称
    scene_advice_button16 = ("com.broadlink.auxair:id/info")  # 选择设备按钮
    scene_advice_button17 = ("com.broadlink.auxair:id/tv_action")  # 设备状态判断
    scene_advice_button18 = ("com.broadlink.auxair:id/btn_ok")  # 场景命名确定按钮
    scene_advice_button19 = ("com.broadlink.auxair:id/exePane")  # 场景执行按钮
    scene_advice_button20 = ("com.broadlink.auxair:id/iv_delete")  # 场景名称清除按钮
    scene_advice_button21 = ("com.broadlink.auxair:id/tv_input")  # 场景名称输入按钮
    scene_advice_button22 = ("com.broadlink.auxair:id/open_device")  # 开机按钮
    scene_advice_button23 = ("com.broadlink.auxair:id/close_device")  # 关机按钮
    scene_advice_button24 = ("com.broadlink.auxair:id/info1")  # 制冷模式按钮
    scene_advice_button25 = ("com.broadlink.auxair:id/info2")  # 制热模式按钮
    scene_advice_button26 = ("com.broadlink.auxair:id/info3")  # 除湿模式按钮
    scene_advice_button27 = ("com.broadlink.auxair:id/info4")  # 送风模式按钮
    scene_advice_button28 = ("com.broadlink.auxair:id/info5")  # 自动模式按钮
    scene_advice_button29 = ("com.broadlink.auxair:id/iv_temp")  # 温度勾选按钮
    scene_advice_button30 = ("com.broadlink.auxair:id/tv_temp")  # 温度显示状态
    scene_advice_button31 = ("com.broadlink.auxair:id/sb_temp")  # 温度条按钮
    scene_advice_button32 = ("com.broadlink.auxair:id/btnDel")  # 删除场景按钮
    scene_advice_button33 = ("com.broadlink.auxair:id/tv_title")  # 离线问题状态

    login_phone_button1 = ("com.broadlink.auxair:id/tv_next")  # 登录按钮
    login_phone_button2 = ("com.broadlink.auxair:id/edit1")  # 输入手机号按钮
    login_phone_button3 = ("请输入密码")  # 输入密码按钮
    login_phone_button4 = ('com.broadlink.auxair:id/iv_login_change')  # 切换至验证码登录按钮
    login_phone_button5 = ("com.broadlink.auxair:id/iv_select")

    def login_y_n(self):  # 用于判断登录与否
        global a
        a = sceneRecommend.get_text(self, self.scene_advice_button0)
        print(a)
        if a == '未登录':
            sceneRecommend.get_id(self, self.scene_advice_button0).click()
            sceneRecommend.get_id(self, self.login_phone_button4).click()  # 进入登录页面
            sceneRecommend.get_id(self, self.login_phone_button2).send_keys("13456140816")
            sceneRecommend.get_name(self, self.login_phone_button3).send_keys("Aa123456")
            sceneRecommend.get_id(self, self.login_phone_button5).click()
            sceneRecommend.get_id(self, self.login_phone_button1).click()  # 点击登录
            sceneRecommend.get_id(self, self.scene_advice_button8).click()
            sceneRecommend.get_name(self, self.text3).click()  # 进入场景页面
        else:
            sceneRecommend.get_name(self, self.text3).click()  # 进入场景页面

    def click_button1(self):
        sceneRecommend.get_id(self, self.scene_advice_button6).click()
        sceneRecommend.get_id(self, self.scene_advice_button3).click()
        sceneRecommend.find_name(self, self.text4)
        time.sleep(1)
        log.MyLog.info('点击回家(手动)pass')

    def click_button2(self):
        sceneRecommend.get_id(self, self.scene_advice_button6).click()
        sceneRecommend.get_id(self, self.scene_advice_button4).click()
        sceneRecommend.find_name(self, self.text4)
        time.sleep(1)
        log.MyLog.info('点击离家(手动)pass')

    def click_button3(self):
        sceneRecommend.get_id(self, self.scene_advice_button6).click()
        sceneRecommend.get_id(self, self.scene_advice_button5).click()
        sceneRecommend.find_toast(self, self.text2)
        time.sleep(1)
        log.MyLog.info('无设备状态-点击多设备快捷控制pass')

    def click_button4(self):
        sceneRecommend.get_xpath_TextView(self, self.scene_advice_button9).click()
        sceneRecommend.find_toast(self, self.text1)
        time.sleep(1)
        log.MyLog.info('未添加设备点击确定pass')

    def click_button5(self):
        sceneRecommend.get_id(self, self.scene_advice_button10).click()
        sceneRecommend.find_toast(self, self.text2)
        time.sleep(1)
        log.MyLog.info('无设备状态-点击继续添加设备pass')

    def click_button6(self):
        sceneRecommend.get_id(self, self.scene_advice_button10).click()
        time.sleep(1)
        b = sceneRecommend.get_text(self, self.scene_advice_button16)
        print('设备名称为:', b)
        sceneRecommend.get_id(self, self.scene_advice_button16).click()
        time.sleep(1)
        log.MyLog.info('有设备状态-点击继续添加设备pass')

    def click_button7(self):
        sceneRecommend.get_id(self, self.scene_advice_button11).click()
        sceneRecommend.find_toast(self, self.text2)
        time.sleep(1)
        log.MyLog.info('无设备状态-点击选择设备pass')

    def click_button8(self):
        sceneRecommend.get_id(self, self.scene_advice_button11).click()
        time.sleep(1)
        b = sceneRecommend.get_text(self, self.scene_advice_button16)
        print('设备名称为:', b)
        sceneRecommend.get_id(self, self.scene_advice_button16).click()
        time.sleep(1)
        log.MyLog.info('有设备状态-点击选择设备pass')

    def click_button9(self):
        sceneRecommend.get_id(self, self.scene_advice_button7).click()
        sceneRecommend.swipe_right(self)
        assert sceneRecommend.get_text(self, self.scene_advice_button32) == '删除'
        sceneRecommend.get_id(self, self.scene_advice_button32).click()
        sceneRecommend.find_toast(self, self.text15)
        time.sleep(1)
        log.MyLog.info('无设备状态-删除默认场景pass')

    def click_button10(self):
        sceneRecommend.get_id(self, self.scene_advice_button8).click()
        sceneRecommend.find_name(self, self.text5)
        sceneRecommend.find_name(self, self.text6)
        sceneRecommend.find_name(self, self.text7)
        time.sleep(1)
        log.MyLog.info('返回至场景推荐页pass')

    def click_button11(self):
        sceneRecommend.get_xpath_TextView(self, self.scene_advice_button9).click()
        assert sceneRecommend.get_text(self, self.scene_advice_button17) == '关机'
        sceneRecommend.get_xpath_TextView(self, self.scene_advice_button9).click()
        # sceneRecommend.get_id(self, self.scene_advice_button20).click()
        sceneRecommend.get_id(self, self.scene_advice_button21).send_keys("关机场景")
        sceneRecommend.get_id(self, self.scene_advice_button18).click()
        sceneRecommend.find_toast(self, self.text13)
        log.MyLog.info('关机场景创建pass')

    def click_button12(self):
        sceneRecommend.get_id(self, self.scene_advice_button22).click()
        sceneRecommend.get_id(self, self.scene_advice_button24).click()  # 制冷模式
        assert sceneRecommend.get_text(self, self.scene_advice_button30) == '26℃'
        sceneRecommend.get_id(self, self.scene_advice_button29).click()
        sceneRecommend.get_id(self, self.scene_advice_button31).click()
        assert sceneRecommend.get_text(self, self.scene_advice_button30) == '24℃'
        sceneRecommend.get_xpath_TextView(self, self.scene_advice_button9).click()
        assert sceneRecommend.get_text(self, self.scene_advice_button17) == '开机， 制冷24℃'
        sceneRecommend.get_xpath_TextView(self, self.scene_advice_button9).click()
        # sceneRecommend.get_id(self, self.scene_advice_button20).click()
        sceneRecommend.get_id(self, self.scene_advice_button21).send_keys("开机制冷场景")
        sceneRecommend.get_id(self, self.scene_advice_button18).click()
        sceneRecommend.find_toast(self, self.text13)
        log.MyLog.info('开机制冷场景创建pass')

    def click_button13(self):
        sceneRecommend.get_id(self, self.scene_advice_button22).click()
        if sceneRecommend.find_text(self, name="制热"):
            sceneRecommend.get_id(self, self.scene_advice_button25).click()  # 制热模式
            assert sceneRecommend.get_text(self, self.scene_advice_button30) == '26℃'
            sceneRecommend.get_id(self, self.scene_advice_button29).click()
            sceneRecommend.get_id(self, self.scene_advice_button31).click()
            assert sceneRecommend.get_text(self, self.scene_advice_button30) == '24℃'
            sceneRecommend.get_xpath_TextView(self, self.scene_advice_button9).click()
            assert sceneRecommend.get_text(self, self.scene_advice_button17) == '开机， 制热24℃'
            sceneRecommend.get_xpath_TextView(self, self.scene_advice_button9).click()
            # sceneRecommend.get_id(self, self.scene_advice_button20).click()
            sceneRecommend.get_id(self, self.scene_advice_button21).send_keys("开机制热场景")
            sceneRecommend.get_id(self, self.scene_advice_button18).click()
            sceneRecommend.find_toast(self, self.text13)
            log.MyLog.info('开机制热场景创建pass')
        else:
            log.MyLog.info("请确认当前设备是否是单冷机型，若是则执行无问题")
            return

    def click_button14(self):
        sceneRecommend.get_id(self, self.scene_advice_button22).click()
        sceneRecommend.get_id(self, self.scene_advice_button26).click()  # 除湿模式
        assert sceneRecommend.get_text(self, self.scene_advice_button30) == '26℃'
        sceneRecommend.get_id(self, self.scene_advice_button29).click()
        sceneRecommend.get_id(self, self.scene_advice_button31).click()
        assert sceneRecommend.get_text(self, self.scene_advice_button30) == '24℃'
        sceneRecommend.get_xpath_TextView(self, self.scene_advice_button9).click()
        assert sceneRecommend.get_text(self, self.scene_advice_button17) == '开机， 除湿24℃'
        sceneRecommend.get_xpath_TextView(self, self.scene_advice_button9).click()
        # sceneRecommend.get_id(self, self.scene_advice_button20).click()
        sceneRecommend.get_id(self, self.scene_advice_button21).send_keys("开机除湿场景")
        sceneRecommend.get_id(self, self.scene_advice_button18).click()
        sceneRecommend.find_toast(self, self.text13)
        log.MyLog.info('开机除湿场景创建pass')

    def click_button15(self):
        sceneRecommend.get_id(self, self.scene_advice_button22).click()
        sceneRecommend.get_id(self, self.scene_advice_button27).click()  # 送风模式
        sceneRecommend.get_xpath_TextView(self, self.scene_advice_button9).click()
        assert sceneRecommend.get_text(self, self.scene_advice_button17) == '开机， 送风'
        sceneRecommend.get_xpath_TextView(self, self.scene_advice_button9).click()
        # sceneRecommend.get_id(self, self.scene_advice_button20).click()
        sceneRecommend.get_id(self, self.scene_advice_button21).send_keys("开机送风场景")
        sceneRecommend.get_id(self, self.scene_advice_button18).click()
        sceneRecommend.find_toast(self, self.text13)
        log.MyLog.info('开机送风场景创建pass')

    def click_button16(self):
        sceneRecommend.get_id(self, self.scene_advice_button22).click()
        if sceneRecommend.find_text(self, name="自动"):
            sceneRecommend.get_id(self, self.scene_advice_button28).click()  # 自动模式
            sceneRecommend.get_xpath_TextView(self, self.scene_advice_button9).click()
            assert sceneRecommend.get_text(self, self.scene_advice_button17) == '开机， 自动'
            sceneRecommend.get_xpath_TextView(self, self.scene_advice_button9).click()
            # sceneRecommend.get_id(self, self.scene_advice_button20).click()
            sceneRecommend.get_id(self, self.scene_advice_button21).send_keys("开机自动场景")
            sceneRecommend.get_id(self, self.scene_advice_button18).click()
            sceneRecommend.find_toast(self, self.text13)
            log.MyLog.info('开机自动场景创建pass')
        else:
            log.MyLog.info("请确认当前设备是否是柜机机型，若是则执行无问题")
            return

    def click_button17(self):
        sceneRecommend.get_id(self, self.scene_advice_button19).click()
        sceneRecommend.find_toast(self, self.text14)
        time.sleep(1)
        log.MyLog.info('场景执行pass')

    def click_button18(self):
        sceneRecommend.get_id(self, self.scene_advice_button1).click()
        sceneRecommend.find_name(self, self.text8)
        sceneRecommend.get_id(self, self.scene_advice_button8).click()
        time.sleep(1)
        log.MyLog.info('场景日志pass')

    def click_button19(self):
        sceneRecommend.swipe_right(self)
        assert sceneRecommend.get_text(self, self.scene_advice_button32) == '删除'
        sceneRecommend.get_id(self, self.scene_advice_button32).click()
        sceneRecommend.get_id(self, self.scene_advice_button18).click()
        sceneRecommend.find_toast(self, self.text16)
        time.sleep(1)
        log.MyLog.info('有设备状态-删除新增场景pass')

    def click_button20(self):
        sceneRecommend.get_id(self, self.scene_advice_button6).click()
        sceneRecommend.get_id(self, self.scene_advice_button5).click()
        time.sleep(1)
        # log.MyLog.info('有设备状态-点击多设备快捷控制pass')

    def click_button21(self):
        sceneRecommend.get_xpath_TextView(self, self.scene_advice_button9).click()  # 未选设备点击确定
        sceneRecommend.find_toast(self, self.text1)
        sceneRecommend.get_id(self, self.scene_advice_button12).click()
        sceneRecommend.get_xpath_TextView(self, self.scene_advice_button9).click()  # 全选设备点击确定
        sceneRecommend.get_id(self, self.scene_advice_button21).send_keys("多设备快捷控制")
        sceneRecommend.get_id(self, self.scene_advice_button18).click()
        assert sceneRecommend.get_text(self, self.scene_advice_button15) == '多设备快捷控制'
        time.sleep(1)
        log.MyLog.info('集中控制场景创建pass')

    def click_button22(self):
        if sceneRecommend.find_text(self, name="已离线"):
            print('设备离线')
            sceneRecommend.get_id(self, self.scene_advice_button13).click()
            assert sceneRecommend.get_text(self, self.scene_advice_button33) == '其他问题'
            sceneRecommend.find_name(self, self.text9)
            sceneRecommend.get_name(self, self.text10).click()
            assert sceneRecommend.get_xpath_text(self, self.scene_advice_button14) == '其他问题'
            sceneRecommend.get_id(self, self.scene_advice_button8).click()
            assert sceneRecommend.get_text(self, self.scene_advice_button33) == '其他问题'
            sceneRecommend.get_id(self, self.scene_advice_button2).click()
            sceneRecommend.get_id(self, self.scene_advice_button8).click()
            time.sleep(1)
        else:
            print('设备在线')
            sceneRecommend.find_name(self, '制冷')
            sceneRecommend.find_name(self, '低档')
            sceneRecommend.find_name(self, '27')
            sceneRecommend.get_id(self, self.scene_advice_button8).click()
            time.sleep(1)
        log.MyLog.info('集中控制设备状态pass')


if __name__ == '__main__':
    driver = appPage.driver()
    sceneRecommend(driver).login_y_n()
    sceneRecommend(driver).click_button9()
