from test_wework.page.main_page import MainPage


class Test_DelMember:
    def test_del_member(self):
        del_name="李五"
        self.main = MainPage()
        assert del_name not in self.main.goto_contact().del_member(del_name)
