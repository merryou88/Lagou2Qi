from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver_basepage: WebDriver = None):
        _base_url = ""
        if driver_basepage == None:
            option = Options()
            # 端口号与启动命令一致
            option.debugger_address = "localhost:9222"
            self.driver = webdriver.Chrome(options=option)
            if _base_url != "":
                self.driver.get(_base_url)
        else:
            self.driver = driver_basepage
        self.driver.implicitly_wait(3)

    def find(self, by, value):
        return self.driver.find_element(by, value)

    def finds(self, by, value):
        return self.driver.find_elements(by, value)

    def quit(self):
        self.driver.quit()
