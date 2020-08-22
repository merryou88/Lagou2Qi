from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_wework.page.base_page import BasePage


class Contact(BasePage):
    def get_member(self):
        eles = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        name_list = [ele.get_attribute('title') for ele in eles]
        return name_list

    def del_member(self, name):
        name_list = self.get_member()
        for index in range(1, len(name_list)):
            search_name = self.find(By.XPATH, f'//*[@id="member_list"]/tr[{index}]/td[2]').get_attribute("title")
            if search_name == name:
                self.find(By.XPATH, f'//*[@id="member_list"]/tr[{index}]/td[1]/input').click()
                WebDriverWait(self.driver, 10).until(
                    expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".js_delete")))
                self.find(By.CSS_SELECTOR, ".js_delete").click()
                WebDriverWait(self.driver, 10).until(
                    expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]')))
                self.find(By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]').click()
                break
        self.driver.refresh()
        new_name_list = self.get_member()
        return new_name_list
