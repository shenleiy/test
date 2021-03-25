import pytest
import allure
import os
from page.desired_caps.driver_app import appPage
from page.page_network.device_network import adviceNetwork

print("请确认当前账号下是否有设备？按Y/N")
content = input("请输入：")
if content == "Y":
    if __name__ == '__main__':
        pytest.main(['-s', 'test_scene_yes.py'])
else:
    driver = appPage.driver()
    adviceNetwork(driver).login_y_n()
    adviceNetwork(driver).click_button1()
    print("请确认当前设备配网是否成功？按Y/N")
    content = input("请输入：")
    if content == "Y":
        if __name__ == '__main__':
            pytest.main(['-s', 'test_scene_yes.py'])
        else:
            print('配网失败,需重新开始')

if __name__ == '__main__':
    pytest.main(['-s', 'test_decide.py'])
