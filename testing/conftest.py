from typing import List

import pytest
import yaml

from pythoncode.calculator import Calculator


@pytest.fixture(scope='session')
def cal():
    print('开始计算')
    calcula = Calculator()
    yield calcula
    print('计算结束')


def pytest_collection_modifyitems(
        session: 'Session', config: 'Config', items: List['Items']) -> None:
    items.reverse()
    for item in items:
        print(item.nodeid)
        if 'mar' in item.nodeid:
            item.add_marker(pytest.mark.mar)
    pass


def pytest_addoption(parser):
    mygroup = parser.getgroup("lagou")
    mygroup.addoption("--env",
                      default='test',
                      dest='env',
                      help='set the pytest environment')
    mygroup.addoption("--env0",
                      default='dev',
                      dest='dev',
                      help='set the pytest environment')
    mygroup.addoption("--env1",
                      default='dev',
                      dest='st',
                      help='set the pytest environment')

@pytest.fixture(scope='session')
def cmd_option(request):
    myenv=request.config.getoption('--env',default='test')
    if myenv == 'test':
        print('获取测试数据')
        with open('datas/test/test.yml') as f:
            datas=yaml.safe_load(f)
    elif myenv=='dev':
        print('获取开发数据')
        with open('datas/dev/dev.yml') as d:
            datas=yaml.safe_load(d)
    elif myenv=='st':
        print('获取st数据')
        with open('datas/st/st.yml') as s:
            datas=yaml.safe_load(s)
    return datas