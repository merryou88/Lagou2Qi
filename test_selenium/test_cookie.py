import json
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestCookie:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")

    @pytest.mark.skip
    def test_cookie(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        sleep(15)
        cookie = self.driver.get_cookies()
        with open("cookie.json", 'w') as f:
            json.dump(cookie, f)

    def test_cookie_login(self):
        cookies = json.load(open("cookie.json"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        while True:
            self.driver.refresh()
            res = WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable((By.ID, "menu_contacts")))
            print(res)
            if res is not None:
                break

        # expected_conditions.xx需要传入一个元组
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)")))
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()

        # sendkeys需要使用绝对路径
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, "js_upload_file_input")))
        ele = self.driver.find_element(By.ID, "js_upload_file_input")
        ele.send_keys("/Users/ouyanxia/PycharmProjects/Lagou2QiProject/test_selenium/data/tongxunlu.xlsx")

        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, "upload_file_name")))
        assert_ele = self.driver.find_element(By.ID, "upload_file_name").text
        assert assert_ele == "tongxunlu.xlsx"
        # self.driver.find_element(By.ID,"submit_csv").click()

        # self.driver.find_element(By.ID,"reloadContact")
        sleep(5000)

    def teardown(self):
        self.driver.quit()
