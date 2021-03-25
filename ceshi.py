import pytest
import allure


@pytest.fixture(scope='function')  # 相当于setup
def start():
    print('start')

    yield  # 相当于teardown
    print('end')


@pytest.mark.usefixtures('start')
class TestClass:
    def test(self):
        print('测试')

    def test1(self):
        print('测试1')


class TestClass1:
    def test(self):
        print('测试')

    def test1(self):
        print('测试1')


if __name__ == '__main__':
    pytest.main(['ceshi.py', '-s'])
