from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.picCapture import capture_pic
from common.logGen import LogGen
logger = LogGen(logger=__name__).get_log()


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            capture_pic(self.driver)
            logger.info("{}页面中未找到{}元素".format(self, loc))

    # def send_keys(self, loc, value):
    #     try:
    #         # getattr获取对象属性值
    #         loc = getattr(self, "_%s" % loc)
    #         self.find_element(*loc).send_keys(value)
    #     except AttributeError:
    #         capture_pic(self.driver)
    #         logger.info("{}页面中未找到{}元素".format(self, loc))
    #
    # def click(self, loc):
    #     try:
    #         loc = getattr(self, "_%s" % loc)
    #         self.find_element(*loc).click()
    #     except AttributeError:
    #         capture_pic(self.driver)
    #         logger.info("{}页面中未找到{}元素".format(self, loc))

