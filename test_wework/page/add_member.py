from time import sleep

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from test_wework.page.base_page import BasePage
from test_wework.page.contact_page import Contact

class AddMember(BasePage):

    def add_member(self):
        "添加成员"
        self.find(By.ID,'username').send_keys('王晓敏')
        self.find(By.ID,'memberAdd_acctid').send_keys('1005')
        self.find(By.ID,'memberAdd_phone').send_keys('13566660005')
        self.find(By.CSS_SELECTOR,'.js_btn_save').click()
        return Contact(self.driver)