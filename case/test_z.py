# coding=utf-8
"""
Created on 2021-1-19
@author:Shenlei
Project:测试用例--需手动黑盒测试的功能模块
"""
import pytest
import allure
import os


@allure.epic('需手动黑盒测试的功能模块')
class TestClass:
    @allure.story('手机号注册--注册按钮')
    @allure.title('验证码正确点击注册成功测试')
    def test1(self):
        return

    @allure.story('QQ登录--QQ按钮')
    @allure.title('QQ登录成功测试')
    def test2(self):
        return

    @allure.story('微信登录--微信按钮')
    @allure.title('微信登录成功测试')
    def test3(self):
        return

    @allure.story('苹果登录--苹果按钮')
    @allure.title('苹果登录成功测试')
    def test4(self):
        return

    @allure.story('手机号登录--忘记密码')
    @allure.title('正确手机号，忘记密码并修改密码测试')
    def test5(self):
        return

    @allure.story('个人资料--头像')
    @allure.title('从相册或拍照方式修改头像测试')
    def test6(self):
        return

    @allure.story('设置--账号安全')
    @allure.title('修改密码测试')
    def test7(self):
        return

    @allure.story('设置--账号安全')
    @allure.title('账号注销测试')
    def test8(self):
        return

    @allure.story('设置--账号安全')
    @allure.title('手机号更换测试')
    def test9(self):
        return

    @allure.story('设置--账号安全')
    @allure.title('第三方平台绑定测试')
    def test10(self):
        return

    @allure.story('设置--去评价')
    @allure.title('给好评测试')
    def test11(self):
        return

    @allure.story('设置--去评价')
    @allure.title('去吐槽--意见反馈提交测试')
    def test12(self):
        return

    @allure.story('设置--关于奥云家')
    @allure.title('分享奥云家测试')
    def test13(self):
        return

    @allure.story('场景--新增场景')
    @allure.title('位置触发场景测试')
    def test14(self):
        return

    @allure.story('场景--新增场景')
    @allure.title('时间触发场景测试')
    def test15(self):
        return


if __name__ == '__main__':
    pytest.main(['--alluredir', '../report/result/', '--clean-alluredir', 'test_z.py'])
    split = 'allure generate ../report/result/ -o ../report/html --clean'
    os.system(split)
