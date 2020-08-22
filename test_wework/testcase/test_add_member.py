from test_wework.page.main_page import MainPage


class TestAddMember:
    def test_add_member(self):
        self.main = MainPage()
        # 1.点击添加成员，跳转到添加成员页
        # 2。填写成员信息
        # 3。点击保存
        # 4。断言是否添加成功
        assert "王翠敏" not in self.main.goto_add_member().add_member().get_member()

    def teardown(self):
        self.main.quit()
