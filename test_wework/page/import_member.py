from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_wework.page.base_page import BasePage
from test_wework.page.contact_page import Contact


class ImportMember(BasePage):
    def import_member(self,filepath,filename):
        self.find(By.ID, 'js_upload_file_input').send_keys(filepath)
        assert_ele = self.driver.find_element(By.ID, "upload_file_name").text
        assert assert_ele == filename
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.ID,"submit_csv")))
        self.find(By.ID,"submit_csv").click()
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.ID,"reloadContact")))
        self.find(By.ID,"reloadContact").click()
        return Contact(self.driver)

