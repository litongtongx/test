from selenium.webdriver.common.by import By
from common.logGen import LogGen
from pages.basepage import BasePage
logger = LogGen(__name__).get_log()


class MainPage(BasePage):
    true_name = (By.XPATH, "//*[@id='w7']/li[2]/a")

    def get_true_name(self):
        return self.find_element(*self.true_name).text
        logger.info("获取登陆后页面用户名名称")