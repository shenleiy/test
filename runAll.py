import pytest
import os

if __name__ == '__main__':
    pytest.main(['--alluredir', '../report/result/', '--clean-alluredir', '-v', './case'])
    split = 'allure generate ../report/result/ -o ../report/html --clean'
    os.system(split)


# pytest --alluredir ../report/result/ --clean-alluredir -v -s
# allure generate ../report/result/ -o ../report/html --clean
# 命令行操作
