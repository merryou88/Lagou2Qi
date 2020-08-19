import pytest
import yaml


@pytest.mark.parametrize('a,b', yaml.safe_load(open('test_cal.yml')))
class TestCal:

    def test_add(self, cal, a, b):
        assert a + b == cal.add(a, b)

    def test_sub(self, cal, a, b):
        assert a - b == cal.sub(a, b)

    def test_mul(self, cal, a, b):
        assert a * b == cal.mul(a, b)

    def test_div(self, cal, a, b):
        assert a / b == cal.div(a, b)
