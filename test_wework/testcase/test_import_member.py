from test_wework.page.main_page import MainPage


class Test_ImportMember():
    def test_importmember(self):
        filepath="/Users/ouyanxia/PycharmProjects/Lagou2QiProject/test_wework/member/tongxunlu.xlsx"
        filename="tongxunlu.xlsx"
        self.main = MainPage()
        newmember=self.main.goto_import_contact().import_member(filepath,filename).get_member()
        assert "李一" in newmember