import pytest
import yaml


@pytest.mark.parametrize('a,b', yaml.safe_load(open('test_cal.yml')))
class TestCal:

    @pytest.mark.run(order=1)
    def test_add(self, cal, a, b):
        assert a + b == cal.add(a, b)

    @pytest.mark.run(order=2)
    @pytest.mark.dependency(depends=['test_add'])
    def test_sub(self, cal, a, b):
        assert a - b == cal.sub(a, b)

    @pytest.mark.run(order=3)
    def check_mul(self, cal, a, b):
        assert a * b == cal.mul(a, b)

    @pytest.mark.run(order=4)
    @pytest.mark.dependency(depends=['check_mul'])
    def check_div(self, cal, a, b):
        assert a / b == cal.div(a, b)
