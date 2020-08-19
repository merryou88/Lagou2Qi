import pytest

from pythoncode.calculator import Calculator


@pytest.fixture(scope='session')
def cal():
    print('开始计算')
    calcula = Calculator()
    yield calcula
    print('计算结束')