# coding=utf-8
"""
Created on 2021-1-6
@author:Shenlei
Project:App引导页
"""

from common.public import Element
from common import log
from page.desired_caps.driver_app2 import appPage


class BootProject(Element):
    text1 = ("界面全新改版")
    text2 = ('简化控制界面，优化用户体验')
    text3 = ("优化配网")
    text4 = ('优化配网流程，提升配网成功率')
    text5 = ("新增家庭")
    text6 = ('随时切换家庭，快捷控制')
    text7 = ("数据隐私声明")
    text8 = (
        '我们非常尊重用户个人信息的保护。保护每个客户、供应商和员工的个人隐私是获得和保持利益关系人信任的关键部分。'
        '我们希望通过下面列出的隐私政策，向您阐明我们如何致力于保护您的个人信息的安全和隐私。在您使用奥克斯平台提供的服务时，'
        '我们将按照本隐私权政策收集、使用及共享您的个人信息。本隐私权政策包含了我们收集、存储、使用、共享和保护您的个人信息的条款，'
        '建议您完整地阅读《用户协议》和《隐私政策》，以帮助您了解维护自己隐私权的方式。')
    text9 = ("奥云家隐私政策")
    boot_button1 = ('com.broadlink.auxair:id/btnok')  # 立即体验按钮
    boot_button2 = ("com.broadlink.auxair:id/btn2")  # 同意按钮/确定按钮
    boot_button3 = ("com.broadlink.auxair:id/btn1")  # 不同意按钮/取消按钮

    def click_button1(self):
        self.get_id(self.boot_button1).click()  # 点击立即体验

    def click_button2(self):
        BootProject.find_name(self, self.text7)
        BootProject.find_name(self, self.text8)
        BootProject.get_id(self, self.boot_button2).click()  # 点击同意
        log.MyLog.info('同意隐私声明pass')

    def click_button3(self):
        BootProject.find_name(self, self.text7)
        BootProject.find_name(self, self.text8)
        BootProject.get_id(self, self.boot_button3).click()  # 点击不同意
        log.MyLog.info('不同意隐私声明pass')

    def click_button4(self):
        BootProject.find_name(self, self.text9)
        BootProject.get_id(self, self.boot_button2).click()  # 点击确定
        log.MyLog.info('确定奥云家隐私政策pass')

    def boot(self):
        log.MyLog.info("-------开始引导页测试-------")
        BootProject.find_name(self, self.text1)
        BootProject.find_name(self, self.text2)
        BootProject.swipe_to_right(self)
        log.MyLog.info('-------启动页第一页文字显示正确-------')
        BootProject.find_name(self, self.text3)
        BootProject.find_name(self, self.text4)
        BootProject.swipe_to_right(self)
        log.MyLog.info('-------启动页第二页文字显示正确-------')
        BootProject.find_name(self, self.text5)
        BootProject.find_name(self, self.text6)
        BootProject.click_button1(self)
        log.MyLog.info('-------启动页第三页文字显示正确-------')
        log.MyLog.info("-------结束引导页测试-------")
        # BootProject.find_name(self, self.text7)
        # BootProject.find_name(self, self.text8)
        # BootProject.click_button2(self)


if __name__ == '__main__':
    driver = appPage.driver()
    BootProject(driver).click_button2()
    BootProject(driver).boot()
    BootProject(driver).click_button4()
