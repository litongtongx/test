from selenium import webdriver
from pages import basepage
from selenium.webdriver.common.by import By
from common.logGen import LogGen
logger = LogGen(__name__).get_log()


class LoginPage(basepage.BasePage):
    username = (By.ID, "loginform-identity")
    password = (By.ID, "loginform-password")
    submit = (By.NAME, "login-button")

    def input_username(self, username):
        self.find_element(*self.username).send_keys(username)
        logger.info("输入用户名:{}".format(username))

    def input_password(self,password):
        self.find_element(*self.password).send_keys(password)
        logger.info("输入密码：{}".format(password))

    def click_submit(self):
        self.find_element(*self.submit).click()
        logger.info("点击登录按钮")