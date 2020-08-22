from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_wework.page.add_member import AddMember
from test_wework.page.base_page import BasePage
from test_wework.page.contact_page import Contact
from test_wework.page.import_member import ImportMember


class MainPage(BasePage):
    _base_url="https://work.weixin.qq.com/wework_admin/frame#index"
    def goto_add_member(self):
        # click
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)")))
        self.find(By.CSS_SELECTOR,".index_service_cnt_itemWrap:nth-child(1)").click()
        return AddMember(self.driver)

    def goto_contact(self):
        self.find(By.ID, "menu_contacts").click()
        return Contact(self.driver)

    def goto_import_contact(self):
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        return ImportMember(self.driver)
